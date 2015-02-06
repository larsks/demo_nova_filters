#!/usr/bin/env python

import setuptools

setuptools.setup(
    name="demo_nova_filters",
    version=1,
    packages=['demo_nova_filters'],
    entry_points={
        'nova.filters.domxml': [
            'prettyprint=demo_nova_filters.prettyprint:PrettyPrintFilter',
            'novideo=demo_nova_filters.novideo:NoVideoFilter',
            'addnetwork=demo_nova_filters.addnetwork:AddNetworkFilter',
        ]
    },
)
