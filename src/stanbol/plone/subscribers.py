from stanbol.plone.utils import get_stanbol
from Products.statusmessages.interfaces import IStatusMessage

def stanbol_indexer_handler(obj, event):
    obj._stanbol_enhancements = None
    stanbol = get_stanbol(obj)
    try:           
        obj._stanbol_enhancements = stanbol.engines(obj.SearchableText(), 'rdfjson')
    except Exception, e:
        msg = "Problem while using Stanbol server for automatic "+\
              "enhancement.\n%s" % str(e)
        IStatusMessage(obj.REQUEST).addStatusMessage(msg, type='error')