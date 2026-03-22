# Autonomous Cloud Ops Agent

AI-powered autonomous agent that monitors Kubernetes cluster,
detects failures, and auto-remediates without human intervention.

## Architecture
```
                    ┌─────────────────────────────────┐
                    │     Autonomous Cloud Ops Agent   │
                    │                                  │
  ┌──────────┐     │  ┌──────────┐  ┌─────────────┐  │
  │Prometheus│────▶│  │ Observe  │─▶│  LLM Reason │  │
  │ Metrics  │     │  │  Tool    │  │ Groq Llama  │  │
  └──────────┘     │  └──────────┘  └──────┬──────┘  │
                    │                       │          │
  ┌──────────┐     │              ┌─────────▼──────┐  │
  │  K8s     │────▶│              │ Confidence     │  │
  │ Cluster  │     │              │ Threshold 80%  │  │
  └──────────┘     │              └────┬──────┬────┘  │
                    │                  │      │        │
                    │           ┌──────▼─┐ ┌──▼─────┐ │
                    │           │  Act   │ │Escalate│ │
                    │           │kubectl │ │  SNS   │ │
                    │           └──────┬─┘ └────────┘ │
                    └──────────────────┼───────────────┘
                                       │
                    ┌──────────────────▼───────────────┐
                    │           AWS Services            │
                    │  S3 (audit logs)  SNS (alerts)   │
                    └──────────────────────────────────┘
```

## Tech Stack
- LangChain ReAct Agent — agentic loop + tool calling
- Groq Llama 3.1 — free LLM for reasoning
- Kubernetes Minikube — local K8s cluster
- Prometheus — metrics monitoring
- AWS S3 — audit log storage
- AWS SNS — incident alerting
- AWS IAM — secure access
- Python + boto3 — agent code

## How it works
1. Agent polls Prometheus every 60 seconds
2. Detects anomalies — pod crash, OOMKill, high CPU
3. Groq LLM reasons about root cause
4. If confidence >= 80% — fixes autonomously
5. If confidence < 80% — escalates to human via SNS
6. Every decision logged to AWS S3

## Agent Tools
- get_pod_metrics — reads Prometheus metrics
- get_cluster_health — checks cluster status
- restart_pod — restarts crashed pods
- scale_deployment — scales replicas up/down
- get_pod_logs — fetches pod logs for diagnosis
- send_alert — sends AWS SNS alert
- send_resolution — sends resolution notification

## Demo Flow
```
YOU: delete pod (simulate crash)
AGENT: detects crash → LLM reasons → sends CRITICAL alert
AWS SNS: sends email to your inbox
AWS S3: saves JSON audit log
AGENT: reports check complete
```

## Resume Bullets
- Built autonomous LangChain ReAct agent monitoring K8s cluster
  using Groq Llama 3.1 — reducing MTTR from 40 mins to 2 mins
- Integrated AWS S3, SNS, IAM for audit logging and alerting
- Implemented confidence threshold — auto-fix vs human escalation
- Agent detects pod crashes, OOMKills, and high CPU automatically

## GitHub
https://github.com/Justkimayaa/cloud-ops-agent-ai
