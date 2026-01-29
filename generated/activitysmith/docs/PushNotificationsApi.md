# activitysmith.PushNotificationsApi

All URIs are relative to *https://activitysmith.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**send_push_notification**](PushNotificationsApi.md#send_push_notification) | **POST** /push-notification | Send a push notification


# **send_push_notification**
> PushNotificationResponse send_push_notification(push_notification_request)

Send a push notification

Sends a push notification to every paired device in your account.

### Example

* Bearer (API Key) Authentication (apiKeyAuth):

```python
import activitysmith
from activitysmith.models.push_notification_request import PushNotificationRequest
from activitysmith.models.push_notification_response import PushNotificationResponse
from activitysmith.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://activitysmith.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = activitysmith.Configuration(
    host = "https://activitysmith.com/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (API Key): apiKeyAuth
configuration = activitysmith.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with activitysmith.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = activitysmith.PushNotificationsApi(api_client)
    push_notification_request = {"title":"Build Failed 🚨","message":"CI pipeline failed on main branch"} # PushNotificationRequest | 

    try:
        # Send a push notification
        api_response = api_instance.send_push_notification(push_notification_request)
        print("The response of PushNotificationsApi->send_push_notification:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PushNotificationsApi->send_push_notification: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **push_notification_request** | [**PushNotificationRequest**](PushNotificationRequest.md)|  | 

### Return type

[**PushNotificationResponse**](PushNotificationResponse.md)

### Authorization

[apiKeyAuth](../README.md#apiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Push notification sent |  -  |
**429** | Rate limit exceeded |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

