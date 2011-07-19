from zope.interface import Interface

class Layer(Interface):
    """Layer Marker"""
    
def initialize(context):
    """Initializer called when used as a Zope 2 product."""