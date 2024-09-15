# coding: utf-8

"""
    ClinicalTrials.gov REST API

    This API is made available to provide users meta data, statistics, and the most recent version of the clinical trials available on ClinicalTrials.gov.

    The version of the OpenAPI document: 2.0.3
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from openapi_client.models.denom import Denom
from openapi_client.models.measure_analysis import MeasureAnalysis
from openapi_client.models.measure_class import MeasureClass
from openapi_client.models.measure_group import MeasureGroup
from openapi_client.models.measure_param import MeasureParam
from openapi_client.models.outcome_measure_type import OutcomeMeasureType
from openapi_client.models.reporting_status import ReportingStatus
from typing import Optional, Set
from typing_extensions import Self

class OutcomeMeasure(BaseModel):
    """
    OutcomeMeasure
    """ # noqa: E501
    type: Optional[OutcomeMeasureType] = None
    title: Optional[StrictStr] = None
    description: Optional[StrictStr] = None
    population_description: Optional[StrictStr] = Field(default=None, alias="populationDescription")
    reporting_status: Optional[ReportingStatus] = Field(default=None, alias="reportingStatus")
    anticipated_posting_date: Optional[StrictStr] = Field(default=None, description="Date in `yyyy`, `yyyy-MM`, or `yyyy-MM-dd` format", alias="anticipatedPostingDate")
    param_type: Optional[MeasureParam] = Field(default=None, alias="paramType")
    dispersion_type: Optional[StrictStr] = Field(default=None, alias="dispersionType")
    unit_of_measure: Optional[StrictStr] = Field(default=None, alias="unitOfMeasure")
    calculate_pct: Optional[StrictBool] = Field(default=None, alias="calculatePct")
    time_frame: Optional[StrictStr] = Field(default=None, alias="timeFrame")
    type_units_analyzed: Optional[StrictStr] = Field(default=None, alias="typeUnitsAnalyzed")
    denom_units_selected: Optional[StrictStr] = Field(default=None, alias="denomUnitsSelected")
    groups: Optional[List[MeasureGroup]] = None
    denoms: Optional[List[Denom]] = None
    classes: Optional[List[MeasureClass]] = None
    analyses: Optional[List[MeasureAnalysis]] = None
    __properties: ClassVar[List[str]] = ["type", "title", "description", "populationDescription", "reportingStatus", "anticipatedPostingDate", "paramType", "dispersionType", "unitOfMeasure", "calculatePct", "timeFrame", "typeUnitsAnalyzed", "denomUnitsSelected", "groups", "denoms", "classes", "analyses"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of OutcomeMeasure from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of each item in groups (list)
        _items = []
        if self.groups:
            for _item_groups in self.groups:
                if _item_groups:
                    _items.append(_item_groups.to_dict())
            _dict['groups'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in denoms (list)
        _items = []
        if self.denoms:
            for _item_denoms in self.denoms:
                if _item_denoms:
                    _items.append(_item_denoms.to_dict())
            _dict['denoms'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in classes (list)
        _items = []
        if self.classes:
            for _item_classes in self.classes:
                if _item_classes:
                    _items.append(_item_classes.to_dict())
            _dict['classes'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in analyses (list)
        _items = []
        if self.analyses:
            for _item_analyses in self.analyses:
                if _item_analyses:
                    _items.append(_item_analyses.to_dict())
            _dict['analyses'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of OutcomeMeasure from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "type": obj.get("type"),
            "title": obj.get("title"),
            "description": obj.get("description"),
            "populationDescription": obj.get("populationDescription"),
            "reportingStatus": obj.get("reportingStatus"),
            "anticipatedPostingDate": obj.get("anticipatedPostingDate"),
            "paramType": obj.get("paramType"),
            "dispersionType": obj.get("dispersionType"),
            "unitOfMeasure": obj.get("unitOfMeasure"),
            "calculatePct": obj.get("calculatePct"),
            "timeFrame": obj.get("timeFrame"),
            "typeUnitsAnalyzed": obj.get("typeUnitsAnalyzed"),
            "denomUnitsSelected": obj.get("denomUnitsSelected"),
            "groups": [MeasureGroup.from_dict(_item) for _item in obj["groups"]] if obj.get("groups") is not None else None,
            "denoms": [Denom.from_dict(_item) for _item in obj["denoms"]] if obj.get("denoms") is not None else None,
            "classes": [MeasureClass.from_dict(_item) for _item in obj["classes"]] if obj.get("classes") is not None else None,
            "analyses": [MeasureAnalysis.from_dict(_item) for _item in obj["analyses"]] if obj.get("analyses") is not None else None
        })
        return _obj


