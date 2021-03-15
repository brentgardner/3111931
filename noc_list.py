"""Noc List

This script allows the user to request retrieve a list of VIP users from the
The Bureau of Adversarial Dossiers and Securely Encrypted Code (BADSEC) API.

This script requires that `requests` be installed within the Python3
environment.

This file can also be imported as a module and contains the following
functions:

    * main - the main function of the script
"""

from noc_list_api import NocListApi
import sys

def main():

    try:
        noc_list_api = NocListApi()
        noc_list_users = noc_list_api.users()

        print(noc_list_users)

    except Exception as e:
        print(f"There was an error {e} running the NocList.", file=sys.stderr)
        sys.exit(f'{e}')

if __name__ == '__main__':
    main()