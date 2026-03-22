import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langgraph.prebuilt import create_react_agent

from tools.prometheus_tool import get_pod_metrics, get_cluster_health
from tools.kubectl_tool import restart_pod, scale_deployment, get_pod_status, get_pod_logs
from tools.notify_tool import send_alert, send_resolution

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

def create_agent():
    tools = [
        get_pod_metrics,
        get_cluster_health,
        restart_pod,
        scale_deployment,
        get_pod_status,
        get_pod_logs,
        send_alert,
        send_resolution
    ]

    llm = ChatGroq(
        model="llama-3.1-8b-instant",
        api_key=GROQ_API_KEY,
        temperature=0
    )

    agent_executor = create_react_agent(llm, tools)

    return agent_executor
