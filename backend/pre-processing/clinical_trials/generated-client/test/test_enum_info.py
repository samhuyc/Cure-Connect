# coding: utf-8

"""
    ClinicalTrials.gov REST API

    This API is made available to provide users meta data, statistics, and the most recent version of the clinical trials available on ClinicalTrials.gov.

    The version of the OpenAPI document: 2.0.3
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.enum_info import EnumInfo

class TestEnumInfo(unittest.TestCase):
    """EnumInfo unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> EnumInfo:
        """Test EnumInfo
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `EnumInfo`
        """
        model = EnumInfo()
        if include_optional:
            return EnumInfo(
                pieces = [
                    ''
                    ],
                type = '',
                values = [
                    openapi_client.models.enum_item.EnumItem(
                        exceptions = openapi_client.models.exceptions.exceptions(), 
                        legacy_value = '', 
                        value = '', )
                    ]
            )
        else:
            return EnumInfo(
                pieces = [
                    ''
                    ],
                type = '',
                values = [
                    openapi_client.models.enum_item.EnumItem(
                        exceptions = openapi_client.models.exceptions.exceptions(), 
                        legacy_value = '', 
                        value = '', )
                    ],
        )
        """

    def testEnumInfo(self):
        """Test EnumInfo"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
