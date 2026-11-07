# activitysmith_openapi.DevicesApi

All URIs are relative to *https://activitysmith.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list_account_devices**](DevicesApi.md#list_account_devices) | **GET** /account/devices | List paired devices


# **list_account_devices**
> AccountDeviceListResponse list_account_devices(limit=limit, offset=offset, include_inactive=include_inactive)

List paired devices

Lists the iPhones and iPads paired to the account, active devices first. Use it to check that a device is paired before you send, or to find device IDs for Channels. An empty list means no device is paired yet: install the ActivitySmith app from the App Store and sign in. Channel-scoped API keys cannot list devices.

### Example

* Bearer (API Key) Authentication (apiKeyAuth):

```python
import activitysmith_openapi
from activitysmith_openapi.models.account_device_list_response import AccountDeviceListResponse
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
    api_instance = activitysmith_openapi.DevicesApi(api_client)
    limit = 100 # int | Maximum devices to return, 1 to 100. Defaults to 100. (optional) (default to 100)
    offset = 0 # int | Devices to skip. Use meta.next_offset from the previous page. (optional) (default to 0)
    include_inactive = False # bool | Include devices that can no longer receive deliveries, such as unpaired phones. (optional) (default to False)

    try:
        # List paired devices
        api_response = api_instance.list_account_devices(limit=limit, offset=offset, include_inactive=include_inactive)
        print("The response of DevicesApi->list_account_devices:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DevicesApi->list_account_devices: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Maximum devices to return, 1 to 100. Defaults to 100. | [optional] [default to 100]
 **offset** | **int**| Devices to skip. Use meta.next_offset from the previous page. | [optional] [default to 0]
 **include_inactive** | **bool**| Include devices that can no longer receive deliveries, such as unpaired phones. | [optional] [default to False]

### Return type

[**AccountDeviceListResponse**](AccountDeviceListResponse.md)

### Authorization

[apiKeyAuth](../README.md#apiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Paired devices |  * RateLimit - Current request quotas using IETF draft-8 structured fields. Each named policy includes r (remaining requests) and t (seconds until reset). Multiple policies may apply. <br>  * RateLimit-Policy - Each named policy includes q (request quota) and w (window in seconds). Listing devices has an IP limit of 600 requests and an account limit of 60 requests per 60 seconds. <br>  |
**403** | The API key is limited to Channels |  -  |
**429** | Rate limit exceeded |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

