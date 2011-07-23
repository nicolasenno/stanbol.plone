'''
Created on Jul 22, 2011

@author: "Yannis Mazzer"
'''
from stanbol.client import Stanbol
from jquery.pyproxy.plone import JQueryProxy, jquery
from stanbol.plone.utils import get_stanbol

class StanbolProxy():
    
    @jquery
    def __init__(self):
        self.jq = JQueryProxy()
        pass
    #

    @jquery
    def engineProxy(self):
        return self.jq
    #

    @jquery  
    def contentHubProxy(self):
        return self.jq
    #

    @jquery
    def engineCall(self):
        return self.jq
    #

    @jquery
    def contentHubCall(self):
        return self.jq
    #
