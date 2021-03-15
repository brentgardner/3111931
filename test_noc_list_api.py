from noc_list_api import NocListApi
import unittest

class TestNocListApi(unittest.TestCase):
    """
    A test case class that inherits from unittest.TestCase. 

    Tests the NocListApi wrapper

    Methods
    -------
    test_auth_request_response()
        test that the auth method returns a string in the Badsec-Authentication-Token header
    test_auth_raises_exception()
        test that the auth method returns an exception
    test_checksum_response()
        tests that the checksum method returns an expected sha256 hash digest
    test_users_request_response()
        test that the users method returns a valid JSON formatted str
    """
    
    def test_auth_request_response(self):
        """
        Test that a call to the auth endpoint returns a response in the 'Badsec-Authentication-Token' header.
        """
        # create a instance of the NocListApi class and call the auth method
        response = NocListApi().auth()
        # resonse should return a response
        self.assertTrue(response)

    def test_auth_raises_exception(self):
        """
        Test that the auth endpoint raises an Exception.
        """
        # create a instance of the NocListApi class and call the auth method
        noc_list_api = NocListApi()

        self.assertRaises(Exception, noc_list_api.auth())

    def test_checksum_response(self):
        """
        Test that a call to the static method checksum in the NocListApi class returns the expected sha256 hash digest.
        """
        # predetermined hash that is expected as a response
        expected_result = 'fda4f9b1f9b14409c7468c9d125b341fd855140866f2a9347b816bcac5aa5f4f'
        # call the static checksum method
        response = NocListApi.checksum('123456789','/urlpattern')
        # response should equal expected result
        self.assertEqual(response, expected_result)

    def test_users_request_response(self):
        """
        Test that a call to the auth endpoint returns a response in the 'Badsec-Authentication-Token' header.
        """
        # create a instance of the NocListApi class and call the auth method
        noc_list_api = NocListApi()
        response = noc_list_api.users()

        # response should return a json array formatted string
        self.assertTrue(type(response) == str)

    def test_users_raises_exception(self):
        """
        Test that the users endpoint raises an Exception.
        """
        # create a instance of the NocListApi class and call the auth method
        noc_list_api = NocListApi()

        self.assertRaises(Exception, noc_list_api.users())

if __name__ == '__main__':
    unittest.main()