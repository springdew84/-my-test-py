# -*- coding: utf-8 -*-

from kazoo.client import KazooClient

class PyZooConn(object):
    # init function include connection method
    def __init__(self):
        self.zk = KazooClient(hosts='localhost:2181')
        self.zk.start()

    # get node data
    def get_data(self, param):
        result = self.zk.get(param)
        print result

    def get_children(self, param):
        result = self.zk.get_children(param)
        print result

    # create a node and input a value in this node
    def create_node(self, node, value):
        self.zk.create(node, value)


    # close the connection
    def close(self):
        self.zk.stop()

if __name__ == '__main__':
    pz = PyZooConn()
    #pz.create_node("/test", "a value")
    #pz.get_children("/services/local-service/ac09e7aa-1abc-47fe-990a-cbce9f37f483")
    services = pz.get_children("/services/local-service")
    for data in services:
      print str(data))
      print "|"
    pz.close()