#
# THIS CODE AND INFORMATION ARE PROVIDED "AS IS" WITHOUT WARRANTY OF ANY KIND, EITHER EXPRESSED OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE IMPLIED WARRANTIES OF MERCHANTABILITY AND/OR FITNESS
# FOR A PARTICULAR PURPOSE. THIS CODE AND INFORMATION ARE NOT SUPPORTED BY XEBIALABS.
#

import sys

class SoaHelper(object):

    def __init__(self, container):
        self.container = container

    def check_host_property(self):
        if self.container.type == "wls.Cluster":
            if self.container.servers is None or self.container.servers.pop().host is None:
                return False
        else:
            if self.container.host is None:
                return False
        return True

soa_helper = SoaHelper(container)
host_defined = soa_helper.check_host_property()

if host_defined:
    print "Container with name %s has its host property defined.\n" % container.name
else:
    print "Container with name %s has its host property NOT defined.\n" % container.name
    print "In order to deploy a SOA Composite, each container (wls.Server or wls.Cluster) it gets deployed to, should have its host property defined."
    sys.exit(1)