import hashlib
import json
import requests
import sys
from urllib.parse import urljoin

class NocListApi:
    """
    A class that represents a wrapper for the The Bureau of Adversarial Dossiers and Securely Encrypted Code (BADSEC) REST Api

    Attributes
    ----------
    MAX_ATTEMPTS : int
        the number of allowed attempted requests for any one API endpoint.
    NOCLIST_END_PT : str
        the root url for the Noc List Api.
    token : str
        the token that can use to generate the checksum for the any subsequent API requests.

    Methods
    -------
    checksum(end_pt)
        Returns a sha256 hash digest of the authentication token and the end_pt.
    auth()
        Performs a get request to the BADSEC Api and returns the authentication token.
    users()
        Performs a get request to the BADSEC Api and returns a JSON formated string.
    """

    # the number of allowed attempted requests for any one API endpoint.
    MAX_ATTEMPTS = 3
    
    # the root url for the Noc List Api.
    NOCLIST_BASE_URL = 'http://0.0.0.0:8888'

    def __init__(self):
        self.token = self.auth()

    @staticmethod
    def checksum(token, end_pt):
        """Static Method that returns a sha256 hash digest of the authentication token and the end_pt"""

        string_to_hash = f"{token}/{end_pt}"
        
        return hashlib.sha256(string_to_hash.encode('ascii')).hexdigest()
    
    def auth(self):
        """Performs a get request to the NocListApi and returns the authentication token.

        Raises
        ------
        Exception
            if any error is encounted or if the Max Attempts are reached.
        """

        # noclist auth end point.
        noclist_auth_end_pt = 'auth'
        
        # number of attemps that have been made.
        attempts = 0

        while attempts < self.MAX_ATTEMPTS:

            attempts = attempts + 1

            try:
                # make a get request to the auth endpoint
                response = requests.get(urljoin(self.NOCLIST_BASE_URL, noclist_auth_end_pt))

                # If the respons status code indicates success return the auth token included in the response HTTP header value for key 'Badsec-Authentication-Token'.
                if response.status_code == 200:
                    return response.headers['Badsec-Authentication-Token']    
            except:
                print(f"authentication error attempt {attempts}", file=sys.stderr)
        
        # if max attempts are reached raise exception.
        if attempts == self.MAX_ATTEMPTS:
            raise Exception('max attempts reached error')

    def users(self):
        """Performs a get request to the NocListApi and returns a list of 64-bit newline-separated user IDs

        Raises
        ------
        Exception
            If any error is encounted a retry will be attempted until the max attempts are reached.
        """

        # noclist users end point.
        noclist_users_end_pt = 'users'

        # number of attemps that have been made.
        attempts = 0

        while attempts < self.MAX_ATTEMPTS:

            attempts = attempts + 1

            try:
                # calculate the checksum to authenticate the request
                checksum = NocListApi.checksum(self.token, noclist_users_end_pt)

                # include the checksum as a X-Request-Checksum in a header
                headers = {'X-Request-Checksum': checksum}

                # make a get request to the users endpoint and provide the checksum in the headers options.
                response = requests.get(urljoin(self.NOCLIST_BASE_URL, noclist_users_end_pt), headers= headers)

                # If the response status code is 200 then the a list of 64-bit newline-separated user IDs is returned as text.
                if response.status_code == 200:
                    # if the response text is not empty or None then parse it to a json array and return. 
                    # else a retry attempt will be made.
                    if response.text:
                        return json.dumps(response.text.split('\n'))
    
            except Exception as e:
                print(f"users error {e} attempt {attempts}", file=sys.stderr)
        
        # if max attempts are reached raise exception.
        if attempts == self.MAX_ATTEMPTS:
            raise Exception('max attempts reached error')

    


