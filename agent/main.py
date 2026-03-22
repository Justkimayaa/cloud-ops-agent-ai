import time
import os
from dotenv import load_dotenv
from agent.agent_core import create_agent
from audit.logger import log_decision

load_dotenv()

def run_agent():
    print("=== Autonomous Cloud Ops Agent Started ===")
    print("Monitoring Kubernetes cluster every 60 seconds...")
    print("Press Ctrl+C to stop\n")

    agent_executor = create_agent()

    while True:
        try:
            print(f"\n--- Checking cluster health ---")
            
            result = agent_executor.invoke({
                "messages": [
                    {"role": "user", "content": "Check status of all pods in default namespace and report what you find"}
                ]
            })

            print(f"Agent result: {result}")

            log_decision(
                observation="Cluster health check",
                reasoning=str(result),
                action="Automated health check",
                outcome="Check completed"
            )

            print("\n--- Check complete. Waiting 60 seconds ---\n")
            time.sleep(60)

        except KeyboardInterrupt:
            print("\n=== Agent stopped by user ===")
            break
        except Exception as e:
            print(f"Agent error: {str(e)}")
            print("Retrying in 30 seconds...")
            time.sleep(30)

if __name__ == "__main__":
    run_agent()
