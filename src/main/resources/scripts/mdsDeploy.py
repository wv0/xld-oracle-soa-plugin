import glob

deployedName=str(deployed.name)

print 'Processing [' + deployedName + ']'

serverUrl="http://" + deployed.container.domain.host.address + ":" + str(deployed.container. port)

theurl=str(deployed.file)

print 'Deploying [' + theurl + '] to [' +  serverUrl + ']'

importMetadata(application='soa-infra', server = deployed.container.name ,fromLocation= theurl ,docs='/**', remote='true')
#sca_deployComposite(serverUrl, deployed.file, true, deployed.container.domain.username, deployed.container.domain.password, deployed.forcedefault == 'true')
