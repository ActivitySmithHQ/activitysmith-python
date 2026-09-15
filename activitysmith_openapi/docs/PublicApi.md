# activitysmith_openapi.PublicApi

All URIs are relative to *https://activitysmith.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_api_health**](PublicApi.md#get_api_health) | **GET** /health | Get API Health
[**list_public_changelog_entries**](PublicApi.md#list_public_changelog_entries) | **GET** /changelog | List Public Changelog Entries


# **get_api_health**
> HealthResponse get_api_health()

Get API Health

Returns the current availability of the ActivitySmith API and its required services. No authentication is required.

### Example


```python
import activitysmith_openapi
from activitysmith_openapi.models.health_response import HealthResponse
from activitysmith_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://activitysmith.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = activitysmith_openapi.Configuration(
    host = "https://activitysmith.com/api"
)


# Enter a context with an instance of the API client
with activitysmith_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = activitysmith_openapi.PublicApi(api_client)

    try:
        # Get API Health
        api_response = api_instance.get_api_health()
        print("The response of PublicApi->get_api_health:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PublicApi->get_api_health: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**HealthResponse**](HealthResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The API and its required services are available. |  -  |
**503** | One or more required services are unavailable. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_public_changelog_entries**
> ChangelogListResponse list_public_changelog_entries(platform=platform, limit=limit)

List Public Changelog Entries

Returns published ActivitySmith app changelog entries. No authentication is required.

### Example


```python
import activitysmith_openapi
from activitysmith_openapi.models.changelog_list_response import ChangelogListResponse
from activitysmith_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://activitysmith.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = activitysmith_openapi.Configuration(
    host = "https://activitysmith.com/api"
)


# Enter a context with an instance of the API client
with activitysmith_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = activitysmith_openapi.PublicApi(api_client)
    platform = 'ios' # str | Platform whose published changelog entries should be returned. (optional) (default to 'ios')
    limit = 10 # int | Maximum number of entries to return. (optional) (default to 10)

    try:
        # List Public Changelog Entries
        api_response = api_instance.list_public_changelog_entries(platform=platform, limit=limit)
        print("The response of PublicApi->list_public_changelog_entries:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PublicApi->list_public_changelog_entries: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **platform** | **str**| Platform whose published changelog entries should be returned. | [optional] [default to &#39;ios&#39;]
 **limit** | **int**| Maximum number of entries to return. | [optional] [default to 10]

### Return type

[**ChangelogListResponse**](ChangelogListResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Published changelog entries ordered from newest to oldest. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

