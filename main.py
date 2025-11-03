from strands import Agent
from strands_tools import calculator

SYSTEM_PROMPT = """Você é um assistente útil especializado em cálculos matemáticos. 
Use a ferramenta de calculadora sempre que necessário para garantir precisão em suas respostas."""

MODEL_ID = "us.amazon.nova-premier-v1:0"  # Certifique-se de que você tem acesso a esse modelo no Bedrock

agent = Agent(
    system_prompt=SYSTEM_PROMPT,
    model=MODEL_ID,
    tools=[calculator]
)

agent("Quanto é 10^2/3*9")

