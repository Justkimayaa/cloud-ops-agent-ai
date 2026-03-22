import subprocess
from langchain.tools import tool

@tool
def restart_pod(namespace: str, deployment: str) -> str:
    """Restart a Kubernetes deployment"""
    try:
        result = subprocess.run([
            "kubectl", "rollout", "restart",
            f"deployment/{deployment}",
            "-n", namespace
        ], capture_output=True, text=True)
        return result.stdout or result.stderr
    except Exception as e:
        return f"Error restarting pod: {str(e)}"

@tool
def scale_deployment(namespace: str, deployment: str, replicas: int) -> str:
    """Scale a deployment to given replica count"""
    try:
        result = subprocess.run([
            "kubectl", "scale",
            f"deployment/{deployment}",
            f"--replicas={replicas}",
            "-n", namespace
        ], capture_output=True, text=True)
        return result.stdout or result.stderr
    except Exception as e:
        return f"Error scaling deployment: {str(e)}"

@tool
def get_pod_status(namespace: str) -> str:
    """Get status of all pods in a namespace"""
    try:
        result = subprocess.run([
            "kubectl", "get", "pods",
            "-n", namespace,
            "-o", "wide"
        ], capture_output=True, text=True)
        return result.stdout or result.stderr
    except Exception as e:
        return f"Error getting pod status: {str(e)}"

@tool
def get_pod_logs(namespace: str, pod_name: str) -> str:
    """Get logs from a specific pod"""
    try:
        result = subprocess.run([
            "kubectl", "logs",
            pod_name,
            "-n", namespace,
            "--tail=50"
        ], capture_output=True, text=True)
        return result.stdout or result.stderr
    except Exception as e:
        return f"Error getting logs: {str(e)}"

