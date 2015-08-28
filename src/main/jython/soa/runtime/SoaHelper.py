#
# THIS CODE AND INFORMATION ARE PROVIDED "AS IS" WITHOUT WARRANTY OF ANY KIND, EITHER EXPRESSED OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE IMPLIED WARRANTIES OF MERCHANTABILITY AND/OR FITNESS
# FOR A PARTICULAR PURPOSE. THIS CODE AND INFORMATION ARE NOT SUPPORTED BY XEBIALABS.
#

import glob

class SoaHelper(object):

    def __init__(self, deployed):
        self.deployed = deployed

    def find_revision(self):
        theurl=str(self.deployed.file)
        jars=glob.glob(theurl+'/*.jar')
        if self.deployed.revisionVersion:
            return self.deployed.revisionVersion
        if jars and len(jars) > 0:
            jar_name = jars[0]
            return jar_name[jar_name.find("_rev")+len("_rev"):jar_name.rfind(".jar")]