#
# THIS CODE AND INFORMATION ARE PROVIDED "AS IS" WITHOUT WARRANTY OF ANY KIND, EITHER EXPRESSED OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE IMPLIED WARRANTIES OF MERCHANTABILITY AND/OR FITNESS
# FOR A PARTICULAR PURPOSE. THIS CODE AND INFORMATION ARE NOT SUPPORTED BY XEBIALABS.
#

import glob
from StringIO import StringIO
from datetime import datetime
import sys

#XLDeploy connects to the admin server of the domain to which the managed server belongs to
#To create a partition we need to connect to the managed server directly
disconnect()

# Start main function
result = "-1"

print 'Processing [' + str(deployed.name) + ']'


# TODO: replace with wrapper function
old_stdout = sys.stdout
redirectedStdout = StringIO()
sys.stdout = redirectedStdout

if deployed.container.type == "wls.Cluster":
    managedServerUrl="t3://"+deployed.container.servers[0].host.address+":"+str(deployed.container.servers[0].port)
else:
    managedServerUrl="t3://"+deployed.container.host.address+":"+str(deployed.container.port)

connect(deployed.container.domain.username, deployed.container.domain.password, managedServerUrl)

print 'Creating partition [' + deployed.partition + "] on [" + managedServerUrl + ']'

sca_createPartition(partitionName = deployed.partition)
sys.stdout = old_stdout
result_string = redirectedStdout.getvalue()
if 'Exception:' in result_string and 'already exists' in result_string:
	print 'Partition already exists, ignoring'

disconnect()

theurl=str(deployed.file)

jars=glob.glob(theurl+'/*.jar')

configplan=glob.glob(theurl+'/*.xml')

old_stdout = sys.stdout
redirectedStdout = StringIO()
sys.stdout = redirectedStdout

if deployed.container.type == "wls.Cluster":
    server_url="t3://"+deployed.container.servers[0].host.address+":"+str(deployed.container.servers[0].port)
else:
    server_url="t3://"+deployed.container.host.address+":"+str(deployed.container.port)


if configplan and len(configplan) > 0:
 for jar in jars:
  print 'Deploying [' + jar + '] with plan [' + str(configplan) + '] on [' + server_url + ']'
  sca_deployComposite(server_url, jar, True, deployed.container.domain.username, deployed.container.domain.password, deployed.forcedefault == 'true', configplan[0], partition=deployed.partition)
else:
 for jar in jars:
  print 'Deploying [' + jar + '] on [' + server_url + ']'
  sca_deployComposite(server_url, jar, True, deployed.container.domain.username, deployed.container.domain.password, deployed.forcedefault == 'true', partition=deployed.partition)

sys.stdout = old_stdout

result_string = redirectedStdout.getvalue()
print 'result'
print result_string
if '--->Deploying composite success.' in result_string:
	print 'ok'
	result = "0"
else:
	print 'error'

print "DEPLOYIT-DAEMON-EXIT-VALUE: " + result
