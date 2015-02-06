#!/bin/sh
#
# THIS CODE AND INFORMATION ARE PROVIDED "AS IS" WITHOUT WARRANTY OF ANY KIND, EITHER EXPRESSED OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE IMPLIED WARRANTIES OF MERCHANTABILITY AND/OR FITNESS
# FOR A PARTICULAR PURPOSE. THIS CODE AND INFORMATION ARE NOT SUPPORTED BY XEBIALABS.
#

<#include "/dda/common/ftl/directives.ftl">
<#assign userName = deployed.container.host.oracleUser>
<#assign groupName = deployed.container.host.oracleGroup>
<#assign tempDirectory = ((deployed.container.host.temporaryDirectoryPath)!'/tmp')>
<#assign sudoScriptPath = deployed.container.host.sudoSourceScript?matches("(.*/)([^/]+)$")?groups[1]>
<#assign sudoScriptName = deployed.container.host.sudoSourceScript?matches("(.*/)([^/]+)$")?groups[2]>
# 
# remove resources for ESB
#
echo 'Start destroy-xslresources.sh'

targetPath=${deployed.targetPath}
name=${deployed.name}

echo 'targetPath: ' $targetPath
echo 'name: ' $name

<#if deployed.container.host.useSudo>
if [ $(basename $0) != ${sudoScriptName} ]; then
   chmod -R 777 $PWD/..
   if [ ! -f "${deployed.container.host.sudoSourceScript}" ]; then
      sudo -u ${userName} cp ./${sudoScriptName} ${sudoScriptPath}
      if [ $? -ne 0 ]; then
         echo "Unable to install sudo sourcing file."
         echo "Exiting installation."
         exit 1
      fi
   fi
   echo "sudo -u ${userName} ${deployed.container.host.sudoSourceScript} rm -rf $targetPath"
   sudo -u ${userName} ${deployed.container.host.sudoSourceScript} rm -rf $targetPath
   exit $?
else
   rm -rf $targetPath
fi
<#else>
   rm -rf $targetPath
</#if>
exit $?
   
