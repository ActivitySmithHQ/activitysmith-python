from copy import deepcopy

import pytest

from activitysmith import ActivitySmith
from activitysmith.client import content_state, metric
from activitysmith_openapi.api_client import ApiClient
from activitysmith_openapi.models.activity_metric_value import ActivityMetricValue
from activitysmith_openapi.models.metric_value_update_request_value import MetricValueUpdateRequestValue
from activitysmith_openapi.models.metric_value_update_request import MetricValueUpdateRequest


class RequestCaptured(Exception):
    pass


@pytest.fixture
def requests(monkeypatch):
    captured = []

    def capture(self, method, url, header_params=None, body=None, post_params=None, **kwargs):
        captured.append(body)
        raise RequestCaptured

    monkeypatch.setattr(ApiClient, "call_api", capture)
    return captured


@pytest.mark.parametrize("value", [0, 42, 3.5, "Healthy"])
@pytest.mark.parametrize("method", ["start", "update", "end", "stream", "end_stream"])
@pytest.mark.parametrize("form", ["dict", "named", "helper", "wrapped"])
def test_live_activity_metric_serializes_native_values(requests, value, method, form):
    activitysmith = ActivitySmith(api_key="test")
    state = {"title": "Status", "type": "stats", "metrics": [{"label": "Value", "value": value}]}
    if form == "wrapped":
        state["metrics"][0]["value"] = ActivityMetricValue(value)
    if form == "helper":
        state = content_state("Status", type="stats", metrics=[metric("Value", value)])
    original = deepcopy(state)
    request = {"content_state": state}
    if method in ("update", "end"):
        request["activity_id"] = "activity-1"
    args = ["status"] if method in ("stream", "end_stream") else []
    with pytest.raises(RequestCaptured):
        if form == "named":
            kwargs = dict(state)
            if method in ("update", "end"):
                kwargs["activity_id"] = "activity-1"
            getattr(activitysmith.live_activities, method)(*args, **kwargs)
        else:
            getattr(activitysmith.live_activities, method)(*args, request)
    assert requests[-1]["content_state"]["metrics"][0]["value"] == value
    assert state == original


@pytest.mark.parametrize("value", [0, 42, 3.5, "Healthy"])
@pytest.mark.parametrize("form", ["scalar", "dict", "wrapped", "model", "legacy"])
def test_widget_metric_serializes_native_values(requests, value, form):
    activitysmith = ActivitySmith(api_key="test")
    request = {"value": value, "timestamp": "2026-09-15T00:00:00Z"}
    if form == "wrapped":
        request["value"] = MetricValueUpdateRequestValue(value)
    if form == "model":
        request = MetricValueUpdateRequest(value=MetricValueUpdateRequestValue(value))
    original = deepcopy(request)
    with pytest.raises(RequestCaptured):
        if form == "scalar":
            activitysmith.metrics.update("status", value)
        elif form == "legacy":
            activitysmith.metrics.update_metric_value("status", request)
        else:
            activitysmith.metrics.update("status", request)
    assert requests[-1]["value"] == value
    assert request == original


@pytest.mark.parametrize("value", [True, [], {}])
def test_invalid_metric_values_do_not_reach_transport(requests, value):
    activitysmith = ActivitySmith(api_key="test")
    with pytest.raises(ValueError):
        activitysmith.metrics.update("status", value)
    assert requests == []


@pytest.mark.parametrize("method", ["update", "end"])
@pytest.mark.parametrize("tags", [None, ["billing"], []])
@pytest.mark.parametrize("form", ["dict", "named"])
def test_legacy_tags_serialized(requests, method, tags, form):
    client = ActivitySmith(api_key="test")
    fields = {"activity_id": "activity-1", "content_state": {"title": "Job"}}
    if tags is not None:
        fields["tags"] = tags
    with pytest.raises(RequestCaptured):
        if form == "named":
            getattr(client.live_activities, method)(**fields)
        else:
            getattr(client.live_activities, method)(fields)
    assert ("tags" in requests[-1]) == (tags is not None)
    if tags is not None:
        assert requests[-1]["tags"] == tags


@pytest.mark.parametrize("method", ["send", "start", "update", "end", "stream", "end_stream"])
@pytest.mark.parametrize("metadata", [None, {}, {"order": "382", "ready": False, "count": 0, "empty": "", "ratio": 1.25}])
@pytest.mark.parametrize("form", ["dict", "named"])
def test_metadata_serialization(requests, method, metadata, form):
    client = ActivitySmith(api_key="test")
    fields = {"title": "Job"} if method == "send" else {"content_state": {"title": "Job", "type": "progress"}}
    if method in ("update", "end"):
        fields["activity_id"] = "activity-1"
    if metadata is not None:
        fields["metadata"] = metadata
    resource = client.notifications if method == "send" else client.live_activities
    args = ["job"] if method in ("stream", "end_stream") else []
    with pytest.raises(RequestCaptured):
        if form == "named":
            getattr(resource, method)(*args, **fields)
        else:
            getattr(resource, method)(*args, fields)
    body = requests[-1]
    assert ("metadata" in body) == (metadata is not None)
    if metadata is not None:
        assert body["metadata"] == metadata
        assert body["metadata"].get("ready", False) is False
    assert "metadata" not in body.get("content_state", {})


@pytest.mark.parametrize("url", ["http://example.com", "https://example.com", "shortcuts://run-shortcut?name=Test", "spotify://", "spotify:track:123"])
def test_external_push_urls(requests, url):
    client = ActivitySmith(api_key="test")
    with pytest.raises(RequestCaptured):
        client.notifications.send(title="Job", redirection=url, actions=[{"title":"Open", "type":"open_url", "url":url}])
    assert requests[-1]["redirection"] == url
    assert requests[-1]["actions"][0]["url"] == url

@pytest.mark.parametrize("tags", [None, [], ["finished"]])
def test_end_stream_tags(requests, tags):
    client = ActivitySmith(api_key="test")
    with pytest.raises(RequestCaptured):
        client.live_activities.end_stream("job", tags=tags, metadata={})
    assert ("tags" in requests[-1]) == (tags is not None)
    if tags is not None:
        assert requests[-1]["tags"] == tags
    assert requests[-1]["metadata"] == {}


@pytest.mark.parametrize("value", ["$1,240", "0007", "", 0, -12.75])
@pytest.mark.parametrize("method", ["start", "update", "end", "stream", "end_stream"])
@pytest.mark.parametrize("form", ["dict", "named", "helper"])
def test_prominent_value_serializes_without_losing_format(requests, value, method, form):
    activitysmith = ActivitySmith(api_key="test")
    state = content_state("Revenue", type="value", value=value)
    request = {"content_state": state}
    if method in ("update", "end"):
        request["activity_id"] = "activity-1"
    args = ["revenue"] if method in ("stream", "end_stream") else []
    with pytest.raises(RequestCaptured):
        if form == "named":
            kwargs = dict(state)
            if method in ("update", "end"):
                kwargs["activity_id"] = "activity-1"
            getattr(activitysmith.live_activities, method)(*args, **kwargs)
        else:
            getattr(activitysmith.live_activities, method)(*args, request)
    assert requests[-1]["content_state"]["value"] == value
    assert isinstance(requests[-1]["content_state"]["value"], str) == isinstance(value, str)
