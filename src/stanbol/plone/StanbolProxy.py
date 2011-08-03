'''
Created on Jul 22, 2011

@author: "Yannis Mazzer"
'''

from Products.Five import BrowserView
from jquery.pyproxy.plone import JQueryProxy, jquery
from stanbol.plone.utils import get_stanbol
import json
import hashlib
from rdflib.graph import Graph

class StanbolProxy(BrowserView):

    @jquery
    def engineProxy(self):
        jq = JQueryProxy()
        stanbol = get_stanbol(self.context)
        #content = jq("#text_ifr").contents().find("#content").html()
        content=self.request.form.get('text')
        res = stanbol.engines(payload=content, format='rdfxml', parsed=True)
	#g = Graph(res)
        cache = {}
        for t in res:
            print t[2].title()
            if t[2].istitle():
                if t[2].datatype is None or t[2].datatype.endswith('string'):
                    cache[hashlib.md5(t[2].title()).hexdigest()] = t[2].title()
        tags=""
        for k in cache:
            tags += cache[k] + '\n'
        jq("#subject_keywords").html(tags)
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
