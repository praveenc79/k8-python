from __future__ import print_function
import time
import kubernetes.client
from kubernetes.client.rest import ApiException
from pprint import pprint

# Configure API key authorization: BearerToken
configuration = kubernetes.client.Configuration()
# API Key is invalidated by inserting *** and removing real characters in original API Key
# Long string left for how it actually looks
configuration.api_key['authorization'] ='eyJhbGciOiJSUzI1NiI******************HhLenVlSmIzSlhEX0hWbVpFbn**********************************************Jlcm5ldGVzL3NlcnZpY2VhY2NvdW50Iiwia3ViZXJuZXRlcy5pby9zZXJ2aWNlYWNjb3VudC9uYW1lc3BhY2UiOiJkZWZhdWx0Iiwia3ViZXJuZXRlcy5pby9zZXJ2aWNlYWNjb3VudC9zZWNyZXQubmFtZSI6InRlc3RzZXJ2aWNlYWNjb3VudC10b2tlbi1ueGNqMiIsImt1YmVybmV0ZXMuaW8vc2VydmljZWFjY291bnQvc2VydmljZS1hY2NvdW50Lm5hbWUiOiJ0ZXN0c2VydmljZWFjY291bnQiLCJrdWJlcm5ldGVzLmlvL3NlcnZpY2VhY2NvdW50L3NlcnZpY2UtYWNjb3VudC51aWQiOiIwYjM2ZTBjNC0wYWE5LTRlZTMtYTJlNC03ZDE0ZDJmOTRhOGQiLCJzdWIiOiJzeXN0ZW06c2V*******************************************Z2qR3KEKBX4WRNKv96JrvVD0t1KpKEGVdMLwTAoErq6s89p4kMRHwpwWknSFU9IsE9cn9VJY2YD1vjjy10UVvewEwf0xeP-UdJX6uEKECu28X8scWWEqGt8CNoEbISAkuQHU_-WCrgf71TVWwhnHTXrbGCYx3FTtbw0eGi_sBtA3x1GD1wrF00CPNIjZzfgi6IziVAeLbsZoKe9usgzCoEhz4l-1CeNI53iVn58AHRQHBO5l7xWgH-xZIKN_DpHq2SfycN5CCSrv53gCdyLfjAGmH_dJWmB4PMgPIprwEhfhBfeuK0L3MLajvH05mBljcPKKzZaVp0Bpy7DXtBw'
configuration.api_key_prefix['authorization'] = 'Bearer'

# API end point is updated so its just the representation of API server end point
configuration.host = 'https://BE1799***************************.gr7.us-west-2.eks.amazonaws.com'
## ca1.crt file is supposed to be gegrated following
### https://stackoverflow.com/questions/57158867/having-problem-in-authenticating-kubernetes-python-client
### The one in this project is kept just for demonstration purpose and not a vald certificate file.
configuration.ssl_ca_cert = 'ca1.crt'

# create an instance of the API class
api_instance = kubernetes.client.AdmissionregistrationApi(kubernetes.client.ApiClient(configuration))
try:
    api_response = api_instance.get_api_group()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdmissionregistrationApi->get_api_group: %s\n" % e)
