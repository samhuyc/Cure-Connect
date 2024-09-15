# coding: utf-8

"""
    ClinicalTrials.gov REST API

    This API is made available to provide users meta data, statistics, and the most recent version of the clinical trials available on ClinicalTrials.gov.

    The version of the OpenAPI document: 2.0.3
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.study import Study

class TestStudy(unittest.TestCase):
    """Study unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Study:
        """Test Study
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Study`
        """
        model = Study()
        if include_optional:
            return Study(
                protocol_section = openapi_client.models.protocol_section.ProtocolSection(
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
                            date = '', ), 
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
                            investigator_full_name = '', 
                            investigator_title = '', 
                            investigator_affiliation = '', 
                            old_name_title = '', 
                            old_organization = '', ), 
                        lead_sponsor = openapi_client.models.sponsor.Sponsor(
                            name = '', ), 
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
                            count = 56, ), ), 
                    arms_interventions_module = openapi_client.models.arms_interventions_module.ArmsInterventionsModule(
                        arm_groups = [
                            openapi_client.models.arm_group.ArmGroup(
                                label = '', 
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
                        url = '', ), ),
                results_section = openapi_client.models.results_section.ResultsSection(
                    participant_flow_module = openapi_client.models.participant_flow_module.ParticipantFlowModule(
                        pre_assignment_details = '', 
                        recruitment_details = '', 
                        type_units_analyzed = '', 
                        groups = [
                            openapi_client.models.flow_group.FlowGroup(
                                id = '', 
                                title = '', 
                                description = '', )
                            ], 
                        periods = [
                            openapi_client.models.flow_period.FlowPeriod(
                                title = '', 
                                milestones = [
                                    openapi_client.models.flow_milestone.FlowMilestone(
                                        type = '', 
                                        comment = '', 
                                        achievements = [
                                            openapi_client.models.flow_stats.FlowStats(
                                                group_id = '', 
                                                comment = '', 
                                                num_subjects = '', 
                                                num_units = '', )
                                            ], )
                                    ], 
                                drop_withdraws = [
                                    openapi_client.models.drop_withdraw.DropWithdraw(
                                        type = '', 
                                        comment = '', 
                                        reasons = [
                                            openapi_client.models.flow_stats.FlowStats(
                                                group_id = '', 
                                                comment = '', 
                                                num_subjects = '', 
                                                num_units = '', )
                                            ], )
                                    ], )
                            ], ), 
                    baseline_characteristics_module = openapi_client.models.baseline_characteristics_module.BaselineCharacteristicsModule(
                        population_description = '', 
                        type_units_analyzed = '', 
                        denoms = [
                            openapi_client.models.denom.Denom(
                                units = '', 
                                counts = [
                                    openapi_client.models.denom_count.DenomCount(
                                        group_id = '', 
                                        value = '', )
                                    ], )
                            ], 
                        measures = [
                            openapi_client.models.baseline_measure.BaselineMeasure(
                                title = '', 
                                description = '', 
                                population_description = '', 
                                param_type = 'GEOMETRIC_MEAN', 
                                dispersion_type = 'NA', 
                                unit_of_measure = '', 
                                calculate_pct = True, 
                                denom_units_selected = '', 
                                classes = [
                                    openapi_client.models.measure_class.MeasureClass(
                                        title = '', 
                                        categories = [
                                            openapi_client.models.measure_category.MeasureCategory(
                                                title = '', 
                                                measurements = [
                                                    openapi_client.models.measurement.Measurement(
                                                        group_id = '', 
                                                        value = '', 
                                                        spread = '', 
                                                        lower_limit = '', 
                                                        upper_limit = '', 
                                                        comment = '', )
                                                    ], )
                                            ], )
                                    ], )
                            ], ), 
                    outcome_measures_module = openapi_client.models.outcome_measures_module.OutcomeMeasuresModule(
                        outcome_measures = [
                            openapi_client.models.outcome_measure.OutcomeMeasure(
                                type = 'PRIMARY', 
                                title = '', 
                                description = '', 
                                population_description = '', 
                                reporting_status = 'NOT_POSTED', 
                                anticipated_posting_date = '', 
                                unit_of_measure = '', 
                                calculate_pct = True, 
                                time_frame = '', 
                                type_units_analyzed = '', 
                                denom_units_selected = '', 
                                analyses = [
                                    openapi_client.models.measure_analysis.MeasureAnalysis(
                                        param_value = '', 
                                        dispersion_value = '', 
                                        statistical_method = '', 
                                        statistical_comment = '', 
                                        p_value = '', 
                                        p_value_comment = '', 
                                        ci_num_sides = 'ONE_SIDED', 
                                        ci_pct_value = '', 
                                        ci_lower_limit = '', 
                                        ci_upper_limit = '', 
                                        ci_lower_limit_comment = '', 
                                        ci_upper_limit_comment = '', 
                                        estimate_comment = '', 
                                        tested_non_inferiority = True, 
                                        non_inferiority_type = 'SUPERIORITY', 
                                        non_inferiority_comment = '', 
                                        other_analysis_description = '', 
                                        group_description = '', 
                                        group_ids = [
                                            ''
                                            ], )
                                    ], )
                            ], ), 
                    adverse_events_module = openapi_client.models.adverse_events_module.AdverseEventsModule(
                        frequency_threshold = '', 
                        time_frame = '', 
                        description = '', 
                        all_cause_mortality_comment = '', 
                        event_groups = [
                            openapi_client.models.event_group.EventGroup(
                                id = '', 
                                title = '', 
                                description = '', 
                                deaths_num_affected = 56, 
                                deaths_num_at_risk = 56, 
                                serious_num_affected = 56, 
                                serious_num_at_risk = 56, 
                                other_num_affected = 56, 
                                other_num_at_risk = 56, )
                            ], 
                        serious_events = [
                            openapi_client.models.adverse_event.AdverseEvent(
                                term = '', 
                                organ_system = '', 
                                source_vocabulary = '', 
                                assessment_type = 'NON_SYSTEMATIC_ASSESSMENT', 
                                notes = '', 
                                stats = [
                                    openapi_client.models.event_stats.EventStats(
                                        group_id = '', 
                                        num_events = 56, 
                                        num_affected = 56, 
                                        num_at_risk = 56, )
                                    ], )
                            ], 
                        other_events = [
                            openapi_client.models.adverse_event.AdverseEvent(
                                term = '', 
                                organ_system = '', 
                                source_vocabulary = '', 
                                notes = '', )
                            ], ), 
                    more_info_module = openapi_client.models.more_info_module.MoreInfoModule(
                        limitations_and_caveats = openapi_client.models.limitations_and_caveats.LimitationsAndCaveats(
                            description = '', ), 
                        certain_agreement = openapi_client.models.certain_agreement.CertainAgreement(
                            pi_sponsor_employee = True, 
                            restriction_type = 'LTE60', 
                            restrictive_agreement = True, 
                            other_details = '', ), 
                        point_of_contact = openapi_client.models.point_of_contact.PointOfContact(
                            title = '', 
                            organization = '', 
                            email = '', 
                            phone = '', 
                            phone_ext = '', ), ), ),
                annotation_section = openapi_client.models.annotation_section.AnnotationSection(
                    annotation_module = openapi_client.models.annotation_module.AnnotationModule(
                        unposted_annotation = openapi_client.models.unposted_annotation.UnpostedAnnotation(
                            unposted_responsible_party = '', 
                            unposted_events = [
                                openapi_client.models.unposted_event.UnpostedEvent(
                                    type = 'RESET', 
                                    date = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(), 
                                    date_unknown = True, )
                                ], ), 
                        violation_annotation = openapi_client.models.violation_annotation.ViolationAnnotation(
                            violation_events = [
                                openapi_client.models.violation_event.ViolationEvent(
                                    description = '', 
                                    creation_date = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(), 
                                    issued_date = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(), 
                                    release_date = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(), 
                                    posted_date = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(), )
                                ], ), ), ),
                document_section = openapi_client.models.document_section.DocumentSection(
                    large_document_module = openapi_client.models.large_document_module.LargeDocumentModule(
                        no_sap = True, 
                        large_docs = [
                            openapi_client.models.large_doc.LargeDoc(
                                type_abbrev = '', 
                                has_protocol = True, 
                                has_sap = True, 
                                has_icf = True, 
                                label = '', 
                                date = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(), 
                                upload_date = '', 
                                filename = '', 
                                size = 56, )
                            ], ), ),
                derived_section = openapi_client.models.derived_section.DerivedSection(
                    misc_info_module = openapi_client.models.misc_info_module.MiscInfoModule(
                        version_holder = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(), 
                        removed_countries = [
                            ''
                            ], 
                        submission_tracking = openapi_client.models.submission_tracking.SubmissionTracking(
                            estimated_results_first_submit_date = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(), 
                            first_mcp_info = openapi_client.models.first_mcp_info.FirstMcpInfo(
                                post_date_struct = openapi_client.models.date_struct.DateStruct(
                                    date = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(), 
                                    type = 'ACTUAL', ), ), 
                            submission_infos = [
                                openapi_client.models.submission_info.SubmissionInfo(
                                    release_date = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(), 
                                    unrelease_date = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(), 
                                    unrelease_date_unknown = True, 
                                    reset_date = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(), 
                                    mcp_release_n = 56, )
                                ], ), ), 
                    condition_browse_module = openapi_client.models.browse_module.BrowseModule(
                        meshes = [
                            openapi_client.models.mesh.Mesh(
                                id = '', 
                                term = '', )
                            ], 
                        ancestors = [
                            openapi_client.models.mesh.Mesh(
                                id = '', 
                                term = '', )
                            ], 
                        browse_leaves = [
                            openapi_client.models.browse_leaf.BrowseLeaf(
                                id = '', 
                                name = '', 
                                as_found = '', 
                                relevance = 'LOW', )
                            ], 
                        browse_branches = [
                            openapi_client.models.browse_branch.BrowseBranch(
                                abbrev = '', 
                                name = '', )
                            ], ), 
                    intervention_browse_module = openapi_client.models.browse_module.BrowseModule(), ),
                has_results = True
            )
        else:
            return Study(
        )
        """

    def testStudy(self):
        """Test Study"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
