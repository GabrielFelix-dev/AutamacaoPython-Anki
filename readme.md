# Anki Automation Web App 🚀

Uma aplicação web desenvolvida em Python (com Streamlit) para acelerar a criação de baralhos de estudo no **Anki**. A ferramenta possui uma interface amigável onde você faz o upload de uma lista de vocabulário e ela gera os cartões automaticamente, já com a pronúncia nativa (Text-to-Speech) anexada.

## ✨ Novidades da Versão Web
* **Interface Gráfica (UI):** Não é mais necessário rodar scripts no terminal para cada lista. Tudo é feito pelo navegador.
* **Upload Dinâmico:** Envie seus arquivos `.txt` simplesmente arrastando e soltando na página.
* **Seleção de Baralho:** Escolha para qual baralho as palavras irão diretamente pelo painel do site.
* **Feedback Visual:** Acompanhe o processo de criação de cartões em tempo real através de uma barra de progresso.

## 📋 Pré-requisitos

Antes de começar, certifique-se de ter instalado em sua máquina:
* **Python 3.x**
* **Anki** (O aplicativo desktop precisa estar instalado e aberto para a automação funcionar)

## ⚙️ Configuração Inicial

### 1. Preparando o Anki (AnkiConnect)
Para permitir que o app converse com o seu Anki, instale a API local:
1. Abra o **Anki**.
2. Vá em **Ferramentas** > **Complementos** > **Obter Complementos...**
3. Insira o código: `2055492159` (AnkiConnect) e clique em **OK**.
4. **Reinicie o Anki**.

### 2. Criando o Tipo de Nota (Recomendado)
Para evitar conflitos na verificação de cartões duplicados quando o áudio for gerado:
1. No Anki, vá em **Ferramentas** > **Gerenciar Tipos de Nota**.
2. Adicione um novo tipo Baseado no "Básico" e nomeie como **Inglês Automático**.
3. Em **Campos**, adicione um terceiro campo chamado `Audio`.
4. Em **Cartões**, adicione a tag `{{Audio}}` no Modelo da Frente.

### 3. Instalação do Projeto
Clone o repositório e instale as bibliotecas necessárias para o Web App rodar:
```bash
git clone https://github.com/SEU-USUARIO/nome-do-repositorio.git
cd nome-do-repositorio

# Instalação das dependências
pip install streamlit requests
```

## 🛠️ Como Usar

1. Deixe o aplicativo do **Anki aberto** no seu computador.
2. Crie seu arquivo de vocabulário (ex: `palavras.txt`). O formato deve ser estritamente uma palavra e uma tradução separadas por vírgula por linha:
   ```text
   house,casa
   dog,cachorro
   cat,gato
   ```
3. Abra o terminal na pasta do projeto e inicie o servidor do Web App:
   ```bash
   streamlit run app.py
   ```
4. O seu navegador abrirá automaticamente em `http://localhost:8501`.
5. Digite o nome do baralho, faça o upload do seu arquivo de texto e clique em **Iniciar Automação**!

## 📂 Estrutura do Projeto
* `app.py` — Código fonte contendo o Backend (integração com Anki) e o Frontend (Streamlit).
* `palavras.txt` — Arquivo de exemplo para upload.
* `README.md` — Documentação do projeto.

## 🛡️ Tratamento de Erros e Regras
* **Anti-Duplicatas:** O sistema barra automaticamente a inserção da mesma palavra no mesmo baralho.
* **Timeouts:** Se a internet falhar ou o servidor de áudio do Google atrasar, o app reporta o erro visualmente na tela e segue para a próxima palavra sem fechar a aplicação.
