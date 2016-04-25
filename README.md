# XLD Oracle SOA Plugin #

[![Build Status](https://travis-ci.org/xebialabs-community/xld-oracle-soa-plugin.svg?branch=master)](https://travis-ci.org/xebialabs-community/xld-oracle-soa-plugin)

# Preface #

This document describes the functionality provided by the XLD Oracle SOA plugin.

See the **XL Deploy Reference Manual** for background information on XL Deploy and deployment concepts.

# Overview #

The XLD Oracle SOA plugin is a XL Deploy plugin that adds capability for deploying SOA composites to Oracle Fusion.

# History #

* v1.0.0 - jdewinne - First version 
* v1.4.0 - jdewinne	- Issue 8.
* v1.5.0 - gpaulissen - Issue 10: when deploying to MDS, first remove data in Oracle MDS before deployment (optional)

# Requirements #

* **Requirements**
	* **XL Deploy** 5.0.0 (from version 1.0.1+)
	* **XL Deploy** Weblogic plugin
	
	* Version 1.4.0 is incompatible with version 1.3.4 when using the `soa.MdsSOADeployableSpec` (See [Issue 8](https://github.com/xebialabs-community/xld-oracle-soa-plugin/issues/8))
	
	* The types `soa.CompositeSOADeployable` and `soa.CompositeSOADeployableSpec` are deprecated. From version 2.0.0. they will be removed. Use `soa.Composite` and `soa.CompositeSpec` instead.
	* The types `soa.MdsSOADeployable` and `soa.MdsSOADeployableSpec` are deprecated. From version 2.0.0. they will be removed. Use `soa.Mds` and `soa.MdsSpec` instead.

# Build #

$ ./gradlew -PjythonInterpreter=jython xlPlugin

or, if you are behind a proxy server:

$ ./gradlew -Dhttps.proxyHost=127.0.0.1 -Dhttps.proxyPort=3128 -PjythonInterpreter=jython xlPlugin
	
# Installation #

Place the plugin xldp file into your `SERVER_HOME/plugins` directory.

# Supported features #

* SOA Composite deployments
* SOA MDS deployments
* DB Connection Factory
* MQ Connection Factory
* FTP Connection Factory
* File Connection Factory
* JMS Connection Factory


# API #

* `soa.Mds`
	  * removeDataBeforeDeployment - `boolean` - Remove data in Oracle MDS before deployment.
	  * folderNameToRemove - `string` - The MDS folder name (below /apps) to remove.
