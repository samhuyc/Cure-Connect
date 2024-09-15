# coding: utf-8

"""
    ClinicalTrials.gov REST API

    This API is made available to provide users meta data, statistics, and the most recent version of the clinical trials available on ClinicalTrials.gov.

    The version of the OpenAPI document: 2.0.3
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import json
from enum import Enum
from typing_extensions import Self


class NonInferiorityType(str, Enum):
    """
    NonInferiorityType
    """

    """
    allowed enum values
    """
    SUPERIORITY = 'SUPERIORITY'
    NON_INFERIORITY = 'NON_INFERIORITY'
    EQUIVALENCE = 'EQUIVALENCE'
    OTHER = 'OTHER'
    NON_INFERIORITY_OR_EQUIVALENCE = 'NON_INFERIORITY_OR_EQUIVALENCE'
    SUPERIORITY_OR_OTHER = 'SUPERIORITY_OR_OTHER'
    NON_INFERIORITY_OR_EQUIVALENCE_LEGACY = 'NON_INFERIORITY_OR_EQUIVALENCE_LEGACY'
    SUPERIORITY_OR_OTHER_LEGACY = 'SUPERIORITY_OR_OTHER_LEGACY'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of NonInferiorityType from a JSON string"""
        return cls(json.loads(json_str))


