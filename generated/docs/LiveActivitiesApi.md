# openapi_client.LiveActivitiesApi

All URIs are relative to *https://activitysmith.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**end_live_activity**](LiveActivitiesApi.md#end_live_activity) | **POST** /live-activity/end | End a Live Activity
[**start_live_activity**](LiveActivitiesApi.md#start_live_activity) | **POST** /live-activity/start | Start a Live Activity
[**update_live_activity**](LiveActivitiesApi.md#update_live_activity) | **POST** /live-activity/update | Update a Live Activity


# **end_live_activity**
> LiveActivityEndResponse end_live_activity(live_activity_end_request)

End a Live Activity

Ends a Live Activity and archives its lifecycle.

### Example

* Bearer (API Key) Authentication (bearerAuth):

```python
import openapi_client
from openapi_client.models.live_activity_end_request import LiveActivityEndRequest
from openapi_client.models.live_activity_end_response import LiveActivityEndResponse
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://activitysmith.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://activitysmith.com/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (API Key): bearerAuth
configuration = openapi_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.LiveActivitiesApi(api_client)
    live_activity_end_request = {"activity_id":"pLAr-Hnq9ZFW4sxlk43Lhbuok4GLh7UW","content_state":{"title":"ActivitySmith API Deployment","subtitle":"done","current_step":4,"auto_dismiss_minutes":3}} # LiveActivityEndRequest | 

    try:
        # End a Live Activity
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

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Live Activity ended |  -  |
**429** | Rate limit exceeded |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **start_live_activity**
> LiveActivityStartResponse start_live_activity(live_activity_start_request)

Start a Live Activity

Starts a Live Activity on all registered devices and returns an activity_id.

### Example

* Bearer (API Key) Authentication (bearerAuth):

```python
import openapi_client
from openapi_client.models.live_activity_start_request import LiveActivityStartRequest
from openapi_client.models.live_activity_start_response import LiveActivityStartResponse
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://activitysmith.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://activitysmith.com/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (API Key): bearerAuth
configuration = openapi_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.LiveActivitiesApi(api_client)
    live_activity_start_request = {"content_state":{"title":"ActivitySmith API Deployment","subtitle":"start","number_of_steps":4,"current_step":1,"type":"segmented_progress","color":"yellow"}} # LiveActivityStartRequest | 

    try:
        # Start a Live Activity
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

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Live Activity started |  -  |
**429** | Rate limit exceeded |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_live_activity**
> LiveActivityUpdateResponse update_live_activity(live_activity_update_request)

Update a Live Activity

Updates an existing Live Activity. If the per-activity token is not registered yet, the update is queued.

### Example

* Bearer (API Key) Authentication (bearerAuth):

```python
import openapi_client
from openapi_client.models.live_activity_update_request import LiveActivityUpdateRequest
from openapi_client.models.live_activity_update_response import LiveActivityUpdateResponse
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://activitysmith.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://activitysmith.com/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (API Key): bearerAuth
configuration = openapi_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.LiveActivitiesApi(api_client)
    live_activity_update_request = {"activity_id":"pLAr-Hnq9ZFW4sxlk43Lhbuok4GLh7UW","content_state":{"title":"ActivitySmith API Deployment","subtitle":"npm i & pm2","current_step":3}} # LiveActivityUpdateRequest | 

    try:
        # Update a Live Activity
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

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Live Activity updated (or queued) |  -  |
**429** | Rate limit exceeded |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

