Bebeto - Assistente Virtual Inteligente 🤖
Descrição
Bebeto é um assistente virtual inteligente construído com Streamlit e LangChain que pode interagir com diferentes tipos de conteúdo (sites, vídeos do YouTube, PDFs, CSVs e arquivos de texto) e responder perguntas usando modelos de linguagem como Groq e OpenAI.

Funcionalidades
📄 Suporte a múltiplos tipos de arquivo:
Sites
Vídeos do YouTube
PDFs
CSVs
Arquivos TXT

🤖 Modelos de IA disponíveis:

Groq:
- llama-3.3-70b-versatile
- gemma2-9b-it
- mixtral-8x7b-32768
  
OpenAI:
- GPT-4o-mini
- GPT-4o
- o1 and o1-mini

Como usar
- Na interface:
  - Selecione o tipo de arquivo que deseja processar
  - Faça upload do arquivo ou forneça a URL
  - Escolha o modelo de IA
  - Forneça sua API key
  - Clique em "Inicializar Bebeto"
  - Comece a conversar!

Requisitos
- Python 3.6+
- Streamlit
- LangChain
- Outras dependências listadas em requirements.txt
  
Estrutura do Projeto:

  projeto_completo/
  ├── app.py              # Arquivo principal
  ├── loaders.py          # Funções para carregar diferentes tipos de arquivo
  └── requirements.txt    # Dependências do projeto

  Interface Web do Bebeto:
![Captura de tela 2025-01-19 143554](https://github.com/user-attachments/assets/dd3cf976-a3ea-4b8c-91a9-8b77c537e6aa)

