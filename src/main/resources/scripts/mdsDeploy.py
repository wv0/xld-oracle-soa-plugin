#
# THIS CODE AND INFORMATION ARE PROVIDED "AS IS" WITHOUT WARRANTY OF ANY KIND, EITHER EXPRESSED OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE IMPLIED WARRANTIES OF MERCHANTABILITY AND/OR FITNESS
# FOR A PARTICULAR PURPOSE. THIS CODE AND INFORMATION ARE NOT SUPPORTED BY XEBIALABS.
#

# gpaulissen  10-FEB-2016  Remove data if necessary (copied from mdsUndeploy.py)

if deployed.removeDataBeforeDeployment:
    print 'undeploy ' + deployed.name
    thefolder=str(deployed.name) 
    serverUrl="http://"+deployed.container.domain.host.address+":"+str(deployed.container.domain.port)
    sca_removeSharedData(serverUrl, thefolder, deployed.container.domain.username, deployed.container.domain.password)


# gpaulissen  10-FEB-2016  Normal deployment continues here    

deployedName=str(deployed.name)

print 'Processing [' + deployedName + ']'

theurl=str(deployed.file)

print 'Deploying [' + theurl + '] to [' +  deployed.container.name + ']'

if deployed.container.type == "wls.Cluster":
    server_name=deployed.container.servers[0].name
else:
    server_name=deployed.container.name


importMetadata(application='soa-infra', server = server_name ,fromLocation= theurl ,docs='/**', remote='true')
