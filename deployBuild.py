import kubernetes.client
from kubernetes.client.rest import ApiException
from pprint import pprint
import configk8
import libk8

##### BELOW ARE PRE-DEFINED / ALREADY CREATED objects for namespace /ALB -Ingress /security group / #######
##### These are one time objects needed per team. #########

INGRESS_NAME = "hello-ingress"
NAME_SPACE = "hello-namespace"
INGRESS_SG = "sg-01073d3e7a66d78e6"


############       Authentication #######

# create an instance of the API class
configuration = configk8.configuration
core_instance = kubernetes.client.CoreV1Api(kubernetes.client.ApiClient(configuration))
app_instance = kubernetes.client.AppsV1Api(kubernetes.client.ApiClient(configuration))
#config.load_kube_config()


####### ACTUAL CALLS TO DEPLOY NECESSARY COMONENTS FOR STORY BRANCH DEPLOYMENT #######

networking_v1_beta1_api = kubernetes.client.NetworkingV1beta1Api(kubernetes.client.ApiClient(configuration))
app_label_name = "hellowebapp"  #### THIS COULD BE STORY BRANCH NAME
service_name = "hello-service"  #### STORY BRANHC NAME - SERVICE

### STORY BRANCH NAME - DEPLOYMENT = DEPLOYMENT_NAME
### IMG_NAME = STORY_BRANCH_CONTAINER_IMAGE HERE = 'PCHAUDHARY/HELLOWEBAPP'
### APP_LABEL_NAME IS LABEL SELECTOR TO BE USED TO ASSOCIATE SERVICE WITH DEPLOYMENT
deployment_object = libk8.create_deployment_object("hello-deployment",app_label_name,"pchaudhary/hellowebapp",8080,app_label_name)
print ("Create Deployment Object")
libk8.create_deployment(app_instance,deployment_object,NAME_SPACE)
#create_ingress(networking_v1_beta1_api,ingress_name,ns_name,bs_name,app_label_name,ingress_sg)
#core_instance,service_name,ns_name,label_name,target_port,protocol,type
print ("Create service ---  ")
#### 8080 HERE IS PORT WHERE APP IN CONTIANER IS LISTENING
libk8.create_service(core_instance,service_name,NAME_SPACE,app_label_name,8080,"TCP","NodePort")
print ("Update ingress ---  ")
# path = hello here LIKE IN MY CASE ITS ALB/HELLO/
libk8.update_ingress(networking_v1_beta1_api,INGRESS_NAME,NAME_SPACE,service_name,"hello","add")
