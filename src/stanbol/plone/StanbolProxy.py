'''
Created on Jul 22, 2011

@author: "Yannis Mazzer"
'''
from jquery.pyproxy.plone import JQueryProxy, jquery
from stanbol.plone.utils import get_stanbol

class StanbolProxy():
    
    def __init__(self):
        self.jq = JQueryProxy()
        self.stanbol = get_stanbol(self)
    #

    @jquery
    def engineProxy(self):
        content = self.jq("#text_ifr").contents().find("#content").html()
        res = self.stanbol.engines(payload=content, format="jsonld",
                             parsed=False)
        
        self.jq("#subject_keywords").append(res);
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
