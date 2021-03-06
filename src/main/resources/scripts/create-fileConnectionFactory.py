#
# THIS CODE AND INFORMATION ARE PROVIDED "AS IS" WITHOUT WARRANTY OF ANY KIND, EITHER EXPRESSED OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE IMPLIED WARRANTIES OF MERCHANTABILITY AND/OR FITNESS
# FOR A PARTICULAR PURPOSE. THIS CODE AND INFORMATION ARE NOT SUPPORTED BY XEBIALABS.
#

import os.path

#
# Redeploy app
def redeploy_app(appName, planPath, targets):
	print 'Redeploying application [' + appName + '] with deployment plan [' + planPath + ']'
	cd('/AppDeployments/' + appName + '/Targets')
	redeploy(appName, planPath, targets=targets)

# Change deployment plan
def make_deployment_plan_variable(wlstPlan, name, value, xpath, moduleOverrideName, moduleDescriptorName='META-INF/weblogic-ra.xml', origin='planbased'):
	print 'Modifying plan:'
	print '- name: [' + name + ']'
	print '- value: [' + value + ']'
	print '- xpath: [' + xpath + ']'
	print '- moduleOverrideName: [' + moduleOverrideName + ']'
	print '- moduleDescriptorName: [' + moduleDescriptorName + ']'
	print '- origin: [' + origin + ']'
	
	while wlstPlan.getVariableAssignment(name, moduleOverrideName, moduleDescriptorName):
		wlstPlan.destroyVariableAssignment(name, moduleOverrideName, moduleDescriptorName)
	
	while wlstPlan.getVariable(name):
		wlstPlan.destroyVariable(name)
	
	variableAssignment = wlstPlan.createVariableAssignment(name, moduleOverrideName, moduleDescriptorName)
	variableAssignment.setXpath(xpath)
	variableAssignment.setOrigin(origin)
	wlstPlan.createVariable(name, value)
	
# Check plan path, if non existing, create an empty version
def checkPlanPath(planPath):
	print 'Checking plan:'
	print '- path: [' + planPath + ']'
	if os.path.isfile(planPath):
		print 'Plan exists. OK.'
		return
	print 'Plan does not exist - creating'
	dir = os.path.dirname(planPath)
	if not os.path.exists(dir):
		os.makedirs(dir)
	
# Start main function
connectAndEdit()

connection_factory = ConnectionFactory(deployed)
cfId = connection_factory.get_cf_id()
cfTarget = connection_factory.get_cf_target()


cfAppName = deployed.appName
cfAppPath = deployed.AppPath
cfJndiName = deployed.jndiName
cfPlanPath = deployed.PlanPath
fileControlDir = deployed.controlDir

checkPlanPath(cfPlanPath)

print 'Loading application [' + cfAppName + '] with deployment plan [' + cfPlanPath + ']'
plan = loadApplication(cfAppPath, cfPlanPath)
	
print 'Updating deployment plan with connection factory: [' + cfJndiName + ']'
make_deployment_plan_variable(plan, 'ConnectionInstance_' + cfJndiName + '_JNDIName_' + cfId, cfJndiName, '/weblogic-connector/outbound-resource-adapter/connection-definition-group/[connection-factory-interface="javax.resource.cci.ConnectionFactory"]/connection-instance/[jndi-name="' + cfJndiName + '"]/jndi-name', moduleOverrideName=cfAppName + '.rar')
make_deployment_plan_variable(plan, 'ConfigProperty_host_Value_' + cfId, fileControlDir, '/weblogic-connector/outbound-resource-adapter/connection-definition-group/[connection-factory-interface="javax.resource.cci.ConnectionFactory"]/connection-instance/[jndi-name="' + cfJndiName + '"]/connection-properties/properties/property/[name="controlDir"]/value', moduleOverrideName=cfAppName + '.rar')

plan.save();

#save()
#activate(block='true')
	
print 'Redeploying app: [' + cfAppName + ']'
redeploy_app(cfAppName, cfPlanPath, cfTarget)

saveAndExit()
