import glob

print 'undeploy ' + deployed.name

thefolder=str(deployed.name) 

serverUrl="http://"+deployed.container.domain.host.address+":"+str(deployed.container.domain.port)
sca_removeSharedData(serverUrl, thefolder, deployed.container.domain.username, deployed.container.domain.password)