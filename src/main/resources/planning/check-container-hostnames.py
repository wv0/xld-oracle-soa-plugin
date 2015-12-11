#
# THIS CODE AND INFORMATION ARE PROVIDED "AS IS" WITHOUT WARRANTY OF ANY KIND, EITHER EXPRESSED OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE IMPLIED WARRANTIES OF MERCHANTABILITY AND/OR FITNESS
# FOR A PARTICULAR PURPOSE. THIS CODE AND INFORMATION ARE NOT SUPPORTED BY XEBIALABS.
#

from java.util import HashSet

def containers():
    result = HashSet()
    for _delta in specification.deltas:
        depl = _delta.deployedOrPrevious
        current_container = depl.container
        if depl.type == "soa.CompositeSOADeployable" and current_container.type in ("wls.Server",'wls.Cluster'):
            result.add(current_container)
    return result

for container in containers():
    context.addStep(steps.jython(
        description="Check if container %s has a host set" % container.name,
        order=1,
        script="scripts/checkHostProperty.py",
        jython_context= {"container": container}
        ))