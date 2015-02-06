#!/bin/sh
#
# THIS CODE AND INFORMATION ARE PROVIDED "AS IS" WITHOUT WARRANTY OF ANY KIND, EITHER EXPRESSED OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE IMPLIED WARRANTIES OF MERCHANTABILITY AND/OR FITNESS
# FOR A PARTICULAR PURPOSE. THIS CODE AND INFORMATION ARE NOT SUPPORTED BY XEBIALABS.
#

<#include "/dda/common/ftl/directives.ftl">
<#assign userName = deployed.container.host.oracleInstallUser>
<#assign groupName = deployed.container.host.oracleInstallGroup>
<#assign tempDirectory = ((deployed.container.host.temporaryDirectoryPath)!'/tmp')>
<#assign sudoScriptPath = deployed.container.host.sudoSourceScript?matches("(.*/)([^/]+)$")?groups[1]>
<#assign sudoScriptName = deployed.container.host.sudoSourceScript?matches("(.*/)([^/]+)$")?groups[2]>
# 
# copy resources for ESB only if target file doesn't yet exist
#
echo 'Start modify-xslresources.sh'

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
   echo "sudo -u ${userName} ${deployed.container.host.sudoSourceScript} unzip -n $name -d $targetPath"
   sudo -u ${userName} ${deployed.container.host.sudoSourceScript} unzip -n $name -d $targetPath
   exit $?
else
  unzip -n $name -d $targetPath
fi
<#else>
  unzip -n $name -d $targetPath
</#if>
exit $?
   
