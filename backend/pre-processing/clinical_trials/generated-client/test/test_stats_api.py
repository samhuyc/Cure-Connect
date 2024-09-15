# coding: utf-8

"""
    ClinicalTrials.gov REST API

    This API is made available to provide users meta data, statistics, and the most recent version of the clinical trials available on ClinicalTrials.gov.

    The version of the OpenAPI document: 2.0.3
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.api.stats_api import StatsApi


class TestStatsApi(unittest.TestCase):
    """StatsApi unit test stubs"""

    def setUp(self) -> None:
        self.api = StatsApi()

    def tearDown(self) -> None:
        pass

    def test_field_values_stats(self) -> None:
        """Test case for field_values_stats

        Field Values
        """
        pass

    def test_list_field_sizes_stats(self) -> None:
        """Test case for list_field_sizes_stats

        List Field Sizes
        """
        pass

    def test_size_stats(self) -> None:
        """Test case for size_stats

        Study Sizes
        """
        pass


if __name__ == '__main__':
    unittest.main()
