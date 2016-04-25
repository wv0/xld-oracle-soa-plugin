#
# THIS CODE AND INFORMATION ARE PROVIDED "AS IS" WITHOUT WARRANTY OF ANY KIND, EITHER EXPRESSED OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE IMPLIED WARRANTIES OF MERCHANTABILITY AND/OR FITNESS
# FOR A PARTICULAR PURPOSE. THIS CODE AND INFORMATION ARE NOT SUPPORTED BY XEBIALABS.
#

from StringIO import StringIO
import sys

def mdsUndeploy(deployed_object):
	"""
	Function to undeploy a Meta Data Store
	"""
	print 'Processing undeployment of [' + str(deployed_object.name) + ']'

	if deployed_object.container.type == "wls.Cluster":
		server = deployed_object.container.servers[0]
	else:
		server = deployed_object.container

        if deployed_object.folderNameToRemove:
                folder_name_to_remove = deployed_object.folderNameToRemove
        else:
                folder_name_to_remove = deployed_object.name
	
	print '...Undeploying folder [' + folder_name_to_remove + '] from [' + server.name + ']'
	
	server_url = "http://" + server.host.address + ":" + str(server.port)

        old_stdout = sys.stdout
        redirected_stdout = StringIO()
        sys.stdout = redirected_stdout

	sca_removeSharedData(server_url, folder_name_to_remove, deployed_object.container.domain.username, deployed_object.container.domain.password)

        sys.stdout = old_stdout
        result_string = redirected_stdout.getvalue()
        print result_string
        if ('---->Removing shared data success.' in result_string) or ('---->Remove shared data success.' in result_string):
                print 'mdsUndeploy: OK'
        else:
                print 'mdsUndeploy: FAIL' # do not raise an exception since otherwise un undeploy may fail when there is nothing deployed (anymore)

# main	
mdsUndeploy(deployed)
