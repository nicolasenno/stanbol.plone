'''
Created on Jul 22, 2011

@author: "Yannis Mazzer"
'''

from Products.Five import BrowserView
from jquery.pyproxy.plone import JQueryProxy, jquery
from stanbol.plone.utils import get_stanbol
import hashlib

class StanbolProxy(BrowserView):

    def engineProxy(self, data, fat):
        stanbol = get_stanbol(self.context)
        res = stanbol.engines(payload=data, format=fat, parsed=False)
        return res
    #

    def contentHubProxy(self):
        jq = JQueryProxy()
        stanbol = get_stanbol(self.context)
        #TODO
        
        return jq
    #


class EngineProxy(BrowserView):
    
    def __init__(self, context, request):
        self.context = context
        self.request = request
    #

    def __call__(self):
        response = self.request.response
        stanbol = get_stanbol(self.context) 
        print self.request.form
        try:
            print self.request.form['data']
            data = self.request.form['data']
            res = stanbol.engines(payload=data, format="jsonld", parsed=False)
            print res
            return res
        except:
            return '{}' 
    #

class ContentHubProxy(BrowserView):

    def __init__(self, context, request):
        self.context = context
        self.request = request
    #

    def __call__(self):
        response = self.request.response
        stanbol = get_stanbol(self.context)
        #TODO
        return ''
    #

class EntityHubProxy(BrowserView):

    def __init__(self, context, request):
        self.context = context
        self.request = request
    #

    def __call__(self):
        response = self.request.response
        stanbol = get_stanbol(self.context)
        #TODO
        return ''
    #

class EntityHubSiteProxy(BrowserView):

    def __init__(self, context, request):
        self.context = context
        self.request = request
    #

    def __call__(self):
        response = self.request.response
        stanbol = get_stanbol(self.context)
        print self.request["URL"]
        req = self.request["URL"].split("sites")
        req = req[1]
        #TODO
        return ''
    #

class EntityHubSiteActions(BrowserView):

    def __init__(self, context, request):
        self.context = context
        self.request = request
    #

    def referenced(self):
        stanbol = get_stanbol(self.context)
        res = stanbol.entityHubSite().get_referenced_sites()
        return res
    #

    def entity(self):
        if self.request.form['id']:
            uri = self.request.form['id']
        stanbol = get_stanbol(self.context)
        ehs = stanbol.entityHubSite
        if uri:
            res = ehs.get_entity(uri)
            return res
        return '' 
    #

    def find(self):
        # name
        # field
        # lang
        # limit
        # offset
        
        stanbol = get_stanbol(self.context)
        ehs = stanbol.entityHubSite
        try:
            _name = self.request.form['name']
        except:
            _name = None
        try:
            _field = self.request.form['field']
        except:
            _field = None
        try:
            _lang = self.request.form['lang']
        except:
            _lang = None
        try:
            _limit = self.request.form['limit']
        except:
            _limit = None
        try:
            _offset = self.request.form['offset']
        except:
            _offset = None

        res = ehs.find(
            name = _name, 
            field=_field, 
            lang=_lang, 
            limit=_limit,
            offset=_offset
        )
        return res
    #

    def query(self):
        pass
    #
#

class StanbolCall(BrowserView):

    def contentHubCall(self, data):
        jq = JQueryProxy()
        return jq
    #
    
    def engineCall(self, data):
        '''
        returns the graph resulting from processing data with Stanbol engine
        '''
        stanbol = get_stanbol(self.context)
        res = stanbol.engines(payload=data, format='rdfxml', parsed=True)
        return res
    #

    @jquery
    def enhanceTags(self):
        '''enhances text by extracting keywords from it '''
        jq = JQueryProxy()
        content = self.request.form.get('text')
        res = self.engineCall(content)
        cache = {}
        for t in res:
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
    def enhanceText(self):
        '''enhances text by adding rdfa metadata in it'''
        jq = JQueryProxy()
        content = self.request.form.get('text')
        res = self.engineProxy(content, 'jsonld')
        return res
    #

