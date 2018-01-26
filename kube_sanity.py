#!/bin/python

import argparse
import sys
from kubernetes import config

from service_ip_check import ServiceIpCheck
from pod_ip_check import PodIpCheck

def main():
    parser = argparse.ArgumentParser(description='Sanity check your cluster')
    parser.add_argument('--use-cluster-config', type=bool, default=False,
        help='use an in cluster configuration to talk to the apiserver')
    args = parser.parse_args()
    
    if args.use_cluster_config:
        config.load_incluster_config()
    else:
        config.load_kube_config()

    # Add new checks here.
    checks = [PodIpCheck(), ServiceIpCheck()]

    print("Starting check.")
    errors = False
    for check in checks:
        if not check.run_check():
            errors = True

    if not errors:
        print("No errors found.")
        sys.exit(0)
    sys.exit(1)

if __name__ == "__main__":
    main()
