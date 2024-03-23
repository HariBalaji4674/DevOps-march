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
  - Cloud Watch Logs

***What Should we Monitor**
- Node Health *taints & Tolerations*
- Cluster CPU/Memory *Resource Quotas & Requests and Limits*
- Pod Health Checks *Probes,Readiness Probes,Liveliness Probes*
- Networking *Kube-Proxy,Ingress,Service,LoadBalancers*
- Applications Logs *Side-Car Patterns*

`ELK`


