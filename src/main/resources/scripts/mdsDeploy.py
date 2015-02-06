#
# THIS CODE AND INFORMATION ARE PROVIDED "AS IS" WITHOUT WARRANTY OF ANY KIND, EITHER EXPRESSED OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE IMPLIED WARRANTIES OF MERCHANTABILITY AND/OR FITNESS
# FOR A PARTICULAR PURPOSE. THIS CODE AND INFORMATION ARE NOT SUPPORTED BY XEBIALABS.
#

import glob

deployedName=str(deployed.name)

print 'Processing [' + deployedName + ']'

serverUrl="http://" + deployed.container.domain.host.address + ":" + str(deployed.container. port)

theurl=str(deployed.file)

print 'Deploying [' + theurl + '] to [' +  serverUrl + ']'

importMetadata(application='soa-infra', server = deployed.container.name ,fromLocation= theurl ,docs='/**', remote='true')
#sca_deployComposite(serverUrl, deployed.file, true, deployed.container.domain.username, deployed.container.domain.password, deployed.forcedefault == 'true')
