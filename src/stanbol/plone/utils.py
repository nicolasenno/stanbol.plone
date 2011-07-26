from stanbol.client import Stanbol
from Products.CMFCore.utils import getToolByName
from zope.app.component.hooks import getSite
SERVER = 'http://localhost:8080/'

def get_stanbol(context):
    ptool = getToolByName(context, 'portal_properties')
    stanbolprops = ptool.get('stanbol_properties', None)
    #stanbolprops = getToolByName(context, 'portal_stanbol')
    #portal = getSite()
    #stanbolprops = portal.getProperty('portal_stanbol', '')
    if stanbolprops is not None:
        return Stanbol(stanbolprops.stanbol_server_address)
    return Stanbol(SERVER)
