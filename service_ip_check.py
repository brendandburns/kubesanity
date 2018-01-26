from kubernetes import client

class ServiceIpCheck:
    def __init__(self):
        pass

    def run_check(self):
        v1_client = client.CoreV1Api()
        ret = v1_client.list_service_for_all_namespaces(watch=False)
        ips = {}
        passed = True
        for svc in ret.items:
            if svc.spec.cluster_ip in ips:
                passed = False
                other_svc = ips[svc.spec.cluster_ip]
                print("ERROR: Duplicate Service IP Address: {}/{} -> {} and {}/{} -> {}".format(
                    svc.metadata.namespace, svc.metadata.name, svc.spec.cluster_ip,
                    other_svc.metadata.namespace, other_svc.metadata.name, other_svc.spec.cluster_ip))
            else:
                ips[svc.spec.cluster_ip] = svc
        return passed