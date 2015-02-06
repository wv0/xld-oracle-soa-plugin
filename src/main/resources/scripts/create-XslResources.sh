#!/bin/sh
<#include "/dda/common/ftl/directives.ftl">
<#assign userName = deployed.container.host.oracleUser>
<#assign groupName = deployed.container.host.oracleGroup>
<#assign tempDirectory = ((deployed.container.host.temporaryDirectoryPath)!'/tmp')>
<#assign sudoScriptPath = deployed.container.host.sudoSourceScript?matches("(.*/)([^/]+)$")?groups[1]>
<#assign sudoScriptName = deployed.container.host.sudoSourceScript?matches("(.*/)([^/]+)$")?groups[2]>
<#assign ddaLocation = ((step.remoteWorkingDirectory.path)!'/tmp/dda')>
# 
# copy resources for ESB only if target file doesn't yet exist
#
echo 'Start create-xslresources.sh'

targetPath=${deployed.targetPath}
name=${deployed.name}
createTargetPath=${deployed.createTargetPath}

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
   echo "sudo -u ${userName} ${deployed.container.host.sudoSourceScript} ${ddaLocation}/$(basename $0)"
   sudo -u ${userName} ${deployed.container.host.sudoSourceScript} ${ddaLocation}/$(basename $0) 
   exit $?
else 
   echo "create targetpath"
   # create directory if needed
   if [ "$createTargetPath" == "true"  ]; then
       ${ddaLocation}/createDirectory.sh $targetPath
   fi
   ${ddaLocation}/unzipResources.sh $targetPath
   exit $?
fi
<#else>
     if [ "$createTargetPath" == "true"  ]; then
         createDirectory.sh $targetPath
     fi
  unzipResources.sh $targetPath
</#if>
exit $?
   
