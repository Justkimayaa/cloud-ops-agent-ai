import requests
from langchain.tools import tool

PROMETHEUS_URL = "http://localhost:9090"

@tool
def get_pod_metrics(pod_name: str) -> str:
    """Get CPU and memory usage for a pod from Prometheus"""
    try:
        query = f'container_cpu_usage_seconds_total{{pod="{pod_name}"}}'
        resp = requests.get(
            f"{PROMETHEUS_URL}/api/v1/query",
            params={"query": query}
        )
        data = resp.json()
        return str(data['data']['result'])
    except Exception as e:
        return f"Error fetching metrics: {str(e)}"

@tool
def get_cluster_health() -> str:
    """Check overall cluster health from Prometheus"""
    try:
        resp = requests.get(f"{PROMETHEUS_URL}/-/healthy")
        return f"Prometheus status: {resp.text}"
    except Exception as e:
        return f"Error: {str(e)}"
