# 🌐 Tradutor de Artigos Técnicos com AzureAI

![Python](https://img.shields.io/badge/Python-3.10-blue)
![Azure Translator](https://img.shields.io/badge/Azure-Translator-lightblue)
![Azure OpenAI](https://img.shields.io/badge/Azure-OpenAI-purple)
![Google Colab](https://img.shields.io/badge/Google-Colab-yellow)
![VSCode](https://img.shields.io/badge/VSCode-Editor-green)

---

## 📖 Sobre o Projeto
Este projeto demonstra como criar uma solução de tradução automática de artigos técnicos utilizando Microsoft Azure Translator e Azure OpenAI (GPT‑4o mini).  
O fluxo inclui tradução de frases, documentos Word e artigos da web, com saída final em Markdown para visualização.

---

## 🧩 Estrutura do Projeto

```text
tradutor-artigos-tecnicos-azureai/
│
├── README.md
│   → Documentação principal do projeto, com visão geral, instruções e objetivos.
│
├── requirements.txt
│   → Lista de dependências Python necessárias para executar o projeto.
│
├── notebooks/
│   ├── tradutor_colab.ipynb
│   │   → Notebook para testes e execução do tradutor de textos técnicos.
│   │
│   └── artigo_web_colab.ipynb
│       → Notebook focado na tradução de conteúdos retirados da web.
│
├── src/
│   ├── azure_translator.py
│   │   → Responsável pela integração com o serviço Azure Translator.
│   │
│   ├── azure_openai.py
│   │   → Implementa o uso do Azure OpenAI para processamento e refinamento do texto.
│   │
│   └── utils.py
│       → Funções auxiliares utilizadas no projeto.
│
├── docs/
│   ├── azure_translator_setup.md
│   │   → Guia de configuração do serviço Azure Translator.
│   │
│   ├── azure_openai_setup.md
│   │   → Passo a passo para configurar o Azure OpenAI.
│   │
│   └── guia_projeto.md
│       → Explicação detalhada do funcionamento geral do projeto.
│
└── .gitignore
    → Define arquivos e pastas que não devem ser enviados para o repositório.
```
## 🚀 Fluxo do Projeto

### 1️⃣ Configuração no Azure
- Criar recurso Translator (Free F0).  
- Criar recurso Azure OpenAI (Standard S0).  
- Implantar modelo GPT‑4o mini no Azure AI Studio (Global Standard).  

📸 *Exemplo de configuração no Azure:*  
![Configuração no Azure](docs/images/azure_setup.png)

---

### 2️⃣ Notebook no Colab
- Testar tradução de frases.  
- Traduzir documentos Word.  
- Traduzir artigos da web e gerar Markdown.  

📸 *Exemplo de execução no Colab:*  
![Execução no Colab](docs/images/colab_notebook.png)

---

### 3️⃣ Tradução de Documentos
- Função translate_document(path, target_language) para traduzir .docx.  
- Gera novo documento traduzido com sufixo _pt.docx.  

📸 *Exemplo de tradução de documento:*  
![Tradução de Documento](docs/images/docx_translation.png)

---

### 4️⃣ Extração e Tradução de Artigos da Web
- Web scraping com BeautifulSoup.  
- Tradução com Azure OpenAI via LangChain.  
- Exportação em Markdown.  

📸 *Exemplo de artigo traduzido:*  
![Artigo Traduzido](docs/images/web_article.png)

---

### 5️⃣ Visualização em Markdown
- Exportar artigo traduzido para .md.  
- Visualizar em site de Markdown Viewer.  
- Visualizar no VS Code com extensão de Markdown Preview.  

📸 *Exemplo de preview no VS Code:*  
![Preview no VS Code](docs/images/vscode_markdown.png)

---

## 🔧 Tecnologias Utilizadas
- Python  
- Google Colab  
- Microsoft Azure Translator  
- Microsoft Azure OpenAI (GPT‑4o mini)  
- BeautifulSoup4  
- LangChain  
- VS Code  

---

## ▶️ Como Rodar

1. Clone o repositório:
   ```bash
   git clone https://github.com/seu-usuario/tradutor-artigos-tecnicos-azureai.git
   cd tradutor-artigos-tecnicos-azureai
