from lxml import etree

class PrettyPrintFilter (object):
    def filter(self, xml,
               instance=None,
               context=None):

        doc = etree.fromstring(xml)
        return etree.tostring(doc, pretty_print=True)
