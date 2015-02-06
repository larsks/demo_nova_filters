from lxml import etree

class NoVideoFilter (object):
    def filter(self, xml,
               instance=None,
               context=None):

        doc = etree.fromstring(xml)
        for ele in doc.xpath('//video') + doc.xpath('//graphics'):
            ele.getparent().remove(ele)

        return etree.tostring(doc, pretty_print=True)

