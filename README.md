## KubeSanity

_Trust, but verify_

A sanity checker for Kubernetes.

It runs across a cluster and performs some basic (really basic for now) sanity checking assertions.

### Usage

```sh
docker run -v ${HOME}/.kube:/root/.kube:ro brendanburns/kubesanity:0.1.0
```

### Current Assertions
   * Pod IP Duplication: Validates no two pods have the same IP
   * Service IP Duplication: Validates no two services have the same IP

### Contributing

Please do. New assertions should be easy to add, they all should implement the assertion
contract. See the existing assertions for examples.

### License
Distributed under the [MIT](https://opensource.org/licenses/MIT) License.
