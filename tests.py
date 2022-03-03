import json
import unittest
import urllib
from unittest.mock import patch

from app import app

app.config.update({'TESTING': True, 'DEBUG': True})

BASE_URL = '/?reg='


def make_api_response(reg=''):
    # this fakes the MOT api response
    if reg == 'ZZ99ABC':  # valid registration number
        return [{
            "registration": "ZZ99ABC",
            "make": "FORD",
            "model": "FOCUS",
            "firstUsedDate": "2010.11.13",
            "motTests": [
                {
                    "completedDate": "2013.11.03 09:33:08",
                    "testResult": "PASSED",
                    "expiryDate": "2014.11.02",
                    "odometerValue": "47125",
                    "odometerUnit": "mi",
                    "odometerResultType": "READ",
                    "motTestNumber": "914655760009",
                    "rfrAndComments": []
                }
            ]
        }]
    elif reg == '':  # empty registration number
        return {
            "httpStatus": "404",
            "errorMessage": "",
        }
    else:  # invalid registration number
        return urllib.error.HTTPError(
            'http://example.com', 404, 'No MOT Tests found with vehicle registration : FAFAFA', {}, None)


class TestUrlopen(unittest.TestCase):
    def setUp(self):
        self.ctx = app.app_context()
        self.ctx.push()
        self.client = app.test_client()

    def tearDown(self):
        self.ctx.pop()

    @ patch('urllib.request.urlopen')
    def test_valid_registration_returns_data(self, mock_urlopen):
        # Mocking access to Web API
        mock_urlopen().read.return_value = json.dumps(make_api_response('ZZ99ABC'))

        response = self.client.get(BASE_URL+'ZZ99ABC')
        self.assertEqual(response.status, '200 OK')
        self.assertEqual(
            json.loads(response.data)['registration'],
            'ZZ99ABC')

    @ patch('urllib.request.urlopen')
    def test_no_registration_returns_error_message(self, mock_urlopen):
        # Mocking access to Web API
        mock_urlopen().read.return_value = json.dumps(make_api_response(''))

        response = self.client.get(BASE_URL+'')
        self.assertEqual(response.status, '200 OK')
        self.assertEqual(
            json.loads(response.data)['error'],
            'Please specify a reg number')

    @ patch('urllib.request.urlopen')
    def test_invalid_registration_returns_error_message(self, mock_urlopen):
        # Mocking access to Web API
        mock_urlopen().read.side_effect = make_api_response('FAFAFA')

        response = self.client.get(BASE_URL+'FAFAFA')
        self.assertEqual(response.status, '200 OK')
        self.assertEqual(
            json.loads(response.data)['error'],
            'The registration is invalid or cannot be found')


if __name__ == "__main__":
    unittest.main()
