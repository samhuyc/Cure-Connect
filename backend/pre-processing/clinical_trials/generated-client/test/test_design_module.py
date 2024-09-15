# coding: utf-8

"""
    ClinicalTrials.gov REST API

    This API is made available to provide users meta data, statistics, and the most recent version of the clinical trials available on ClinicalTrials.gov.

    The version of the OpenAPI document: 2.0.3
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.design_module import DesignModule

class TestDesignModule(unittest.TestCase):
    """DesignModule unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> DesignModule:
        """Test DesignModule
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `DesignModule`
        """
        model = DesignModule()
        if include_optional:
            return DesignModule(
                study_type = 'EXPANDED_ACCESS',
                n_ptrs_to_this_exp_acc_nct_id = 1.337,
                expanded_access_types = openapi_client.models.expanded_access_types.ExpandedAccessTypes(
                    individual = True, 
                    intermediate = True, 
                    treatment = True, ),
                patient_registry = True,
                target_duration = '4 Month',
                phases = [
                    'NA'
                    ],
                design_info = openapi_client.models.design_info.DesignInfo(
                    allocation = 'RANDOMIZED', 
                    intervention_model = 'SINGLE_GROUP', 
                    intervention_model_description = '', 
                    primary_purpose = 'TREATMENT', 
                    observational_model = 'COHORT', 
                    time_perspective = 'RETROSPECTIVE', 
                    masking_info = openapi_client.models.masking_block.MaskingBlock(
                        masking = 'NONE', 
                        masking_description = '', 
                        who_masked = [
                            'PARTICIPANT'
                            ], ), ),
                bio_spec = openapi_client.models.bio_spec.BioSpec(
                    retention = 'NONE_RETAINED', 
                    description = '', ),
                enrollment_info = openapi_client.models.enrollment_info.EnrollmentInfo(
                    count = 56, 
                    type = 'ACTUAL', )
            )
        else:
            return DesignModule(
        )
        """

    def testDesignModule(self):
        """Test DesignModule"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
