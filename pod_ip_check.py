from kubernetes import client

class PodIpCheck:
    def __init__(self):
        pass
  
    def run_check(self):
        v1_client = client.CoreV1Api()
        ret = v1_client.list_pod_for_all_namespaces(watch=False)
        ips = {}
        passed = True
        for pod in ret.items:
            # Skip host network pods, we expect duplicates.
            if pod.spec.host_network:
                continue
            if pod.status.pod_ip in ips:
                passed = False
                other_pod = ips[pod.status.pod_ip]
                print("ERROR: Duplicate Pod IP Address: {}/{} -> {} and {}/{} -> {}".format(
                    pod.metadata.namespace, pod.metadata.name, pod.status.pod_ip,
                    other_pod.metadata.namespace, other_pod.metadata.name, other_pod.status.pod_ip))
            else:
                ips[pod.status.pod_ip] = pod
        return passed