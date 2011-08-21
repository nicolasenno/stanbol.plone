from stanbol.client import Stanbol
from Products.CMFCore.utils import getToolByName
from zope.app.component.hooks import getSite
#from zope.component import getUtility
#from plone.registry.interfaces import IRegistry
#from stanbol.plone.controlpanel.stanbol import IStanbolSchema
SERVER = 'http://localhost:8888/'

def get_stanbol(context):
    """
    Utilitary function to access Stanbol preferences
    """
    #registry = getUtility(IRegistry)
    #settings = registry.forInterface(IStanbolSchema)
    #ptool = getToolByName(context, 'portal_properties')
    #stanbolprops = ptool.get('stanbol_properties', None)
    ##stanbolprops = getToolByName(context, 'portal_stanbol')
    ##portal = getSite()
    ##stanbolprops = portal.getProperty('portal_stanbol', '')
    #if stanbolprops is not None:
    #    return Stanbol(stanbolprops.stanbol_server_address)
    return Stanbol(SERVER)

