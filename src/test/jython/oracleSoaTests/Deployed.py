#
# THIS CODE AND INFORMATION ARE PROVIDED "AS IS" WITHOUT WARRANTY OF ANY KIND, EITHER EXPRESSED OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE IMPLIED WARRANTIES OF MERCHANTABILITY AND/OR FITNESS
# FOR A PARTICULAR PURPOSE. THIS CODE AND INFORMATION ARE NOT SUPPORTED BY XEBIALABS.
#

class Deployed(object):

    def __init__(self, container, name, target="", soa_id="", file="", revision_version=""):
        self.container = container
        self.name = name
        self.Target = target
        self.SoaId = soa_id
        self.file = file
        self.revisionVersion = revision_version