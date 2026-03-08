"""
📂 Módulo: src/azure_translator.py

Este módulo contém a função `translator_text` que integra o projeto
com o serviço Azure AI Translator.

Responsabilidade:
- Receber um texto em qualquer idioma
- Enviar para a API do Azure Translator
- Retornar o texto traduzido para o idioma de destino (pt-br)

Observações:
- As credenciais do Azure devem ser configuradas nas variáveis
  `subscription_key`, `endpoint` e `location`.
- Este módulo é utilizado pelo notebook tradutor_colab.ipynb
  e futuramente pode ser usado por outras partes do projeto
  para tradução de textos.
"""

import requests
import os

# 📌 Configurações da API

# IMPORTANTE:
# Para executar o projeto, substitua os valores abaixo pelas suas credenciais do Azure Translator.
subscription_key = "YOUR_AZURE_TRANSLATOR_KEY"
endpoint = "YOUR_AZURE_TRANSLATOR_ENDPOINT"
location = "YOUR_AZURE_REGION"
language_destination = "pt-br"

def translator_text(text, target_language):
    path = '/translate'
    constructed_url = endpoint + path
    headers = {
        'Ocp-Apim-Subscription-Key': subscription_key,
        'Ocp-Apim-Subscription-Region': location,
        'Content-type': 'application/json',
        'X-ClientTraceId': str(os.urandom(16))
    }

    body = [{
        'text': text
    }]
    params = {
        'api-version': '3.0',
        'to': target_language
    }

    request = requests.post(constructed_url, params=params, headers=headers, json=body)
    response = request.json()
    return response[0]['translations'][0]['text']