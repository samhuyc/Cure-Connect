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


class MeasureDispersionType(str, Enum):
    """
    MeasureDispersionType
    """

    """
    allowed enum values
    """
    NA = 'NA'
    STANDARD_DEVIATION = 'STANDARD_DEVIATION'
    STANDARD_ERROR = 'STANDARD_ERROR'
    INTER_QUARTILE_RANGE = 'INTER_QUARTILE_RANGE'
    FULL_RANGE = 'FULL_RANGE'
    CONFIDENCE_80 = 'CONFIDENCE_80'
    CONFIDENCE_90 = 'CONFIDENCE_90'
    CONFIDENCE_95 = 'CONFIDENCE_95'
    CONFIDENCE_975 = 'CONFIDENCE_975'
    CONFIDENCE_99 = 'CONFIDENCE_99'
    CONFIDENCE_OTHER = 'CONFIDENCE_OTHER'
    GEOMETRIC_COEFFICIENT = 'GEOMETRIC_COEFFICIENT'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of MeasureDispersionType from a JSON string"""
        return cls(json.loads(json_str))


