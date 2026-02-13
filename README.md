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

tradutor-artigos-tecnicos-azureai/
│
├── README.md
│   └── Documentação principal do projeto
│
├── requirements.txt
│   └── Dependências Python necessárias para execução
│
├── notebooks/
│   ├── tradutor_colab.ipynb
│   │   └── Testes de tradução de frases e documentos
│   │
│   └── artigo_web_colab.ipynb
│       └── Extração e tradução de artigos da web
│
├── src/
│   ├── azure_translator.py
│   │   └── Integração com serviço Azure Translator
│   │
│   ├── azure_openai.py
│   │   └── Integração com modelos de IA para tradução e processamento textual
│   │
│   └── utils.py
│       └── Funções auxiliares do projeto
│
├── docs/
│   ├── azure_translator_setup.md
│   │   └── Guia de configuração do serviço Translator
│   │
│   ├── azure_openai_setup.md
│   │   └── Guia de configuração do Azure OpenAI
│   │
│   └── guia_projeto.md
│       └── Documentação geral do sistema
│
└── .gitignore
    └── Arquivos ignorados pelo versionamento
    
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
