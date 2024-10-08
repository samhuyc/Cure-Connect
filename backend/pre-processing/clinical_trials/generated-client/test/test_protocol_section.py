# coding: utf-8

"""
    ClinicalTrials.gov REST API

    This API is made available to provide users meta data, statistics, and the most recent version of the clinical trials available on ClinicalTrials.gov.

    The version of the OpenAPI document: 2.0.3
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.protocol_section import ProtocolSection

class TestProtocolSection(unittest.TestCase):
    """ProtocolSection unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ProtocolSection:
        """Test ProtocolSection
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ProtocolSection`
        """
        model = ProtocolSection()
        if include_optional:
            return ProtocolSection(
                identification_module = openapi_client.models.identification_module.IdentificationModule(
                    nct_id = '', 
                    nct_id_aliases = [
                        ''
                        ], 
                    org_study_id_info = openapi_client.models.org_study_id_info.OrgStudyIdInfo(
                        id = '', 
                        type = 'NIH', 
                        link = '', ), 
                    secondary_id_infos = [
                        openapi_client.models.secondary_id_info.SecondaryIdInfo(
                            id = '', 
                            domain = '', 
                            link = '', )
                        ], 
                    brief_title = '', 
                    official_title = '', 
                    acronym = '', 
                    organization = openapi_client.models.organization.Organization(
                        full_name = '', 
                        class = 'NIH', ), ),
                status_module = openapi_client.models.status_module.StatusModule(
                    status_verified_date = '', 
                    overall_status = 'ACTIVE_NOT_RECRUITING', 
                    last_known_status = 'ACTIVE_NOT_RECRUITING', 
                    delayed_posting = True, 
                    why_stopped = '', 
                    expanded_access_info = openapi_client.models.expanded_access_info.ExpandedAccessInfo(
                        has_expanded_access = True, 
                        nct_id = '', 
                        status_for_nct_id = 'AVAILABLE', ), 
                    start_date_struct = openapi_client.models.partial_date_struct.PartialDateStruct(
                        date = '', 
                        type = 'ACTUAL', ), 
                    primary_completion_date_struct = openapi_client.models.partial_date_struct.PartialDateStruct(), 
                    completion_date_struct = , 
                    study_first_submit_date = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(), 
                    study_first_submit_qc_date = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(), 
                    study_first_post_date_struct = openapi_client.models.date_struct.DateStruct(), 
                    results_first_submit_date = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(), 
                    results_first_submit_qc_date = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(), 
                    results_first_post_date_struct = openapi_client.models.date_struct.DateStruct(), 
                    disp_first_submit_date = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(), 
                    disp_first_submit_qc_date = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(), 
                    disp_first_post_date_struct = , 
                    last_update_submit_date = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(), 
                    last_update_post_date_struct = , ),
                sponsor_collaborators_module = openapi_client.models.sponsor_collaborators_module.SponsorCollaboratorsModule(
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
                            name = '', )
                        ], ),
                oversight_module = openapi_client.models.oversight_module.OversightModule(
                    oversight_has_dmc = True, 
                    is_fda_regulated_drug = True, 
                    is_fda_regulated_device = True, 
                    is_unapproved_device = True, 
                    is_ppsd = True, 
                    is_us_export = True, 
                    fdaaa801_violation = True, ),
                description_module = openapi_client.models.description_module.DescriptionModule(
                    brief_summary = '', 
                    detailed_description = '', ),
                conditions_module = openapi_client.models.conditions_module.ConditionsModule(
                    conditions = [
                        ''
                        ], 
                    keywords = [
                        ''
                        ], ),
                design_module = openapi_client.models.design_module.DesignModule(
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
                        type = 'ACTUAL', ), ),
                arms_interventions_module = openapi_client.models.arms_interventions_module.ArmsInterventionsModule(
                    arm_groups = [
                        openapi_client.models.arm_group.ArmGroup(
                            label = '', 
                            type = 'EXPERIMENTAL', 
                            description = '', 
                            intervention_names = [
                                ''
                                ], )
                        ], 
                    interventions = [
                        openapi_client.models.intervention.Intervention(
                            name = '', 
                            description = '', 
                            arm_group_labels = [
                                ''
                                ], 
                            other_names = [
                                ''
                                ], )
                        ], ),
                outcomes_module = openapi_client.models.outcomes_module.OutcomesModule(
                    primary_outcomes = [
                        openapi_client.models.outcome.Outcome(
                            measure = '', 
                            description = '', 
                            time_frame = '', )
                        ], 
                    secondary_outcomes = [
                        openapi_client.models.outcome.Outcome(
                            measure = '', 
                            description = '', 
                            time_frame = '', )
                        ], 
                    other_outcomes = [
                        
                        ], ),
                eligibility_module = openapi_client.models.eligibility_module.EligibilityModule(
                    eligibility_criteria = '', 
                    healthy_volunteers = True, 
                    sex = 'FEMALE', 
                    gender_based = True, 
                    gender_description = '', 
                    minimum_age = '4 Month', 
                    maximum_age = '4 Month', 
                    std_ages = [
                        'CHILD'
                        ], 
                    study_population = '', 
                    sampling_method = 'PROBABILITY_SAMPLE', ),
                contacts_locations_module = openapi_client.models.contacts_locations_module.ContactsLocationsModule(
                    central_contacts = [
                        openapi_client.models.contact.Contact(
                            name = '', 
                            role = 'STUDY_CHAIR', 
                            phone = '', 
                            phone_ext = '', 
                            email = '', )
                        ], 
                    overall_officials = [
                        openapi_client.models.official.Official(
                            name = '', 
                            affiliation = '', )
                        ], 
                    locations = [
                        openapi_client.models.location.Location(
                            facility = '', 
                            status = 'ACTIVE_NOT_RECRUITING', 
                            city = '', 
                            state = '', 
                            zip = '', 
                            country = '', 
                            contacts = [
                                openapi_client.models.contact.Contact(
                                    name = '', 
                                    phone = '', 
                                    phone_ext = '', 
                                    email = '', )
                                ], 
                            country_code = '', 
                            geo_point = openapi_client.models.geo_point.GeoPoint(
                                lat = 1.337, 
                                lon = 1.337, ), )
                        ], ),
                references_module = openapi_client.models.references_module.ReferencesModule(
                    references = [
                        openapi_client.models.reference.Reference(
                            pmid = '', 
                            type = 'BACKGROUND', 
                            citation = '', 
                            retractions = [
                                openapi_client.models.retraction.Retraction(
                                    pmid = '', 
                                    source = '', )
                                ], )
                        ], 
                    see_also_links = [
                        openapi_client.models.see_also_link.SeeAlsoLink(
                            label = '', 
                            url = '', )
                        ], 
                    avail_ipds = [
                        openapi_client.models.avail_ipd.AvailIpd(
                            id = '', 
                            url = '', 
                            comment = '', )
                        ], ),
                ipd_sharing_statement_module = openapi_client.models.ipd_sharing_statement_module.IpdSharingStatementModule(
                    ipd_sharing = 'YES', 
                    description = '', 
                    info_types = [
                        'STUDY_PROTOCOL'
                        ], 
                    time_frame = '', 
                    access_criteria = '', 
                    url = '', )
            )
        else:
            return ProtocolSection(
        )
        """

    def testProtocolSection(self):
        """Test ProtocolSection"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
