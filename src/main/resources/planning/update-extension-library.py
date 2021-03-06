#
# THIS CODE AND INFORMATION ARE PROVIDED "AS IS" WITHOUT WARRANTY OF ANY KIND, EITHER EXPRESSED OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE IMPLIED WARRANTIES OF MERCHANTABILITY AND/OR FITNESS
# FOR A PARTICULAR PURPOSE. THIS CODE AND INFORMATION ARE NOT SUPPORTED BY XEBIALABS.
#

from java.util import HashSet

def deployeds():
    result = HashSet()
    for _delta in deltas.deltas:
        depl = _delta.deployedOrPrevious
        current_container = depl.container
        if _delta.operation != "NOOP" and depl.type == "soa.ExtensionLibrary" and current_container.type in ("wls.SOAServer",'wls.SOACluster'):
            result.add(depl)
    return result

for deployed in deployeds():
    context.addStep(steps.os_script(
        description="Update extension lib to oracle.soa.ext.jar in %s" + deployed.getProperty("targetDirectory"),
        order=50,
        script="esb/updateExtensionLibrary.sh",
        freemarker_context={'directory': deployed.getProperty("targetDirectory"), 'antHomeDirectory':deployed.getProperty("AntHomeDirectory")},
        target_host=deployed.container.host))