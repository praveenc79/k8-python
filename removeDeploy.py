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
networking_v1_beta1_api = kubernetes.client.NetworkingV1beta1Api(kubernetes.client.ApiClient(configuration))

libk8.delete_deployment(app_instance,"hello-deployment",NAME_SPACE)
libk8.delete_service(core_instance,"hello-service",NAME_SPACE)
libk8.update_ingress(networking_v1_beta1_api,INGRESS_NAME,NAME_SPACE,"hello-service","hello","remove")
