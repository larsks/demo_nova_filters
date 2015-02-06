from lxml import etree


class AddNetworkFilter (object):
    def filter(self, xml,
               instance=None,
               context=None):

        doc = etree.fromstring(xml)

        network = etree.fromstring('''<interface type="network">
          <source network="default"/>
          <model type="virtio"/>
        </interface>''')

        devices = doc.xpath('/domain/devices')[0]
        devices.append(network)

        return etree.tostring(doc, pretty_print=True)
