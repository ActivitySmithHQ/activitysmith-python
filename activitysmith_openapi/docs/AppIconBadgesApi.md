# activitysmith_openapi.AppIconBadgesApi

All URIs are relative to *https://activitysmith.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**update_app_icon_badge_count**](AppIconBadgesApi.md#update_app_icon_badge_count) | **POST** /badge | Update App Icon Badge Count


# **update_app_icon_badge_count**
> AppIconBadgeCountUpdateResponse update_app_icon_badge_count(app_icon_badge_count_update_request)

Update App Icon Badge Count

Updates the App Icon Badge Count on devices matched by API key scope and optional target channels. Send `badge: 0` to clear the count. Badge updates are independent of push notifications and do not create a push notification history item.

### Example

* Bearer (API Key) Authentication (apiKeyAuth):

```python
import activitysmith_openapi
from activitysmith_openapi.models.app_icon_badge_count_update_request import AppIconBadgeCountUpdateRequest
from activitysmith_openapi.models.app_icon_badge_count_update_response import AppIconBadgeCountUpdateResponse
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
    api_instance = activitysmith_openapi.AppIconBadgesApi(api_client)
    app_icon_badge_count_update_request = {"badge":12} # AppIconBadgeCountUpdateRequest | 

    try:
        # Update App Icon Badge Count
        api_response = api_instance.update_app_icon_badge_count(app_icon_badge_count_update_request)
        print("The response of AppIconBadgesApi->update_app_icon_badge_count:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AppIconBadgesApi->update_app_icon_badge_count: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_icon_badge_count_update_request** | [**AppIconBadgeCountUpdateRequest**](AppIconBadgeCountUpdateRequest.md)|  | 

### Return type

[**AppIconBadgeCountUpdateResponse**](AppIconBadgeCountUpdateResponse.md)

### Authorization

[apiKeyAuth](../README.md#apiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | App Icon Badge Count updated |  -  |
**400** | Bad request (invalid badge value or channel targeting input) |  -  |
**403** | Forbidden (API key scope or channel assignment violation) |  -  |
**404** | No recipients found for effective channel target |  -  |
**429** | Rate limit exceeded |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

