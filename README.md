# Dataservice

<div align="left">
    <a href="https://speakeasyapi.dev/"><img src="https://custom-icon-badges.demolab.com/badge/-Built%20By%20Speakeasy-212015?style=for-the-badge&logoColor=FBE331&logo=speakeasy&labelColor=545454" /></a>
    <a href="https://opensource.org/licenses/MIT">
        <img src="https://img.shields.io/badge/License-MIT-blue.svg" style="width: 100px; height: 28px;" />
    </a>
</div>


## 🏗 **Welcome to your new SDK!** 🏗

It has been generated successfully based on your OpenAPI spec. However, it is not yet ready for production use. Here are some next steps:
- [ ] 🛠 Make your SDK feel handcrafted by [customizing it](https://www.speakeasyapi.dev/docs/customize-sdks)
- [ ] ♻️ Refine your SDK quickly by iterating locally with the [Speakeasy CLI](https://github.com/speakeasy-api/speakeasy)
- [ ] 🎁 Publish your SDK to package managers by [configuring automatic publishing](https://www.speakeasyapi.dev/docs/productionize-sdks/publish-sdks)
- [ ] ✨ When ready to productionize, delete this section from the README

<!-- Start SDK Installation [installation] -->
## SDK Installation

```bash
pip install git+https://github.com/speakeasy-sdks/demo-python1.git
```
<!-- End SDK Installation [installation] -->

<!-- Start SDK Example Usage [usage] -->
## SDK Example Usage

### Example

```python
import dataservice
from dataservice.models import components

s = dataservice.Dataservice(
    api_key_header="<YOUR_API_KEY_HERE>",
)

req = components.LogRequest(
    dataset_id='<value>',
    multiple=components.LogMultiple(
        columns=[
            '<value>',
        ],
        data=[
            [
                [
                    2469.2,
                ],
            ],
        ],
    ),
)

res = s.profile.log(req)

if res.any is not None:
    # handle response
    pass

```
<!-- End SDK Example Usage [usage] -->

<!-- Start Available Resources and Operations [operations] -->
## Available Resources and Operations

### [profile](docs/sdks/profile/README.md)

* [log](docs/sdks/profile/README.md#log) - Profile tabular data
* [log_embeddings](docs/sdks/profile/README.md#log_embeddings) - Profile embeddings
* [log_pubsub](docs/sdks/profile/README.md#log_pubsub) - Log Pubsub
* [log_pubsub_embedding](docs/sdks/profile/README.md#log_pubsub_embedding) - Log Pubsub Embeddings

### [llm](docs/sdks/llm/README.md)

* [log_llm](docs/sdks/llm/README.md#log_llm) - Evaluate and log a single prompt/response pair using langkit asynchronously.
* [evaluate](docs/sdks/llm/README.md#evaluate) - Evaluate and log a single prompt/response pair using langkit.
* [list_metrics](docs/sdks/llm/README.md#list_metrics) - Get a list of available metrics that can be referenced in policies.
* [validate_llm](docs/sdks/llm/README.md#validate_llm) - Validate a single prompt/response pair

### [manage](docs/sdks/manage/README.md)

* [publish](docs/sdks/manage/README.md#publish) - Publish Profiles
* [health](docs/sdks/manage/README.md#health) - Health
* [status](docs/sdks/manage/README.md#status) - Status
* [debug_info](docs/sdks/manage/README.md#debug_info) - Log Debug Info
<!-- End Available Resources and Operations [operations] -->

<!-- Start Error Handling [errors] -->
## Error Handling

Handling errors in this SDK should largely match your expectations.  All operations return a response object or raise an error.  If Error objects are specified in your OpenAPI Spec, the SDK will raise the appropriate Error type.

| Error Object               | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| errors.HTTPValidationError | 422                        | application/json           |
| errors.SDKError            | 4x-5xx                     | */*                        |

### Example

```python
import dataservice
from dataservice.models import components, errors

s = dataservice.Dataservice(
    api_key_header="<YOUR_API_KEY_HERE>",
)

req = components.LogRequest(
    dataset_id='<value>',
    multiple=components.LogMultiple(
        columns=[
            '<value>',
        ],
        data=[
            [
                [
                    2469.2,
                ],
            ],
        ],
    ),
)

res = None
try:
    res = s.profile.log(req)
except errors.HTTPValidationError as e:
    # handle exception
    raise(e)
except errors.SDKError as e:
    # handle exception
    raise(e)

if res.any is not None:
    # handle response
    pass

```
<!-- End Error Handling [errors] -->

<!-- Start Server Selection [server] -->
## Server Selection

### Select Server by Index

You can override the default server globally by passing a server index to the `server_idx: int` optional parameter when initializing the SDK client instance. The selected server will then be used as the default on the operations that use it. This table lists the indexes associated with the available servers:

| # | Server | Variables |
| - | ------ | --------- |
| 0 | `http://localhost:8080` | None |

#### Example

```python
import dataservice
from dataservice.models import components

s = dataservice.Dataservice(
    server_idx=0,
    api_key_header="<YOUR_API_KEY_HERE>",
)

req = components.LogRequest(
    dataset_id='<value>',
    multiple=components.LogMultiple(
        columns=[
            '<value>',
        ],
        data=[
            [
                [
                    2469.2,
                ],
            ],
        ],
    ),
)

res = s.profile.log(req)

if res.any is not None:
    # handle response
    pass

```


### Override Server URL Per-Client

The default server can also be overridden globally by passing a URL to the `server_url: str` optional parameter when initializing the SDK client instance. For example:
```python
import dataservice
from dataservice.models import components

s = dataservice.Dataservice(
    server_url="http://localhost:8080",
    api_key_header="<YOUR_API_KEY_HERE>",
)

req = components.LogRequest(
    dataset_id='<value>',
    multiple=components.LogMultiple(
        columns=[
            '<value>',
        ],
        data=[
            [
                [
                    2469.2,
                ],
            ],
        ],
    ),
)

res = s.profile.log(req)

if res.any is not None:
    # handle response
    pass

```
<!-- End Server Selection [server] -->

<!-- Start Custom HTTP Client [http-client] -->
## Custom HTTP Client

The Python SDK makes API calls using the [requests](https://pypi.org/project/requests/) HTTP library.  In order to provide a convenient way to configure timeouts, cookies, proxies, custom headers, and other low-level configuration, you can initialize the SDK client with a custom `requests.Session` object.

For example, you could specify a header for every request that this sdk makes as follows:
```python
import dataservice
import requests

http_client = requests.Session()
http_client.headers.update({'x-custom-header': 'someValue'})
s = dataservice.Dataservice(client: http_client)
```
<!-- End Custom HTTP Client [http-client] -->

<!-- Start Authentication [security] -->
## Authentication

### Per-Client Security Schemes

This SDK supports the following security scheme globally:

| Name             | Type             | Scheme           |
| ---------------- | ---------------- | ---------------- |
| `api_key_header` | apiKey           | API key          |

To authenticate with the API the `api_key_header` parameter must be set when initializing the SDK client instance. For example:
```python
import dataservice
from dataservice.models import components

s = dataservice.Dataservice(
    api_key_header="<YOUR_API_KEY_HERE>",
)

req = components.LogRequest(
    dataset_id='<value>',
    multiple=components.LogMultiple(
        columns=[
            '<value>',
        ],
        data=[
            [
                [
                    2469.2,
                ],
            ],
        ],
    ),
)

res = s.profile.log(req)

if res.any is not None:
    # handle response
    pass

```
<!-- End Authentication [security] -->

<!-- Placeholder for Future Speakeasy SDK Sections -->

# Development

## Maturity

This SDK is in beta, and there may be breaking changes between versions without a major version update. Therefore, we recommend pinning usage
to a specific package version. This way, you can install the same version each time without breaking changes unless you are intentionally
looking for the latest version.

## Contributions

While we value open-source contributions to this SDK, this library is generated programmatically.
Feel free to open a PR or a Github issue as a proof of concept and we'll do our best to include it in a future release!

### SDK Created by [Speakeasy](https://docs.speakeasyapi.dev/docs/using-speakeasy/client-sdks)
