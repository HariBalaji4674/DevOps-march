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
- ### *1: Monitoring Containers & Pod Health Check using Probes*
  - Container Health `Auto Healing Features`
    - Automaticall Restart unhealthy containers
    - Active Monitoring
      - Pull The status Healthy or not
      - Application Status should be accurate

  - **Probes**
    - Liveness Probe
    - Readiness Probe
    - Start-Up Probe

  - **Types of Probes Health Check**
    - Command `Will be Check using Command internally insdie the container`
    - HTTP Probe
    - TCP Probe
    - gRPC Probe
    - Exec Probe

  - **Errors Occur when Porbes Failed**
    - CrashLoopBackOff
    - ImageCrashLoopBackOff
    - Err Image Pull

## **Liveness Probe**

- Liveness probe is powerful way to recover from application failures
- Liveness probe allow you to automatically determine container application health state
- By Default K8s will only consider a conatiner to be terminated if the container process stops
- Liveness probe allows you to customize this detection mechanism and make it more flexible

**Liveness Probe Yaml manifest**

```
apiVersion: v1
kind: Pod
metadata:
  name: mypod
spec:
  containers:
  - name: mycontainer
    image: myimage:latest
    livenessProbe:
      httpGet:
        path: /healthz
        port: 8080
      initialDelaySeconds: 10
      periodSeconds: 30
```

## **Startup Probe**
- Similar to the liveness probe however liveness probe run constantly on a schedule , startup probe run at container startup and stop running once they succeed
- They are used to determins when the application has successfully started
- Start Up probe are especially useful for some legacy applications that can have long startup times

***Start Up Probe Yaml Manifest***
```
apiVersion: v1
kind: Pod
metadata:
  name: mypod
spec:
  containers:
  - name: mycontainer
    image: myimage:latest
    startupProbe:
      httpGet:
        path: /ready
        port: 8080
      failureThreshold: 30
      periodSeconds: 10
      initialDelaySeconds: 10
```

## **Readiness Probe**
- Readiness Probe are used to determine when a conatiner is ready to accept requests
- When you have a service backed by multiple container endpoints user traffic will not be sent to a particular pod until its containers have passes all the readiness checks defined by their readiness probes
- Use Reainess probe to prevent user traffic from beings ent to pods that are still in the process of starting up

***Readiness Probe Yaml Manifest***
```
apiVersion: v1
kind: Pod
metadata:
  name: mypod
spec:
  containers:
  - name: mycontainer
    image: myimage:latest
    readinessProbe:
      httpGet:
        path: /healthz
        port: 8080
      initialDelaySeconds: 10
      periodSeconds: 5
```

- ### *Liveness Probe three conditions*

  - **initialDelaySeconds** `This tells kubelet to wait for 5 seconds before performing the first probe`
  - **periodSeconds** `this field specifies that kubelet should perform a liveness probe every 5 seconds`
  - **cat /tmp/health** `This check the health of conatiner if returns 0 kubelet will decide conatiner is alive and healthy`
  - **failureThreshold** `indicates the number of consecutive failures required to consider the probe as failed.`

- ***Commands To Check the Status***
  - kubectl get pods
  - kubectl describe pod liveness-exec
  - kubectl get events

**Restart Policy For Pods**
- *By default the kubernetes will restart the pod always when it fails to run the containers*
- *We can change the `Restart Policy` we can change the setting and make a pod to fail*
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

***Rolling Updates in Kubernetes***
- *Important Fields*
  - targetGracePeriodSeconds `K8s should wait before forcefully terminating a pod during a rolling update or deletion`


## NameSpaces and Resource Quotas

### **Resource Quotas**
- Resource Management is Most important in Kubernetes if the cluster is shared
- *Why?*
  - To Avoid any Particular team or person to consume all the resources
- To Achieve this you can divide everyone to use their own namespaces
  - With This you can enable resource Quota and ObjectQuota

## Insufficient Node Resources










