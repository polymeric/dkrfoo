#!/usr/bin/env python3

'''
Desc:
Manage docker constructs for test automation.

list images
list containers
pull image
build image
create network
start container
health check container
stop container
delete container, image, network

Usage:
from lib import dkrutil

'''

import uuid

import docker


class DkrMgr(object):

    def __init__(self):
        """ Create docker client instance, internal obj cache """
        self._internal_dkr_cache = []
        self.dkrobj              = docker.DockerClient()

    def _update_internal_cache(self, objtype, name):
        """ Keep track of what we create in the instance """
        name = (':').join(name, uuid.uuid4)
        self._internal_dkr_cache.append(name)

    def _is_internal(self, name):
        """ Private method: Return true if name in cache """
        return [True for x in self._internal_dkr_cache if name in x]

    def get_image_names(self):
        " Return list of all image tag names "
        img_obj_list = self.dkrobj.images.list()
        tags = [x.tags for x in img_obj_list]
        return tags 

    def get_container_names(self):
        """ Return list of all containers """
        container_list = self.dkrobj.containers.list()
        names = [x.name for x in container_list]
        return names

    def get_container_status(self, name):
        """ Return status of container """
        return [x.status for x in self.dkrobj.containers.list() if x.name == 'name']

    def get_container_logs(self, name):
        pass

    def get_networks(self):
        """ Return list of networks """
        return [x.name for x in self.dkrobj.networks.list()]

    def build_img(self, dockerfile_name):
        """ Build image based on dockerfile """
        _update_internal_cache(self, obj_type, name)
        pass

    def create_network(self, name):
        """ Create a network """
        _update_internal_cache(self, obj_type, name)
        self.dkrobj.networks.create(name)

    def start_container(self, docker_tag, name, parms):
        """ Start a container
       
            docker_tag, 
            name = container runtime label,
            parms = Similar to docker run any parameters must be supplied:
            "-p 31415:31415 -v $pwd/data:/data -e $TLS_ENABLED='FALSE'"
        """
        _update_internal_cache(self, obj_type, name)
        pass

    def stop_container(self, name):
        container_id = [x.id for x in self.dkrobj.containers.list() if x.name == name]
        container = self.dkrobj.containers.get(container_id)
        container.stop()

    def del_image(self, name):
        pass

    def del_container(self, name):
        pass

    def del_network(self, name):
        if name in _is_internal(name):
            [x.remove() for x in self.dkrobj.networks.list() if x.name == 'name']



