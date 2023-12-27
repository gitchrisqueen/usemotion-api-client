# coding: utf-8

"""
    Motion REST API

    <!-- theme: warning -->  > ### Rate Limit Information > > The Motion API is currently rate limited to 12 requests per minute per user. In the event a user exceeds this rate limit 3 times > in a singe 24 hour period, their API access will be disabled and will require that they contact support to have it re-enabled.  <!-- theme: info -->  > ### Note on Date Formats > > All dates that the Motion API works with are in the format of ISO 8601. **Motion will always return dates in UTC.** 

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from datetime import datetime
from typing import Any, ClassVar, Dict, List, Optional
from pydantic import BaseModel, StrictStr, field_validator
from pydantic import Field
from typing_extensions import Annotated
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class ProjectPost(BaseModel):
    """
    ProjectPost
    """ # noqa: E501
    due_date: Optional[datetime] = Field(default=None, description="ISO 8601 Due date on the task", alias="dueDate")
    name: Annotated[str, Field(min_length=1, strict=True)]
    workspace_id: StrictStr = Field(alias="workspaceId")
    description: Optional[StrictStr] = None
    labels: Optional[List[StrictStr]] = None
    status: Optional[StrictStr] = None
    priority: Optional[StrictStr] = None
    __properties: ClassVar[List[str]] = ["dueDate", "name", "workspaceId", "description", "labels", "status", "priority"]

    @field_validator('priority')
    def priority_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('ASAP', 'HIGH', 'MEDIUM', 'LOW'):
            raise ValueError("must be one of enum values ('ASAP', 'HIGH', 'MEDIUM', 'LOW')")
        return value

    model_config = {
        "populate_by_name": True,
        "validate_assignment": True
    }


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of ProjectPost from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        _dict = self.model_dump(
            by_alias=True,
            exclude={
            },
            exclude_none=True,
        )
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of ProjectPost from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "dueDate": obj.get("dueDate"),
            "name": obj.get("name"),
            "workspaceId": obj.get("workspaceId"),
            "description": obj.get("description"),
            "labels": obj.get("labels"),
            "status": obj.get("status"),
            "priority": obj.get("priority")
        })
        return _obj


