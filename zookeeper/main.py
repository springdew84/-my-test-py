# -*- coding:utf-8 -*-

import sys
#from kazoo.client import KazooClient
import logging

logging.basicConfig(level=logging.ERROR)

# local service dir
LOCAL_SERVICE = '/services/local-service'


class PyZooConn(object):
    # init function include connection method
    def __init__(self):
        #self.zk = KazooClient(hosts='localhost:2181')
        self.zk.start()

    # get node data
    def get_data(self, param):
        result = self.zk.get(param)
        return result

    def get_children(self, param):
        result = self.zk.get_children(param)
        return result

    # create a node and input a value in this node
    def create_node(self, node, value):
        self.zk.create(node, value)

    # delete a node
    def delete_node(self, param):
        self.zk.delete(param)

    # close the connection
    def close(self):
        self.zk.stop()


if __name__ == '__main__':
    servicePort = str(sys.argv[1])
    # print "delete zk local service node " + servicePort
    pz = PyZooConn()
    # pz.create_node("/test", "a value")
    services = pz.get_children(LOCAL_SERVICE)

    # curl "https://ws.it4.dealmoon.net/health"

    for data in services:
        servicePath = LOCAL_SERVICE + "/" + data
        # print servicePath
        service = pz.get_data(servicePath)
        serviceStr = str(service)
        if (servicePort in serviceStr):
            # print "delete" + servicePort
            pz.delete_node(servicePath)
            # print "delete zk service node:" + servicePath
    pz.close()