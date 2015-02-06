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
serverUrl="http://"+deployed.container.host.address+":"+str(deployed.container.port)

if configplan and len(configplan) > 0:
 for jar in jars:
  print 'Deploying [' + jar + '] with plan [' + str(configplan) + '] on [' + serverUrl + ']'
  sca_deployComposite(serverUrl, jar, True, deployed.container.domain.username, deployed.container.domain.password, deployed.forcedefault == 'true', configplan[0], partition=deployed.partition)
else:
 for jar in jars:
  print 'Deploying [' + jar + '] on [' + serverUrl + ']'
  sca_deployComposite(serverUrl, jar, True, deployed.container.domain.username, deployed.container.domain.password, deployed.forcedefault == 'true', partition=deployed.partition)

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
