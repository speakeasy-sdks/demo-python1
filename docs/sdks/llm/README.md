# Llm
(*llm*)

### Available Operations

* [log_llm](#log_llm) - Evaluate and log a single prompt/response pair using langkit asynchronously.
* [evaluate](#evaluate) - Evaluate and log a single prompt/response pair using langkit.
* [list_metrics](#list_metrics) - Get a list of available metrics that can be referenced in policies.
* [validate_llm](#validate_llm) - Validate a single prompt/response pair

## log_llm

This is a convenience wrapper around the llm request type for calling /log, which accepts bulk data.

### Example Usage

```python
import dataservice
from dataservice.models import components

s = dataservice.Dataservice(
    api_key_header="<YOUR_API_KEY_HERE>",
)

req = components.LLMValidateRequest(
    dataset_id='<value>',
)

res = s.llm.log_llm(req)

if res.any is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                      | Type                                                                           | Required                                                                       | Description                                                                    |
| ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ |
| `request`                                                                      | [components.LLMValidateRequest](../../models/components/llmvalidaterequest.md) | :heavy_check_mark:                                                             | The request object to use for the request.                                     |


### Response

**[operations.LogLlmResponse](../../models/operations/logllmresponse.md)**
### Errors

| Error Object               | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| errors.HTTPValidationError | 422                        | application/json           |
| errors.SDKError            | 4x-5xx                     | */*                        |

## evaluate

Run langkit evaluation and return the validation results, as well as the generated metrics.

Args:
    log (bool, optional): Determines if logging to WhyLabs is enabled for the request. Defaults to True.

### Example Usage

```python
import dataservice
from dataservice.models import components, operations

s = dataservice.Dataservice(
    api_key_header="<YOUR_API_KEY_HERE>",
)

req = operations.EvaluateRequest(
    llm_validate_request=components.LLMValidateRequest(
        dataset_id='<value>',
    ),
)

res = s.llm.evaluate(req)

if res.evaluation_result is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                | Type                                                                     | Required                                                                 | Description                                                              |
| ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ |
| `request`                                                                | [operations.EvaluateRequest](../../models/operations/evaluaterequest.md) | :heavy_check_mark:                                                       | The request object to use for the request.                               |


### Response

**[operations.EvaluateResponse](../../models/operations/evaluateresponse.md)**
### Errors

| Error Object                  | Status Code                   | Content Type                  |
| ----------------------------- | ----------------------------- | ----------------------------- |
| errors.FailedEvaluationResult | 400                           | application/json              |
| errors.HTTPValidationError    | 422                           | application/json              |
| errors.SDKError               | 4x-5xx                        | */*                           |

## list_metrics

Get a list of available metrics that can be referenced in policies.

### Example Usage

```python
import dataservice

s = dataservice.Dataservice(
    api_key_header="<YOUR_API_KEY_HERE>",
)


res = s.llm.list_metrics()

if res.available_metrics is not None:
    # handle response
    pass

```


### Response

**[operations.ListMetricsResponse](../../models/operations/listmetricsresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## validate_llm

This endpoint can be used to synchronously get validation results from a single input
prompt/response. It automatically performs whylogs profiling and sends profiles to
whylabs in the background, just like  the /log endpoint.

Args:
    log (bool, optional): Determines if logging to WhyLabs is enabled for the validate request. Defaults to True.

### Example Usage

```python
import dataservice
from dataservice.models import components, operations

s = dataservice.Dataservice(
    api_key_header="<YOUR_API_KEY_HERE>",
)

req = operations.ValidateLlmRequest(
    llm_validate_request=components.LLMValidateRequest(
        dataset_id='<value>',
    ),
)

res = s.llm.validate_llm(req)

if res.validation_result is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                      | Type                                                                           | Required                                                                       | Description                                                                    |
| ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ |
| `request`                                                                      | [operations.ValidateLlmRequest](../../models/operations/validatellmrequest.md) | :heavy_check_mark:                                                             | The request object to use for the request.                                     |


### Response

**[operations.ValidateLlmResponse](../../models/operations/validatellmresponse.md)**
### Errors

| Error Object               | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| errors.ValidationResult    | 400                        | application/json           |
| errors.HTTPValidationError | 422                        | application/json           |
| errors.SDKError            | 4x-5xx                     | */*                        |
