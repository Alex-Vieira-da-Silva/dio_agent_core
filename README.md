# 🧠 MeuAgente – Assistente de Cálculos com Bedrock AgentCore

Este projeto implementa um agente inteligente baseado em [Amazon Bedrock AgentCore](https://docs.aws.amazon.com/bedrock/latest/userguide/agents.html) e [Strands](https://github.com/aws/strands), especializado em cálculos matemáticos. Ele utiliza uma ferramenta de calculadora para garantir precisão nas respostas e pode ser implantado na infraestrutura da AWS via ECR.

---

## 📌 Objetivo

Criar um agente conversacional capaz de interpretar comandos matemáticos, realizar cálculos com precisão e responder de forma natural, utilizando a ferramenta `calculator` do pacote `strands_tools`.

---


## ⚙️ Requisitos

- Python 3.10+
- Docker
- AWS CLI configurado (`aws configure`)
- Permissões IAM adequadas
- `uv` e `bedrock-agentcore` instalados

---

## 📦 Instalação

1. Instale o `uv` e o AgentCore CLI:
   ```bash
   pip install uv
   uv pip install bedrock-agentcore
