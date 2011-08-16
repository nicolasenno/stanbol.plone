'''
Created on Jul 22, 2011

@author: "Yannis Mazzer"
'''

from Products.Five import BrowserView
from jquery.pyproxy.plone import JQueryProxy, jquery
from stanbol.plone.utils import get_stanbol
import hashlib

class StanbolProxy(BrowserView):
    """

    """
    def engineProxy(self, data, fat):
        """
        @param self
        @param data
        @param fat
        @return
        """
        stanbol = get_stanbol(self.context)
        res = stanbol.engines(payload=data, format=fat, parsed=False)
        return res
    #

    def contentHubProxy(self):
        """
        @param self
        @return
        """
        jq = JQueryProxy()
        stanbol = get_stanbol(self.context)
        #TODO
        
        return jq
    #
#

class EngineProxy(BrowserView):
    """
    Proxy View for calls to Apache Stanbol Engines
    """
    
    def __init__(self, context, request):
        """
        Initializes EngineProxy class
        @param self: the object itself
        @param context: the BrowserView context
        @param request: the Zope.View request
        """
        self.context = context
        self.request = request
    #

    def __call__(self):
        """
        Method called when EngineProxy is called
        @param self: the object itself
        @return: the Stanbol engines results in json format or an empty json
                object
        """
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
#

class ContentHubProxy(BrowserView):
    """
    Proxy View for calls to Apache Stanbol ContentHub
    """

    def __init__(self, context, request):
        """
        Initializes ContentHubProxy class
        @param self: the object itself
        @param context: the BrowserView context
        @param request: the Zope.View request
        """
        self.context = context
        self.request = request
    #

    def __call__(self):
        """
        Method called when ContentHubProxy is called
        @param self: the object itself
        @return: the Stanbol ContentHub results 
        """
        response = self.request.response
        stanbol = get_stanbol(self.context)
        #TODO
        return ''
    #
#

class EntityHubProxy(BrowserView):
    """
    Proxy View for calls to Apache Stanbol EntityHub
    """

    def __init__(self, context, request):
        """
        Initializes EntityHubProxy class
        @param self: the object itself
        @param context: the BrowserView context
        @param request: the Zope.View request
        """
        self.context = context
        self.request = request
    #

    def __call__(self):
        """
        Method called when EntityHubProxy is called
        @param self: the object itself
        @return: the Stanbol EntityHub results 
        """
        response = self.request.response
        stanbol = get_stanbol(self.context)
        #TODO
        return ''
    #
#

class EntityHubSiteProxy(BrowserView):
    """
    Proxy View for calls to Apache Stanbol EntityHub sites 
    """

    def __init__(self, context, request):
        """
        Initializes EntityHubProxy class
        @param self: the object itself
        @param context: the BrowserView context
        @param request: the Zope.View request
        """
        self.context = context
        self.request = request
    #

    def __call__(self):
        """
        Method called when EntityHubSiteProxy is called
        @param self: the object itself
        @return: the Stanbol EntityHub sites results 
        """
        response = self.request.response
        stanbol = get_stanbol(self.context)
        print self.request["URL"]
        req = self.request["URL"].split("sites")
        req = req[1]
        #TODO
        return ''
    #
#

class EntityHubSiteActions(BrowserView):
    """
    Actions available for Apache Stanbol EntityHub
    """

    def __init__(self, context, request):
        """
        @param self: the object itself
        @param context: the BrowserView context
        @param request: The Zope.View request
        """
        self.context = context
        self.request = request
    #

    def referenced(self):
        """
        @param self: the object itself
        @return the referenced sites by Apache Stanbol EntityHub
        """
        stanbol = get_stanbol(self.context)
        res = stanbol.entityHubSite().get_referenced_sites()
        return res
    #

    def entity(self):
        """
        @param self: the object itself
        @return informations on the requested entity
        """
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
        """
        @param self: the object itself
        @return the id of related entities
        """
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
        """
        @param self: the object itself
        @return the result of the json query
        """
        pass
    #
#

class StanbolCall(BrowserView):
    """
    View for Plone specific functionnalities
    """

    def contentHubCall(self, data):
        """
        @param self: the object itself
        @param data
        @return
        """
        jq = JQueryProxy()
        return jq
    #
    
    def engineCall(self, data):
        """
        Returns the graph resulting from processing data with Stanbol engine
        @param self: the object itself
        @param data: data to analyse
        @return the rdflib graph
        """
        stanbol = get_stanbol(self.context)
        res = stanbol.engines(payload=data, format='rdfxml', parsed=True)
        return res
    #

    @jquery
    def sparqlCall(self):
        """
        JQuery.PyProxy View for SparQL console
        @param self: the object itself
        @return sparql query result
        """
        jq = JQueryProxy()
        data = self.request.form.get('text')
        print self.request.stdin.getvalue()
        print data
        stanbol = get_stanbol(self.context)
        res = stanbol.sparql(data).body_string()
        print res
        res = res.replace('<', '&lt;')
        res = res.replace('>', '&gt;')
        jq("#sparql_result").html(res)

        return jq
    #

    @jquery
    def enhanceTags(self):
        """
        Enhances text by extracting keywords from it 
        @param self: the object itself
        @return keywords
        """
        jq = JQueryProxy()
        content = self.request.form.get('text')
        print content
        dir(content)
        res = self.engineCall(content)
        dir(res)
        cache = {}
        for t in res:
            if t[2].istitle():
                if t[2].datatype is None or t[2].datatype.endswith('string'):
                    cache[hashlib.md5(t[2].title()).hexdigest()] = t[2].title()
        tags=""
        for k in cache:
            test = jq("#subject input[value='"+cache[k]+"']")
            jq("#subject input[value='"+cache[k]+"']").attr('checked', 'checked')
            print test
            tags += cache[k] + '\n'
        print tags
        jq("#subject_keywords").html(tags)
        return jq   
    #

    @jquery
    def enhanceText(self):
        """
        Enhances text by adding rdfa metadata in it
        @param self: the object itself
        @return RDFa metadata
        """
        jq = JQueryProxy()
        content = self.request.form.get('text')
        res = self.engineProxy(content, 'jsonld')
        return res
    #
#
