#
# THIS CODE AND INFORMATION ARE PROVIDED "AS IS" WITHOUT WARRANTY OF ANY KIND, EITHER EXPRESSED OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE IMPLIED WARRANTIES OF MERCHANTABILITY AND/OR FITNESS
# FOR A PARTICULAR PURPOSE. THIS CODE AND INFORMATION ARE NOT SUPPORTED BY XEBIALABS.
#

from StringIO import StringIO
import sys
# Start main function

old_stdout = sys.stdout
redirectedStdout = StringIO()
sys.stdout = redirectedStdout
serverUrl="http://"+deployed.container.domain.host.address+":"+str(deployed.container.domain.soaPort)
if deployed.retire:
    print 'retire', deployed.soaServiceName
    sca_retireComposite(deployed.container.domain.host.address, str(deployed.container.domain.soaPort), deployed.container.domain.username, deployed.container.domain.password, deployed.soaServiceName, deployed.revisionVersion, partition=deployed.partition)
else:
    print 'undeploy', deployed.soaServiceName
    sca_undeployComposite(serverUrl, deployed.soaServiceName, deployed.revisionVersion, deployed.container.domain.username, deployed.container.domain.password, partition=deployed.partition)

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
if result != "0":
    raise Exception('Undeployment failed')