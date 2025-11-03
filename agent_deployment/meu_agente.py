from strands import Agent
from strands_tools import calculator
from bedrock_agentcore.runtime import BedrockAgentCoreApp

app = BedrockAgentCoreApp()

@app.entrypoint
def invoke(payload, context):
    SYSTEM_PROMPT = """Você é um assistente útil especializado em cálculos matemáticos.
    Use a ferramenta de calculadora sempre que necessário para garantir precisão em suas respostas."""

    agent = Agent(
        system_prompt=SYSTEM_PROMPT,
        tools=[calculator]
    )

    prompt = payload.get("prompt", "Olá")
    result = agent(prompt)

    return {
        "response": result.message.get("content", [{}])[0].get("text", str(result))
    }

if __name__ == "__main__":
    app.run()