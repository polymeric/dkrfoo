#!/usr/bin/env python3

""" Process a test config file.

    Test config describes test cases that will be launched and executes from a pytest
    instance.

    Test config yaml requirements:
      - Tests instances must have unique block identifiers.
        -- ie Test 1, Test 2...
      - Configurations syntax must be included in block syntax
      - Shell environment vars must be set per test block description
      - Order of operations is the rule
"""

import argparse
import os
import yaml

import docker
import pytest


def load_test_yaml(tconfig_file):
    try:
        with open(tconfig_file, 'r') as stream:
            tconfig = list(yaml.safe_load_all(stream))
        return tconfig
    except IOError as e:
        print(e)

def start_pytest(test_filename):
    """ This is used when running tests outside docker container """
    pytest_args = ['-r apP', '--tb=no', '--show-capture=no', test_filename]
    retval = pytest.main(pytest_args)
    raisePytestError(retval)
    return retval

def start_test_config(tconfig):
    print("Testing the following configuration:")
    print(tconfig)
    print("Starting test...")
    print("Current working directory: %s" %os.getcwd())
    # Set up docker environment
    client = docker.from_env()
    parse_docker_config(client, tconfig)
    #TODO: if testing locally use this otherwise work into config parser 
    start_pytest(tconfig['test_filename'])

def raisePytestError(retval):
    if retval == 0:
        print("SUCCESS: All tests in this config passed.")
    elif retval == 1:
        print("ERROR: Tests were collected and run but some of the tests failed")
    elif retval == 2:
        print("ERROR: Test execution was interrupted by the user")
    elif retval == 3:
        print("ERROR: Internal error happened while executing tests")
    elif retval == 4:
        print("ERROR: pytest command line usage error")
    elif retval == 5:
        print("ERROR: No tests were collected")
    else:
        print("ERROR: Unknown error condition.")

def parse_docker_config(client, tconfig):
    #TODO: will need to handle launching multiple containers
    if tconfig['docker_network']:
        create_docker_network(client, tconfig['docker_network'])
    if tconfig['Dockerfile']:
        create_docker_image(client, tconfig['Dockerfile'])
    elif tconfig['ComposeFile']:
        docker_compose_build(tconfig['ComposeFile'])
    elif tconfig['docker_image']:
        start_container(client, tconfig['docker_image'], tconfig['docker_run_vars'])

def docker_network_exists(client, docker_network_name):
    """ Return True if network exists"""
    exists = client.networks.get(docker_network_name)
    return exists

def create_docker_network(client, network_name):
    """ Create network if not present """
    if not docker_network_exists(client, network_name):
        client.networks.create(network_name)

def delete_docker_network(client, network_name):
    """ Delete docker network """
    if docker_network_exists(client, network_name):
        network = client.networks.get(network_name)
        network.remove()

def create_docker_image(client, dockerfile):
    # Dockerfile: "Dockerfile.server"
    pass

def delete_docker_image(client, image_name):
    pass

def start_container(client,image_name, params):
    '''
    docker_image: "dkrsrv"
    docker_run_vars:
        - "-e IS_DOCKER=YES"
        - "-v $(pwd)test/data:/data"
        - "--rm"
        - "-p 5000:5000"
        - "--network=drktest_foo"
    '''
    client.containers.run(image_name, params)

def delete_docker_container(client, container_name):
    pass

def docker_compose_build():
    pass

def docker_compose_up():
    pass

def main(test_config='testconfig.yaml'):
    """ Collect test instance configurations run tests """
    print("Starting tests...")
    # Get yaml
    print("Collecting test config yaml files...")
    test_cases = load_test_yaml(test_config)
    print("%s tests configurations detected..." % len(test_cases))
    for tconfig in test_cases:
        # Data received is nested dict{}. Strip outer dict.
        key=list(tconfig.keys())[0]
        start_test_config(tconfig[key])


if __name__ == "__main__":
    # set up logging

    # execute only if run as a script
    parser = argparse.ArgumentParser(description = 'Smoketest Runner')
    parser.add_argument('-t', '--testconfig', help='Path and name of test config file.')
    args = parser.parse_args()
    if args.testconfig:
        test_config = args.testconfig
        main(test_config)
    else:
        main()
