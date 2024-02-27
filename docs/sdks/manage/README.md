# Manage
(*manage*)

### Available Operations

* [publish](#publish) - Publish Profiles
* [health](#health) - Health
* [status](#status) - Status
* [debug_info](#debug_info) - Log Debug Info

## publish

Publish Profiles

### Example Usage

```python
import dataservice

s = dataservice.Dataservice(
    api_key_header="<YOUR_API_KEY_HERE>",
)


res = s.manage.publish()

if res.any is not None:
    # handle response
    pass
```


### Response

**[operations.PublishResponse](../../models/operations/publishresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## health

Health

### Example Usage

```python
import dataservice

s = dataservice.Dataservice(
    api_key_header="<YOUR_API_KEY_HERE>",
)


res = s.manage.health()

if res.any is not None:
    # handle response
    pass
```


### Response

**[operations.HealthResponse](../../models/operations/healthresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## status

Status

### Example Usage

```python
import dataservice

s = dataservice.Dataservice(
    api_key_header="<YOUR_API_KEY_HERE>",
)


res = s.manage.status()

if res.process_logger_status_response is not None:
    # handle response
    pass
```


### Response

**[operations.StatusResponse](../../models/operations/statusresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## debug_info

Log the output of /status

### Example Usage

```python
import dataservice

s = dataservice.Dataservice(
    api_key_header="<YOUR_API_KEY_HERE>",
)


res = s.manage.debug_info()

if res.any is not None:
    # handle response
    pass
```


### Response

**[operations.DebugInfoResponse](../../models/operations/debuginforesponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |
