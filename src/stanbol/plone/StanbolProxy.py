'''
Created on Jul 22, 2011

@author: "Yannis Mazzer"
'''

from Products.Five import BrowserView
from jquery.pyproxy.plone import JQueryProxy, jquery
from stanbol.plone.utils import get_stanbol

class StanbolProxy(BrowserView):

    @jquery
    def engineProxy(self):
        jq = JQueryProxy()
        #stanbol = get_stanbol(self)
        #content = jq("#text_ifr").contents().find("#content").html()
        #res = stanbol.engines(payload=content, format="jsonld",
        #                     parsed=False)
        
        jq("#subject_keywords").append('test')
        return jq
    #

    @jquery  
    def contentHubProxy(self):
        jq = JQueryProxy()
        stanbol = get_stanbol(self)
        #TODO
        
        return jq
    #

    @jquery
    def engineCall(self):
        jq = JQueryProxy()
        return jq
    #

    @jquery
    def contentHubCall(self):
        jq = JQueryProxy()
        return jq
    #
