"""Adapt plain values to the generated client's union models."""
from typing import Any
from activitysmith_openapi.models.live_activity_value import LiveActivityValue

from activitysmith_openapi.models.activity_metric_value import ActivityMetricValue
from activitysmith_openapi.models.metric_value_update_request_value import MetricValueUpdateRequestValue


def _wrap_value(value: Any, model: Any) -> Any:
    if isinstance(value, model):
        return value
    if isinstance(value, bool) or not isinstance(value, (int, float, str, dict)):
        raise ValueError("ActivitySmith: metric value must be a number or string")
    if isinstance(value, dict):
        if "actual_instance" not in value:
            raise ValueError("ActivitySmith: metric value must be a number or string")
        return model.model_validate(value)
    return model(value)


def normalize_live_activity_request(request: Any) -> Any:
    request = normalize_metadata_request(request)
    if not isinstance(request, dict):
        return request
    state = request.get("content_state")
    if not isinstance(state, dict):
        return request
    if "value" in state:
        state = {**state, "value": _wrap_value(state["value"], LiveActivityValue)}
        request = {**request, "content_state": state}
    if not isinstance(state.get("metrics"), (list, tuple)):
        return request
    metrics = []
    for metric in state["metrics"]:
        if isinstance(metric, dict) and "value" in metric:
            metric = {**metric, "value": _wrap_value(metric["value"], ActivityMetricValue)}
        metrics.append(metric)
    return {**request, "content_state": {**state, "metrics": metrics}}


def normalize_metric_request(request: Any) -> Any:
    if isinstance(request, dict) and "value" in request:
        return {**request, "value": _wrap_value(request["value"], MetricValueUpdateRequestValue)}
    return request


def normalize_metadata_request(request: Any) -> Any:
    if not isinstance(request, dict) or "metadata" not in request:
        return request
    from activitysmith_openapi.models.metadata_value import MetadataValue
    metadata = request["metadata"]
    if not isinstance(metadata, dict):
        raise ValueError("ActivitySmith: metadata must be an object")
    return {**request, "metadata": {
        key: value if isinstance(value, MetadataValue) else MetadataValue(value)
        for key, value in metadata.items()
    }}
