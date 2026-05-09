# activitysmith_openapi.MetricsApi

All URIs are relative to *https://activitysmith.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**update_metric_value**](MetricsApi.md#update_metric_value) | **POST** /metrics/{key}/value | Update a widget metric value


# **update_metric_value**
> MetricValueUpdateResponse update_metric_value(key, metric_value_update_request)

Update a widget metric value

Updates the latest value for a metric displayed in ActivitySmith widgets. Create the metric in the web app first, then update its value using the key.

### Example

* Bearer (API Key) Authentication (apiKeyAuth):

```python
import activitysmith_openapi
from activitysmith_openapi.models.metric_value_update_request import MetricValueUpdateRequest
from activitysmith_openapi.models.metric_value_update_response import MetricValueUpdateResponse
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
    api_instance = activitysmith_openapi.MetricsApi(api_client)
    key = 'key_example' # str | Metric key configured in the web app. Lowercase letters, numbers, dots, underscores, and dashes are allowed.
    metric_value_update_request = {"value":42} # MetricValueUpdateRequest | 

    try:
        # Update a widget metric value
        api_response = api_instance.update_metric_value(key, metric_value_update_request)
        print("The response of MetricsApi->update_metric_value:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MetricsApi->update_metric_value: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key** | **str**| Metric key configured in the web app. Lowercase letters, numbers, dots, underscores, and dashes are allowed. | 
 **metric_value_update_request** | [**MetricValueUpdateRequest**](MetricValueUpdateRequest.md)|  | 

### Return type

[**MetricValueUpdateResponse**](MetricValueUpdateResponse.md)

### Authorization

[apiKeyAuth](../README.md#apiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Metric value updated |  -  |
**400** | Bad request (invalid key or value) |  -  |
**404** | Metric not found |  -  |
**429** | Rate limit exceeded |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

