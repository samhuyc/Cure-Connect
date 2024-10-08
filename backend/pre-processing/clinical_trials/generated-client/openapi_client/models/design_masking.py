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


class DesignMasking(str, Enum):
    """
    DesignMasking
    """

    """
    allowed enum values
    """
    NONE = 'NONE'
    SINGLE = 'SINGLE'
    DOUBLE = 'DOUBLE'
    TRIPLE = 'TRIPLE'
    QUADRUPLE = 'QUADRUPLE'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of DesignMasking from a JSON string"""
        return cls(json.loads(json_str))


