#
# THIS CODE AND INFORMATION ARE PROVIDED "AS IS" WITHOUT WARRANTY OF ANY KIND, EITHER EXPRESSED OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE IMPLIED WARRANTIES OF MERCHANTABILITY AND/OR FITNESS
# FOR A PARTICULAR PURPOSE. THIS CODE AND INFORMATION ARE NOT SUPPORTED BY XEBIALABS.
#

from __future__ import with_statement
from oracleSoaTests.Container import Container
from oracleSoaTests.Deployed import Deployed
from soa.runtime.ConnectionFactory import ConnectionFactory

from nose.tools import eq_

class TestConnectionFactory(object):

    def test_get_cf_target_from_container(self):
        container = Container("container_name")
        deployed = Deployed(container,"test1")
        connection_factory = ConnectionFactory(deployed)
        eq_(connection_factory.get_cf_target(), "container_name")

    def test_get_cf_target_from_deployed(self):
        container = Container("container_name")
        deployed = Deployed(container,"test1",target="target_name")
        connection_factory = ConnectionFactory(deployed)
        eq_(connection_factory.get_cf_target(), "target_name")

    def test_get_cf_id_from_deployed_name(self):
        container = Container("container_name")
        deployed = Deployed(container,"test1")
        connection_factory = ConnectionFactory(deployed)
        eq_(connection_factory.get_cf_id(), "test1")


    def test_get_cf_id_from_deployed_soa_id(self):
        container = Container("container_name")
        deployed = Deployed(container,"test1",soa_id="soa_id")
        connection_factory = ConnectionFactory(deployed)
        eq_(connection_factory.get_cf_id(), "soa_id")

