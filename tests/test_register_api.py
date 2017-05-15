import unittest
import requests
import pytest

class TestRegisterApi(unittest.TestCase):
    @pytest.mark.apitest
    def test_unauthorized(self):
        resp = requests.get('https://patient.heal.com/api/v3/')
        assert resp.status_code == 403


    @pytest.mark.apitest
    def test_genders(self):
        resp = requests.get('https://patient.heal.com/api/config/patients')
        d = resp.json()

        expected_codes = ['F', 'M', 'O']
        expected_names = ['Female', 'Male', 'Other']

        actual_codes = [gen['insuranceBillingCode'] for gen in d['genders']]
        actual_names = [gen['name'] for gen in d['genders']]

        assert expected_codes == actual_codes
        assert expected_names == actual_names


    @pytest.mark.apitest
    def test_relationships(self):
        resp = requests.get('https://patient.heal.com/api/config/patients')
        d = resp.json()

        expected_rels = [
            'Spouse',
            'Partner',
            'Grandparent',
            'Grandchild',
            'Child',
            'Parent',
            'Sibling',
            'Other',
            'You',
            'Friend',
            'Coworker',
            'Assisted Living Resident',
            'Skilled Nursing Facility'
        ]

        #check that the data is exactly the same for expected and actual relationship lists
        assert expected_rels == [rel['name'] for rel in d['relationships']]


        #check a couple of types for fun
        for rel in d['relationships']:
            assert type(rel['insuranceUsage']) is bool
            assert type(rel['frozen']) is bool


    @pytest.mark.apitest
    def test_payers(self):
        resp = requests.get('https://patient.heal.com/api/config/patients')
        d = resp.json()

        expected_payers = [
            'aetna',
            'Anthem Blue Cross',
            'BlueShield',
            'Cigna',
            'Meritain Health (aetna)',
            'Nippon Life Benefits (aetna)',
            'Premera BlueCross',
            'UMR (United Healthcare)',
            'United Healthcare',
            'NALC (Cigna)',
            'GEHA'
        ]

        actual_payers = [payer['shortName'] for payer in d['payers']]

        # check that the data is exactly the same for expected and actual payer lists
        assert expected_payers == actual_payers
