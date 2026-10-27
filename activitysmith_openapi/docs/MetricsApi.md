# activitysmith_openapi.MetricsApi

All URIs are relative to *https://activitysmith.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**update_metric_value**](MetricsApi.md#update_metric_value) | **POST** /metrics/{key}/value | Update a widget metric value
[**upsert_metric**](MetricsApi.md#upsert_metric) | **PUT** /metrics/{key} | Create or update a widget metric


# **update_metric_value**
> MetricValueUpdateResponse update_metric_value(key, metric_value_update_request)

Update a widget metric value

Updates the latest value for a metric displayed in ActivitySmith widgets. If no metric uses the key yet, the first value creates one: the label comes from the key, numeric values get the number format, and text values get the string format. To choose a currency, percent, or unit format, create the metric first with PUT /metrics/{key} or in the web app. A deleted metric is not recreated by new values; the request returns 404 with code metric_deleted. Each account can have up to 100 metrics created through the API. Metric updates have an independent 300-requests-per-minute account allowance. They do not consume the Push Notification, badge, or Live Activity allowances.

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
    key = 'key_example' # str | Metric key. A key that has never been used creates the metric. Lowercase letters, numbers, dots, underscores, and dashes are allowed.
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
 **key** | **str**| Metric key. A key that has never been used creates the metric. Lowercase letters, numbers, dots, underscores, and dashes are allowed. | 
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
**200** | Metric value updated |  * RateLimit - Current request quotas using IETF draft-8 structured fields. Each named policy includes r (remaining requests) and t (seconds until reset). Multiple policies may apply. <br>  * RateLimit-Policy - Each named policy includes q (request quota) and w (window in seconds). Listing devices has an IP limit of 600 requests and an account limit of 60 requests per 60 seconds. <br>  |
**400** | Bad request (invalid key or value) |  * RateLimit - Current request quotas using IETF draft-8 structured fields. Each named policy includes r (remaining requests) and t (seconds until reset). Multiple policies may apply. <br>  * RateLimit-Policy - Each named policy includes q (request quota) and w (window in seconds). Listing devices has an IP limit of 600 requests and an account limit of 60 requests per 60 seconds. <br>  |
**404** | Metric deleted or not found |  * RateLimit - Current request quotas using IETF draft-8 structured fields. Each named policy includes r (remaining requests) and t (seconds until reset). Multiple policies may apply. <br>  * RateLimit-Policy - Each named policy includes q (request quota) and w (window in seconds). Listing devices has an IP limit of 600 requests and an account limit of 60 requests per 60 seconds. <br>  |
**409** | Metric limit reached |  * RateLimit - Current request quotas using IETF draft-8 structured fields. Each named policy includes r (remaining requests) and t (seconds until reset). Multiple policies may apply. <br>  * RateLimit-Policy - Each named policy includes q (request quota) and w (window in seconds). Listing devices has an IP limit of 600 requests and an account limit of 60 requests per 60 seconds. <br>  |
**429** | Rate limit exceeded |  * RateLimit - Current request quotas using IETF draft-8 structured fields. Each named policy includes r (remaining requests) and t (seconds until reset). Multiple policies may apply. <br>  * RateLimit-Policy - Each named policy includes q (request quota) and w (window in seconds). Listing devices has an IP limit of 600 requests and an account limit of 60 requests per 60 seconds. <br>  * Retry-After - Seconds to wait before retrying after a request-rate 429. Live Activity capacity errors are separate and require freeing device capacity; they do not provide a timed retry guarantee. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upsert_metric**
> MetricResponse upsert_metric(key, metric_upsert_request=metric_upsert_request)

Create or update a widget metric

Creates a metric for widgets, or updates the fields sent for an existing metric. Omitted fields keep their current values, so repeating the same request does not change the metric. Changing between the string format and a numeric format clears the latest value. Shares the metric account allowance of 300 requests per minute and is not a billable metric update.

### Example

* Bearer (API Key) Authentication (apiKeyAuth):

```python
import activitysmith_openapi
from activitysmith_openapi.models.metric_response import MetricResponse
from activitysmith_openapi.models.metric_upsert_request import MetricUpsertRequest
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
    key = 'key_example' # str | Metric key. Lowercase letters, numbers, dots, underscores, and dashes are allowed.
    metric_upsert_request = {"label":"MRR","format":"currency","currency_code":"USD"} # MetricUpsertRequest |  (optional)

    try:
        # Create or update a widget metric
        api_response = api_instance.upsert_metric(key, metric_upsert_request=metric_upsert_request)
        print("The response of MetricsApi->upsert_metric:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MetricsApi->upsert_metric: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key** | **str**| Metric key. Lowercase letters, numbers, dots, underscores, and dashes are allowed. | 
 **metric_upsert_request** | [**MetricUpsertRequest**](MetricUpsertRequest.md)|  | [optional] 

### Return type

[**MetricResponse**](MetricResponse.md)

### Authorization

[apiKeyAuth](../README.md#apiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Metric updated |  * RateLimit - Current request quotas using IETF draft-8 structured fields. Each named policy includes r (remaining requests) and t (seconds until reset). Multiple policies may apply. <br>  * RateLimit-Policy - Each named policy includes q (request quota) and w (window in seconds). Listing devices has an IP limit of 600 requests and an account limit of 60 requests per 60 seconds. <br>  |
**201** | Metric created |  * RateLimit - Current request quotas using IETF draft-8 structured fields. Each named policy includes r (remaining requests) and t (seconds until reset). Multiple policies may apply. <br>  * RateLimit-Policy - Each named policy includes q (request quota) and w (window in seconds). Listing devices has an IP limit of 600 requests and an account limit of 60 requests per 60 seconds. <br>  |
**400** | Bad request (invalid key or definition) |  * RateLimit - Current request quotas using IETF draft-8 structured fields. Each named policy includes r (remaining requests) and t (seconds until reset). Multiple policies may apply. <br>  * RateLimit-Policy - Each named policy includes q (request quota) and w (window in seconds). Listing devices has an IP limit of 600 requests and an account limit of 60 requests per 60 seconds. <br>  |
**409** | Metric limit reached |  * RateLimit - Current request quotas using IETF draft-8 structured fields. Each named policy includes r (remaining requests) and t (seconds until reset). Multiple policies may apply. <br>  * RateLimit-Policy - Each named policy includes q (request quota) and w (window in seconds). Listing devices has an IP limit of 600 requests and an account limit of 60 requests per 60 seconds. <br>  |
**429** | Rate limit exceeded |  * RateLimit - Current request quotas using IETF draft-8 structured fields. Each named policy includes r (remaining requests) and t (seconds until reset). Multiple policies may apply. <br>  * RateLimit-Policy - Each named policy includes q (request quota) and w (window in seconds). Listing devices has an IP limit of 600 requests and an account limit of 60 requests per 60 seconds. <br>  * Retry-After - Seconds to wait before retrying after a request-rate 429. Live Activity capacity errors are separate and require freeing device capacity; they do not provide a timed retry guarantee. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

