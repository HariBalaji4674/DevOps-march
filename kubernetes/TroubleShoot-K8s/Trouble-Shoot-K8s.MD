# SRE & Signals

**Two Main Points**
- Focused on ensuring Uptime and Availability
- Monitoring and Designing Systems with resiliency in mind

***SRE Concepts***
- Move Fast Without break anything
- Automation
- Error Budgeting
- Setting SLAs SLOs and SLIs
- Service Level Agreements
- Service Level Objectives
- Service Level Indicators

***Monitoring 4 Golden Sinals***
- Latency
- Traffic
- Errors
- Saturation

***Incident Responses***
- Incident Command System
- Designed Roles
- Keep Record
- Document Everything and Every Issues

**Logging and Monitoring**
- ***Tools***
  - Prometheus --> Monitoring the Metrics(CPU,memory)
  - Grafana --> DashBoards Creations(Based on TSDB)
  - ELK --> Elastic Logstash & Kibana (Logs Management)
  - Cloud Watch Logs *`Cloud Native Solutions`*

**What Should We Monitor**
- Node Health *`taints & Tolerations`*
- Cluster CPU/Memory *`Resource Quotas & Requests and Limits`*
- Pod Health Checks *`Probes,Readiness Probes,Liveliness Probes`*
- Networking *`Kube-Proxy,Ingress,Service,LoadBalancers`*
- Applications Logs *`Side-Car Patterns`*

## Most Important Topics in Kubernetes
- ### *1: Pod Health Check*
  - **Probes**
    - Liveness Probe
    - Readiness Probe
    - Start-Up Probe
  - **Types of Probes**
    - Command `Will be Check using Command internally insdie the container`
    - HTTP Request
    - TCP Request
    - gRPC Request
**Liveness Probe**
- Liveness probe is powerful way to recover from application failures
- There are three conditions
  - **initialDelaySeconds** `This tells kubelet to wait for 5 seconds before performing the first probe`
  - **periodSeconds** `this field specifies that kubelet should perform a liveness probe every 5 seconds`
  - **cat /tmp/health** `This check the health of conatiner if returns 0 kubelet will decide conatiner is alive and healthy`
- ***Commands To Check the Status***
  - kubectl get pods
  - kubectl describe pod liveness-exec
  - kubectl get events

**Restart Policy For Pods**
- *By default the kubernetes will restart the pod always when it fails to run the containers*
- *We can change the `Restart Policy` we can change the setting and make a pod to fail
- #### There are 3 Type of Restart Policies
  - **Always** --> `Default Setting In K8s`
  - **OnFailure** --> `K8s will restart when container exits on non-zero exit status`
  - **Never** --> `K8s will never automatically restart the container if exits`

***Restart Policy Yaml File***
```
apiVersion: v1
kind: Pod
metadata:
  name: mypod
spec:
  restartPolicy: Always
  containers:
  - name: mycontainer
    image: myimage:latest
```







