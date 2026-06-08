# activitysmith_openapi.LiveActivitiesApi

All URIs are relative to *https://activitysmith.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**end_live_activity**](LiveActivitiesApi.md#end_live_activity) | **POST** /live-activity/end | End a Live Activity (legacy manual lifecycle)
[**end_live_activity_stream**](LiveActivitiesApi.md#end_live_activity_stream) | **DELETE** /live-activity/stream/{stream_key} | End a stream
[**reconcile_live_activity_stream**](LiveActivitiesApi.md#reconcile_live_activity_stream) | **PUT** /live-activity/stream/{stream_key} | Start a new Live Activity or update an existing one
[**start_live_activity**](LiveActivitiesApi.md#start_live_activity) | **POST** /live-activity/start | Start a Live Activity (legacy manual lifecycle)
[**update_live_activity**](LiveActivitiesApi.md#update_live_activity) | **POST** /live-activity/update | Update a Live Activity (legacy manual lifecycle)


# **end_live_activity**
> LiveActivityEndResponse end_live_activity(live_activity_end_request)

End a Live Activity (legacy manual lifecycle)

Legacy manual lifecycle endpoint. For new integrations, use DELETE /live-activity/stream/{stream_key} to end a managed Live Activity stream. This endpoint remains supported for existing integrations and advanced lifecycle control. Ends a Live Activity and archives its lifecycle. Supports segmented_progress, progress, metrics, stats, alert, and timer activity types. For segmented_progress activities, you can send the latest number_of_steps here if the workflow changed after start.

### Example

* Bearer (API Key) Authentication (apiKeyAuth):

```python
import activitysmith_openapi
from activitysmith_openapi.models.live_activity_end_request import LiveActivityEndRequest
from activitysmith_openapi.models.live_activity_end_response import LiveActivityEndResponse
from activitysmith_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://activitysmith.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = activitysmith_openapi.Configuration(
    host = "https://activitysmith.com/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (API Key): apiKeyAuth
configuration = activitysmith_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with activitysmith_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = activitysmith_openapi.LiveActivitiesApi(api_client)
    live_activity_end_request = {"activity_id":"pLAr-Hnq9ZFW4sxlk43Lhbuok4GLh7UW","content_state":{"title":"Nightly database backup","subtitle":"verify restore","number_of_steps":3,"current_step":3,"auto_dismiss_minutes":2}} # LiveActivityEndRequest | 

    try:
        # End a Live Activity (legacy manual lifecycle)
        api_response = api_instance.end_live_activity(live_activity_end_request)
        print("The response of LiveActivitiesApi->end_live_activity:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LiveActivitiesApi->end_live_activity: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **live_activity_end_request** | [**LiveActivityEndRequest**](LiveActivityEndRequest.md)|  | 

### Return type

[**LiveActivityEndResponse**](LiveActivityEndResponse.md)

### Authorization

[apiKeyAuth](../README.md#apiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Live Activity ended |  -  |
**403** | Forbidden (activity not owned by this API key account) |  -  |
**429** | Rate limit exceeded |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **end_live_activity_stream**
> LiveActivityStreamDeleteResponse end_live_activity_stream(stream_key, live_activity_stream_delete_request=live_activity_stream_delete_request)

End a stream

Use this endpoint when the process you are tracking is finished and you no longer want the Live Activity on your devices. ActivitySmith ends the current Live Activity for this stream and dismisses it from devices. If you need direct lifecycle control, use /live-activity/start, /live-activity/update, and /live-activity/end instead.

### Example

* Bearer (API Key) Authentication (apiKeyAuth):

```python
import activitysmith_openapi
from activitysmith_openapi.models.live_activity_stream_delete_request import LiveActivityStreamDeleteRequest
from activitysmith_openapi.models.live_activity_stream_delete_response import LiveActivityStreamDeleteResponse
from activitysmith_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://activitysmith.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = activitysmith_openapi.Configuration(
    host = "https://activitysmith.com/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (API Key): apiKeyAuth
configuration = activitysmith_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with activitysmith_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = activitysmith_openapi.LiveActivitiesApi(api_client)
    stream_key = 'stream_key_example' # str | Stable identifier for one ongoing thing. Allowed characters: letters, numbers, underscores, and hyphens.
    live_activity_stream_delete_request = {} # LiveActivityStreamDeleteRequest |  (optional)

    try:
        # End a stream
        api_response = api_instance.end_live_activity_stream(stream_key, live_activity_stream_delete_request=live_activity_stream_delete_request)
        print("The response of LiveActivitiesApi->end_live_activity_stream:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LiveActivitiesApi->end_live_activity_stream: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stream_key** | **str**| Stable identifier for one ongoing thing. Allowed characters: letters, numbers, underscores, and hyphens. | 
 **live_activity_stream_delete_request** | [**LiveActivityStreamDeleteRequest**](LiveActivityStreamDeleteRequest.md)|  | [optional] 

### Return type

[**LiveActivityStreamDeleteResponse**](LiveActivityStreamDeleteResponse.md)

### Authorization

[apiKeyAuth](../README.md#apiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Managed stream ended |  -  |
**400** | Bad request (invalid stream_key or action) |  -  |
**404** | Managed stream not found |  -  |
**429** | Rate limit exceeded |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **reconcile_live_activity_stream**
> LiveActivityStreamPutResponse reconcile_live_activity_stream(stream_key, live_activity_stream_request)

Start a new Live Activity or update an existing one

Use a stable stream_key for each ongoing thing you want to show as a Live Activity. Send the latest content_state whenever it changes, and ActivitySmith will keep the Live Activity in sync. For timer streams, send duration_seconds to start or reset the timer; omit duration_seconds on later updates to preserve the existing timer window.

### Example

* Bearer (API Key) Authentication (apiKeyAuth):

```python
import activitysmith_openapi
from activitysmith_openapi.models.live_activity_stream_put_response import LiveActivityStreamPutResponse
from activitysmith_openapi.models.live_activity_stream_request import LiveActivityStreamRequest
from activitysmith_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://activitysmith.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = activitysmith_openapi.Configuration(
    host = "https://activitysmith.com/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (API Key): apiKeyAuth
configuration = activitysmith_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with activitysmith_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = activitysmith_openapi.LiveActivitiesApi(api_client)
    stream_key = 'stream_key_example' # str | Stable identifier for one ongoing thing. Allowed characters: letters, numbers, underscores, and hyphens.
    live_activity_stream_request = {"content_state":{"title":"Server Health","subtitle":"prod-web-1","type":"metrics","metrics":[{"label":"CPU","value":27,"unit":"%"},{"label":"MEM","value":64,"unit":"%"}]}} # LiveActivityStreamRequest | 

    try:
        # Start a new Live Activity or update an existing one
        api_response = api_instance.reconcile_live_activity_stream(stream_key, live_activity_stream_request)
        print("The response of LiveActivitiesApi->reconcile_live_activity_stream:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LiveActivitiesApi->reconcile_live_activity_stream: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stream_key** | **str**| Stable identifier for one ongoing thing. Allowed characters: letters, numbers, underscores, and hyphens. | 
 **live_activity_stream_request** | [**LiveActivityStreamRequest**](LiveActivityStreamRequest.md)|  | 

### Return type

[**LiveActivityStreamPutResponse**](LiveActivityStreamPutResponse.md)

### Authorization

[apiKeyAuth](../README.md#apiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Stream reconciled |  -  |
**400** | Bad request (invalid stream_key, payload, action, or channel targeting input) |  -  |
**403** | Forbidden (API key scope or channel assignment violation) |  -  |
**404** | No recipients found for effective channel target |  -  |
**429** | Rate limit exceeded |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **start_live_activity**
> LiveActivityStartResponse start_live_activity(live_activity_start_request)

Start a Live Activity (legacy manual lifecycle)

Legacy manual lifecycle endpoint. For new integrations, use PUT /live-activity/stream/{stream_key} so ActivitySmith can manage start, update, rotation, and end state for you. This endpoint remains supported for existing integrations and advanced lifecycle control. Starts a Live Activity on devices matched by API key scope and optional target channels. Supports segmented_progress, progress, metrics, stats, alert, and timer activity types. For segmented_progress activities, number_of_steps can be changed later during update or end calls if the workflow changes.

### Example

* Bearer (API Key) Authentication (apiKeyAuth):

```python
import activitysmith_openapi
from activitysmith_openapi.models.live_activity_start_request import LiveActivityStartRequest
from activitysmith_openapi.models.live_activity_start_response import LiveActivityStartResponse
from activitysmith_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://activitysmith.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = activitysmith_openapi.Configuration(
    host = "https://activitysmith.com/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (API Key): apiKeyAuth
configuration = activitysmith_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with activitysmith_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = activitysmith_openapi.LiveActivitiesApi(api_client)
    live_activity_start_request = {"content_state":{"title":"Nightly database backup","subtitle":"create snapshot","number_of_steps":3,"current_step":1,"type":"segmented_progress","color":"yellow"}} # LiveActivityStartRequest | 

    try:
        # Start a Live Activity (legacy manual lifecycle)
        api_response = api_instance.start_live_activity(live_activity_start_request)
        print("The response of LiveActivitiesApi->start_live_activity:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LiveActivitiesApi->start_live_activity: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **live_activity_start_request** | [**LiveActivityStartRequest**](LiveActivityStartRequest.md)|  | 

### Return type

[**LiveActivityStartResponse**](LiveActivityStartResponse.md)

### Authorization

[apiKeyAuth](../README.md#apiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Live Activity started |  -  |
**400** | Bad request (invalid payload or channel targeting input) |  -  |
**403** | Forbidden (API key scope or channel assignment violation) |  -  |
**404** | No recipients found for effective channel target |  -  |
**429** | Rate limit exceeded |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_live_activity**
> LiveActivityUpdateResponse update_live_activity(live_activity_update_request)

Update a Live Activity (legacy manual lifecycle)

Legacy manual lifecycle endpoint. For new integrations, use PUT /live-activity/stream/{stream_key} so ActivitySmith can manage start, update, rotation, and end state for you. This endpoint remains supported for existing integrations and advanced lifecycle control. Updates an existing Live Activity. If the per-activity token is not registered yet, the update is queued. Supports segmented_progress, progress, metrics, stats, alert, and timer activity types. For segmented_progress activities, you can increase or decrease number_of_steps here as the workflow changes. For timer activities, send duration_seconds only when you want to reset the timer window; omit it to keep the current timer running.

### Example

* Bearer (API Key) Authentication (apiKeyAuth):

```python
import activitysmith_openapi
from activitysmith_openapi.models.live_activity_update_request import LiveActivityUpdateRequest
from activitysmith_openapi.models.live_activity_update_response import LiveActivityUpdateResponse
from activitysmith_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://activitysmith.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = activitysmith_openapi.Configuration(
    host = "https://activitysmith.com/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (API Key): apiKeyAuth
configuration = activitysmith_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with activitysmith_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = activitysmith_openapi.LiveActivitiesApi(api_client)
    live_activity_update_request = {"activity_id":"pLAr-Hnq9ZFW4sxlk43Lhbuok4GLh7UW","content_state":{"title":"Nightly database backup","subtitle":"upload archive","number_of_steps":3,"current_step":2}} # LiveActivityUpdateRequest | 

    try:
        # Update a Live Activity (legacy manual lifecycle)
        api_response = api_instance.update_live_activity(live_activity_update_request)
        print("The response of LiveActivitiesApi->update_live_activity:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LiveActivitiesApi->update_live_activity: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **live_activity_update_request** | [**LiveActivityUpdateRequest**](LiveActivityUpdateRequest.md)|  | 

### Return type

[**LiveActivityUpdateResponse**](LiveActivityUpdateResponse.md)

### Authorization

[apiKeyAuth](../README.md#apiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Live Activity updated (or queued) |  -  |
**403** | Forbidden (activity not owned by this API key account) |  -  |
**429** | Rate limit exceeded |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

