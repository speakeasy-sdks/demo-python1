"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ...models.components import evaluationresult as components_evaluationresult
from ...models.components import llmvalidaterequest as components_llmvalidaterequest
from typing import Optional


@dataclasses.dataclass
class EvaluateRequest:
    llm_validate_request: components_llmvalidaterequest.LLMValidateRequest = dataclasses.field(metadata={'request': { 'media_type': 'application/json' }})
    log: Optional[bool] = dataclasses.field(default=True, metadata={'query_param': { 'field_name': 'log', 'style': 'form', 'explode': True }})
    perf_info: Optional[bool] = dataclasses.field(default=False, metadata={'query_param': { 'field_name': 'perf_info', 'style': 'form', 'explode': True }})
    



@dataclasses.dataclass
class EvaluateResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    raw_response: requests_http.Response = dataclasses.field()
    r"""Raw HTTP response; suitable for custom response parsing"""
    evaluation_result: Optional[components_evaluationresult.EvaluationResult] = dataclasses.field(default=None)
    r"""Successful Response"""
    

