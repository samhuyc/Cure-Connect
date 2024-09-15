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
from openapi_client.models.measure_class import MeasureClass
from openapi_client.models.measure_dispersion_type import MeasureDispersionType
from openapi_client.models.measure_param import MeasureParam
from typing import Optional, Set
from typing_extensions import Self

class BaselineMeasure(BaseModel):
    """
    BaselineMeasure
    """ # noqa: E501
    title: Optional[StrictStr] = None
    description: Optional[StrictStr] = None
    population_description: Optional[StrictStr] = Field(default=None, alias="populationDescription")
    param_type: Optional[MeasureParam] = Field(default=None, alias="paramType")
    dispersion_type: Optional[MeasureDispersionType] = Field(default=None, alias="dispersionType")
    unit_of_measure: Optional[StrictStr] = Field(default=None, alias="unitOfMeasure")
    calculate_pct: Optional[StrictBool] = Field(default=None, alias="calculatePct")
    denom_units_selected: Optional[StrictStr] = Field(default=None, alias="denomUnitsSelected")
    denoms: Optional[List[Denom]] = None
    classes: Optional[List[MeasureClass]] = None
    __properties: ClassVar[List[str]] = ["title", "description", "populationDescription", "paramType", "dispersionType", "unitOfMeasure", "calculatePct", "denomUnitsSelected", "denoms", "classes"]

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
        """Create an instance of BaselineMeasure from a JSON string"""
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
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of BaselineMeasure from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "title": obj.get("title"),
            "description": obj.get("description"),
            "populationDescription": obj.get("populationDescription"),
            "paramType": obj.get("paramType"),
            "dispersionType": obj.get("dispersionType"),
            "unitOfMeasure": obj.get("unitOfMeasure"),
            "calculatePct": obj.get("calculatePct"),
            "denomUnitsSelected": obj.get("denomUnitsSelected"),
            "denoms": [Denom.from_dict(_item) for _item in obj["denoms"]] if obj.get("denoms") is not None else None,
            "classes": [MeasureClass.from_dict(_item) for _item in obj["classes"]] if obj.get("classes") is not None else None
        })
        return _obj


