#
# THIS CODE AND INFORMATION ARE PROVIDED "AS IS" WITHOUT WARRANTY OF ANY KIND, EITHER EXPRESSED OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE IMPLIED WARRANTIES OF MERCHANTABILITY AND/OR FITNESS
# FOR A PARTICULAR PURPOSE. THIS CODE AND INFORMATION ARE NOT SUPPORTED BY XEBIALABS.
#

deployedName=str(deployed.name)

print 'Processing [' + deployedName + ']'

theurl=str(deployed.file)

print 'Deploying [' + theurl + '] to [' +  deployed.container.name + ']'

if deployed.container.type == "wls.Cluster":
    server_name=deployed.container.servers[0].name
else:
    server_name=deployed.container.name


importMetadata(application='soa-infra', server = server_name ,fromLocation= theurl ,docs='/**', remote='true')
