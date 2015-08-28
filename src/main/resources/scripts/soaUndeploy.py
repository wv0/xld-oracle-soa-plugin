#
# THIS CODE AND INFORMATION ARE PROVIDED "AS IS" WITHOUT WARRANTY OF ANY KIND, EITHER EXPRESSED OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE IMPLIED WARRANTIES OF MERCHANTABILITY AND/OR FITNESS
# FOR A PARTICULAR PURPOSE. THIS CODE AND INFORMATION ARE NOT SUPPORTED BY XEBIALABS.
#

from StringIO import StringIO
import sys
# Start main function

# Backward compatibility: in services gedeployed met de 0.0.1 versie van deze plugin
# is serviceName niet gedefinieerd.
try:
    deployedServiceName = deployed.soaServiceName
    if deployedServiceName == "":
    	deployedServiceName = deployed.name
    print 'set deployedServiceName to ' + deployedServiceName
except AttributeError:
    deployedServiceName = deployed.name
    print 'Attribute soaServiceName does not exist, using deployed.name: ' + deployed.name

print 'undeploy ' + deployedServiceName

revision_version = SoaHelper(deployed).find_revision()

old_stdout = sys.stdout
redirectedStdout = StringIO()
sys.stdout = redirectedStdout
serverUrl="http://"+deployed.container.domain.host.address+":"+str(deployed.container.domain.soaPort)
sca_undeployComposite(serverUrl, deployedServiceName, revision_version, deployed.container.domain.username, deployed.container.domain.password, partition=deployed.partition)
sys.stdout = old_stdout
result_string = redirectedStdout.getvalue()
print 'result'
print result_string
result = "-1"
if ('---->Undeploying composite' in result_string) and ('success.' in result_string):
	print 'ok'
	result = "0"
else:
	print 'error'

print "DEPLOYIT-DAEMON-EXIT-VALUE: " + result