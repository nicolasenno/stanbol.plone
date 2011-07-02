from stanbol.client import Stanbol
from Products.CMFCore.utils import getToolByName
SERVER = 'http://localhost:8080/'

def get_stanbol(context):
    ptool = getToolByName(context, 'portal_properties')
    stanbolprops = ptool.get('stanbol_properties', None)
    if stanbolprops is not None:
        return Stanbol(stanbolprops.getProperty('server'))
    return Stanbol(SERVER)
