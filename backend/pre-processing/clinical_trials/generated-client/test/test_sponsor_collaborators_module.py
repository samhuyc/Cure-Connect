# coding: utf-8

"""
    ClinicalTrials.gov REST API

    This API is made available to provide users meta data, statistics, and the most recent version of the clinical trials available on ClinicalTrials.gov.

    The version of the OpenAPI document: 2.0.3
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.sponsor_collaborators_module import SponsorCollaboratorsModule

class TestSponsorCollaboratorsModule(unittest.TestCase):
    """SponsorCollaboratorsModule unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> SponsorCollaboratorsModule:
        """Test SponsorCollaboratorsModule
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `SponsorCollaboratorsModule`
        """
        model = SponsorCollaboratorsModule()
        if include_optional:
            return SponsorCollaboratorsModule(
                responsible_party = openapi_client.models.responsible_party.ResponsibleParty(
                    type = 'SPONSOR', 
                    investigator_full_name = '', 
                    investigator_title = '', 
                    investigator_affiliation = '', 
                    old_name_title = '', 
                    old_organization = '', ),
                lead_sponsor = openapi_client.models.sponsor.Sponsor(
                    name = '', 
                    class = 'NIH', ),
                collaborators = [
                    openapi_client.models.sponsor.Sponsor(
                        name = '', 
                        class = 'NIH', )
                    ]
            )
        else:
            return SponsorCollaboratorsModule(
        )
        """

    def testSponsorCollaboratorsModule(self):
        """Test SponsorCollaboratorsModule"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
