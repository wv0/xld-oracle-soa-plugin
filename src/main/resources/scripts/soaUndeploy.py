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
    print 'Attribute soaServiceName does not exist, using deployed.Name: ' + deployed.Name

print 'undeploy ' + deployedServiceName

old_stdout = sys.stdout
redirectedStdout = StringIO()
sys.stdout = redirectedStdout
serverUrl="http://"+deployed.container.domain.host.address+":"+str(deployed.container.domain.soaPort)
sca_undeployComposite(serverUrl, deployedServiceName, deployed.revisionVersion, deployed.container.domain.username, deployed.container.domain.password, partition=deployed.partition)
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