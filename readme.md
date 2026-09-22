# Anki Automation with Python & AnkiConnect

Uma automação em Python desenvolvida para acelerar a criação de baralhos de estudo no **Anki**, gerando cartões em lote a partir de uma lista de texto e baixando automaticamente a pronúncia em áudio (Text-to-Speech) de cada palavra.

---

## 🚀 O que este projeto faz?
Estudar idiomas exige volume, mas cadastrar palavras manualmente no Anki consome muito tempo. Este script resolve esse problema ao:
1. Ler uma lista de palavras de um arquivo de texto simples (`palavras.txt`).
2. Conectar-se ao Anki em segundo plano através de uma API local (**AnkiConnect**).
3. Criar os cartões automaticamente separando a palavra (Frente) e a tradução (Verso).
4. Gerar e anexar o áudio da pronúncia em inglês (via API pública do Google Tradutor) direto no cartão.
5. Evitar duplicatas no baralho para manter sua coleção limpa.

---

## 📋 Pré-requisitos
Antes de começar, certifique-se de ter instalado em sua máquina:
* **Python 3.x** (Testado e compatível com as versões mais recentes).
* **Anki** instalado no computador.

---

## ⚙️ Passo a Passo para Configuração

### 1. Configurando o Anki (AnkiConnect)
Para permitir que o Python converse com o Anki, você precisa instalar o complemento de API local.
1. Abra o **Anki** no seu computador.
2. No menu superior, vá em **Ferramentas** > **Complementos** > **Obter Complementos...**.
3. Insira o código numérico: `2055492159` e clique em **OK**.
4. **Reinicie o Anki** para ativar o complemento.

### 2. Criando o Tipo de Nota Personalizado 
Para garantir que a verificação de duplicatas funcione perfeitamente sem conflitos com os arquivos de áudio:
1. No Anki, vá em **Ferramentas** > **Gerenciar Tipos de Nota**.
2. Clique em **Adicionar** > escolha **Adicionar: Básico** e nomeie como **Inglês Automático**.
3. Selecione o novo tipo de nota, clique em **Campos** e adicione um novo campo chamado `Audio`.
4. Clique em **Cartões...** e certifique-se de que o campo `{{Audio}}` está visível no modelo do cartão (ex: abaixo da `{{Frente}}`).

### 3. Clonando e Instalando Dependências do Projeto
1. Clone este repositório ou baixe os arquivos para uma pasta local:
   ```bash
   git clone https://github.com/GabrielFelix-dev/AutamacaoPython-Anki.git
   ```
2. Instale a biblioteca necessária (`requests`) para gerenciar as requisições HTTP:
   ```bash
   pip install requests
   ```

---

## 🛠️ Como Usar

1. **Abra o aplicativo do Anki** no seu computador (ele precisa estar aberto rodando em segundo plano para a automação funcionar).
2. Na mesma pasta do projeto, crie ou edite o arquivo `palavras.txt` seguindo o padrão `palavra,tradução` (uma por linha, sem espaços extras):
   ```text
   house,casa
   dog,cachorro
   cat,gato
   ```
3. Abra o terminal na pasta do projeto e execute o script:
   ```bash
   python automacao_anki.py
   ```
4. Acompanhe o progresso no terminal. Abra o Anki e seus cartões estarão lá prontos para estudo, com áudio nativo!

---

## 📂 Estrutura do Projeto
* `automacao_anki.py` — Script principal em Python que realiza a leitura, tratamento de erros e envio via API.
* `palavras.txt` — Arquivo de texto contendo a base de dados de vocabulário (Frente,Verso).
* `README.md` — Documentação de instruções do projeto.

---

## 🛡️ Tratamento de Erros Integrado
O script conta com proteções automáticas para:
* **Duplicatas:** Impede que a mesma palavra seja gerada duas vezes dentro do mesmo baralho (`duplicateScope: "deck"`).
* **Timeout:** Caso a conexão com a internet caia ou o servidor de áudio demore para responder, o script define um limite de 10 segundos por requisição, pulando para a próxima palavra sem quebrar a execução geral.
