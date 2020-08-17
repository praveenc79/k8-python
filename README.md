# k8-python

This is public repository home of a few python modules on top kubernetes pythin client libraries, to ->

1. Add / Delete fundamental kubernetes resources like deployment, service and ingress required to deploy a web application and exposing that to internet. 

2. It also has configuration module that is used to abstract configuration required to connect to kubernetes API server. 

3. These are basic components which can be used to build a pipeline that can dynamically deploy an individual branch into kubernetes so that application is put to integration and functional testing without merging to develop (main branch)

4. The invokation of these scripts can be easily hooked to a CICD tool like Jenkins which can be configured to react to PR against application source, by building that branch into a deployable artifact and then makes above calls to deploy that artifact into kubernetes and expose webapp to internal network using kubernetes service and ingress resource. 

5. Python module also has a function to add a rule so that same ingress can be used to expose new story branch using path based routing.
