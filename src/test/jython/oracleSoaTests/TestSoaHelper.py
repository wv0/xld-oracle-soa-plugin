#
# THIS CODE AND INFORMATION ARE PROVIDED "AS IS" WITHOUT WARRANTY OF ANY KIND, EITHER EXPRESSED OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE IMPLIED WARRANTIES OF MERCHANTABILITY AND/OR FITNESS
# FOR A PARTICULAR PURPOSE. THIS CODE AND INFORMATION ARE NOT SUPPORTED BY XEBIALABS.
#


from oracleSoaTests.Deployed import Deployed
from soa.runtime.SoaHelper import SoaHelper

from nose.tools import eq_

import os

class TestSoaHelper(object):

    def test_get_revsion_from_file(self):
        jar_name = "sca_testing_rev1.2.3.jar"
        path = "/tmp/soatest/%s" % jar_name
        basedir = os.path.dirname(path)
        if not os.path.exists(basedir):
            os.makedirs(basedir)
        open(path, 'a').close()
        deployed = Deployed(None,"test1",file=basedir)
        soa_helper = SoaHelper(deployed)
        eq_(soa_helper.find_revision(), "1.2.3")

    def test_get_revsion_with_defined_number(self):
        deployed = Deployed(None,"test1",revision_version="1.2.3")
        soa_helper = SoaHelper(deployed)
        eq_(soa_helper.find_revision(), "1.2.3")