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
        theurl=str(self.deployed.file.path)
        print "Using url %s" % theurl
        jars=glob.glob(theurl+'/*.jar')
        if self.deployed.revisionVersion:
            print "Using deployed revision version %s" % self.deployed.revisionVersion
            return self.deployed.revisionVersion
        if jars and len(jars) > 0:
            jar_name = jars[0]
            print "Using jar name revision version %s" % jar_name
            return jar_name[jar_name.find("_rev")+len("_rev"):jar_name.rfind(".jar")]

soa_helper = SoaHelper(deployed)
revision_version = soa_helper.find_revision()
deployed.values["revisionVersion"] = revision_version