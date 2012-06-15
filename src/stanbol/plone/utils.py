from stanbol.client import Stanbol
from Products.CMFCore.utils import getToolByName
from zope.app.component.hooks import getSite
from zope.component import getUtility
from plone.registry.interfaces import IRegistry
from stanbol.plone.controlpanel.stanbolpanel import IStanbolSettings

def get_stanbol(context):
    """
    Utilitary function to access Stanbol preferences
    """
    registry = getUtility(IRegistry)
    settings = registry.forInterface(IStanbolSettings)
    protocol = settings.stanbol_server_protocol
    host = settings.stanbol_server_host
    port = settings.stanbol_server_port
    return Stanbol(protocol+'://'+host+':'+str(port))

