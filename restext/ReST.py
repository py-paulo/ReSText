from .style import ReSTStyle
from .restdoc import ReSTDocument


class ReSText(ReSTStyle):

    def __init__(self, doc, indent_width):
        ReSTStyle.__init__(self, doc, indent_width)
