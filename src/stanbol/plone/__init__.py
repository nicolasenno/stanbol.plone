from zope.interface import Interface
from zope.i18nmessageid import MessageFactory
StanbolMessageFactory = MessageFactory(u'stanbol.plone')


class Layer(Interface):
    """Layer Marker"""
    
def initialize(context):
    """Initializer called when used as a Zope 2 product."""