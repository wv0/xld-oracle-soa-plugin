package com.xebialabs.deployit.contributor;

import java.io.IOException;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

import com.xebialabs.deployit.plugin.api.deployment.execution.DeploymentStep;
import com.xebialabs.deployit.plugin.api.deployment.planning.Contributor;
import com.xebialabs.deployit.plugin.api.deployment.planning.DeploymentPlanningContext;
import com.xebialabs.deployit.plugin.api.deployment.specification.Delta;
import com.xebialabs.deployit.plugin.api.deployment.specification.Deltas;
import com.xebialabs.deployit.plugin.api.deployment.specification.Operation;
import com.xebialabs.deployit.plugin.api.udm.Deployed;
import com.xebialabs.deployit.plugin.generic.step.ScriptExecutionStep;
import com.xebialabs.deployit.plugin.overthere.Host;
import com.xebialabs.deployit.plugin.wls.container.WlsContainer;

/**
 * Contributor adds the execution of an ant script for deploying soa extension libs. 
 * 
 */

public class SoaExtensionLibContributor {

	@Contributor
	public void addDeploymentTestStep(Deltas deltas, DeploymentPlanningContext result) throws IOException {
		List<Delta> deltasToDeploy = findDeltas(deltas.getDeltas());

		for (Delta delta : deltasToDeploy) {
			if (delta.getOperation() == Operation.CREATE || delta.getOperation() == Operation.MODIFY || delta.getOperation() == Operation.DESTROY) {
                Deployed<?,?> deployed = delta.getDeployed();
                if(delta.getOperation() == Operation.DESTROY) {
                    deployed= delta.getPrevious();
                }

				WlsContainer container =  (WlsContainer) deployed.getContainer();

				result.addStep(getUpdateExtensionLibCheckStep(container, deployed));
				// Only update the extension libs once (is only once needed).
				break;
			}
		}
	}

	

	private List<Delta> findDeltas(List<Delta> deltas) {
		List<Delta> deltasEsbsToSOAServer = new ArrayList<Delta>();
		for (Delta delta : deltas) {
			if (delta.getOperation() == Operation.CREATE || delta.getOperation() == Operation.MODIFY || delta.getOperation() == Operation.DESTROY) {
                Deployed<?, ?> deployed = delta.getDeployed();
                if(delta.getOperation() == Operation.DESTROY) {
                    deployed= delta.getPrevious();
                }
				if (deployed.getType().toString().equals("soa.ExtensionLibrary") && deployed.getContainer().getType().toString().equals("wls.SOAServer")) {
					deltasEsbsToSOAServer.add(delta);
				}
				if (deployed.getType().toString().equals("soa.ExtensionLibrary") && deployed.getContainer().getType().toString().equals("wls.SOACluster")) {
					deltasEsbsToSOAServer.add(delta);
				}
			}
		}
		return deltasEsbsToSOAServer;
	}
	
	private ScriptExecutionStep getUpdateExtensionLibCheckStep(WlsContainer container,
			Deployed<?, ?> deployed) throws IOException {
		String description = "Update extension lib to oracle.soa.ext.jar in " + deployed.getProperty("targetDirectory");
		Map<String, Object> scriptVariables = new HashMap<String, Object>();
		scriptVariables.put("directory", deployed.getProperty("targetDirectory"));
		scriptVariables.put("antHomeDirectory", deployed.getProperty("AntHomeDirectory"));
		Host destHost = (Host)container.getProperty("host");
		ScriptExecutionStep scriptExecutionStep = new ScriptExecutionStep(50, "esb/updateExtensionLibrary.sh", destHost,scriptVariables, description);
		return scriptExecutionStep;
	}
	
}

