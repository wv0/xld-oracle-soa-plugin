#
# THIS CODE AND INFORMATION ARE PROVIDED "AS IS" WITHOUT WARRANTY OF ANY KIND, EITHER EXPRESSED OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE IMPLIED WARRANTIES OF MERCHANTABILITY AND/OR FITNESS
# FOR A PARTICULAR PURPOSE. THIS CODE AND INFORMATION ARE NOT SUPPORTED BY XEBIALABS.
#

import glob

print 'undeploy ' + deployed.name

thefolder=str(deployed.name) 

serverUrl="http://"+deployed.container.domain.host.address+":"+str(deployed.container.domain.port)
sca_removeSharedData(serverUrl, thefolder, deployed.container.domain.username, deployed.container.domain.password)