# How to run 3111931

## Requirements

python >= 3.6.13
requests >= 2.25.1

These instructions are targeted to macOS or Linux

## Running the server test api server

1. Ensure that you have [docker](https://www.docker.com/products/docker-desktop) installed on your system.
2. The BADSEC server will run on port 8888. You can start it by running in a shell:

    `docker run --rm -p 8888:8888 adhocteam/noclist`

3. If all goes well you should see Listening on http://0.0.0.0:8888.


## Setting up the Python application

1. Ensure that you have [Python](https://www.python.org/downloads/) installed on your system.
2. Clone the 3111931 github repository.
3. Change directories into the 3111931 directory.
4. Create a virtual environment.
    `python -m venv 3111931-env`
5. Activate virtual environment.
    `source 3111931-env/bin/activate`
6. Install the equirements for 3111931.
    `pip install -r requirements.txt`


## Running 3111931

1. Ensure that the BADSEC docker container is running and listening on http://0.0.0.0:8888.
2. Open a command prompt and change directories into the 3111931 repository that you cloned during setup.
3. Run the application.
    `python noc_list.py`
4. You should see a JSON formatted string to stdout.
    `["9757263792576857988", "7789651288773276582", "16283886502782682407", "...etc"]`

## Running the tests for 3111931

1. Ensure that the BADSEC docker container is running and listening on http://0.0.0.0:8888.
2. Open a command prompt and change directories into the 3111931 repository that you cloned during setup.
3. Run the test script.
    `python test_noc_list_api.py`
