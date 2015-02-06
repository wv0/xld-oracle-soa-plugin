#
# THIS CODE AND INFORMATION ARE PROVIDED "AS IS" WITHOUT WARRANTY OF ANY KIND, EITHER EXPRESSED OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE IMPLIED WARRANTIES OF MERCHANTABILITY AND/OR FITNESS
# FOR A PARTICULAR PURPOSE. THIS CODE AND INFORMATION ARE NOT SUPPORTED BY XEBIALABS.
#

print 'Deploying a messaging driver to cluster' + deployed.container.name 

cd('/Clusters/' + deployed.container.name)
servers = cmo.getServers()
domainRuntime() 

OutgoingMailServer = deployed.OutgoingMailServer
OutgoingMailServerPort = deployed.OutgoingMailServerPort
OutgoingMailServerSecurity = deployed.OutgoingMailServerSecurity
OutgoingDefaultFromAddress = deployed.OutgoingDefaultFromAddress
OutgoingUsername = deployed.OutgoingUsername
OutgoingPassword = deployed.OutgoingPassword

if OutgoingDefaultFromAddress is None:
	OutgoingDefaultFromAddress = ''
if OutgoingUsername is None:
	OutgoingUsername = ''
if OutgoingPassword is None:
	OutgoingPassword = ''

for server in servers:
	serverName = server.getName()
	print 'server: ' + server.getName()

	EmailDriverConfigobj = ObjectName('com.oracle.sdp.messaging:Location='+serverName +',name=EmailDriverConfig,type=SDPMessagingDriverConfig,Application=usermessagingdriver-email')
	print 'Common Properties for soa_server1'
	mbs.invoke(EmailDriverConfigobj,'setProperty',['OutgoingMailServer',OutgoingMailServer],['java.lang.String','java.lang.String'])
	mbs.invoke(EmailDriverConfigobj,'setProperty',['OutgoingMailServerPort',OutgoingMailServerPort],['java.lang.String','java.lang.String'])
	mbs.invoke(EmailDriverConfigobj,'setProperty',['OutgoingMailServerSecurity',OutgoingMailServerSecurity],['java.lang.String','java.lang.String'])
	mbs.invoke(EmailDriverConfigobj,'setProperty',['OutgoingDefaultFromAddr',OutgoingDefaultFromAddress],['java.lang.String','java.lang.String'])
	mbs.invoke(EmailDriverConfigobj,'setProperty',['OutgoingUsername',OutgoingUsername],['java.lang.String','java.lang.String'])
	mbs.invoke(EmailDriverConfigobj,'setProperty',['OutgoingPassword',OutgoingPassword],['java.lang.String','java.lang.String'])
	
	ASNSDriverEmailFromAddress = deployed.ASNSDriverEmailFromAddress
	ASNSDriverEmailRespondAddress = deployed.ASNSDriverEmailRespondAddress
	ASNSDriverEmailReplyAddress = deployed.ASNSDriverEmailReplyAddress 
	HWFMailerNotificationMode = deployed.HWFMailerNotificationMode
	WorkflowNotificationObj = ObjectName('oracle.as.soainfra.config:Location='+serverName +',name=human-workflow,type=HWFMailerConfig,Application=soa-infra')
	mbs.setAttribute(WorkflowNotificationObj, Attribute('ASNSDriverEmailFromAddress', ASNSDriverEmailFromAddress))
	mbs.setAttribute(WorkflowNotificationObj, Attribute('ASNSDriverEmailRespondAddress', ASNSDriverEmailRespondAddress))
	mbs.setAttribute(WorkflowNotificationObj, Attribute('ASNSDriverEmailReplyAddress', ASNSDriverEmailReplyAddress ))
	mbs.setAttribute(WorkflowNotificationObj, Attribute('HWFMailerNotificationMode', HWFMailerNotificationMode))
	
	ASNSDriverPropertyName = deployed.ASNSDriverPropertyName
	ASNSDriverPropertyValue = deployed.ASNSDriverPropertyValue
	ASNSDriverDriverName = deployed.ASNSDriverDriverName
	mbs.invoke(WorkflowNotificationObj,'setASNSDriver',[ASNSDriverPropertyName,ASNSDriverPropertyValue,ASNSDriverDriverName],['java.lang.String','java.lang.String','java.lang.String'])
	#
	# TODO: placeholders zijn nu voor 2 met name genoemde profielen. het zou mooi zijn om daar een lijst van te maken 
	#
	WNLEmailFromAddress = deployed.WNLEmailFromAddress
	EINTAKEEmailFromAddress = deployed.EINTAKEEmailFromAddress
	mbs.invoke(WorkflowNotificationObj,'setASNSDriver',['EmailFromAddress',WNLEmailFromAddress,'WNL'],['java.lang.String','java.lang.String','java.lang.String'])
	mbs.invoke(WorkflowNotificationObj,'setASNSDriver',['EmailFromAddress',EINTAKEEmailFromAddress,'EINTAKE'],['java.lang.String','java.lang.String','java.lang.String'])

print ('ok')
