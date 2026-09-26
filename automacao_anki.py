import streamlit as st
import requests

URL_ANKI = 'http://localhost:8765'

# 1. A FUNÇÃO DE ENVIO
def adicionar_ao_anki(frente, verso, deck_name="teste1"):
    pacote = {
        "action": "addNote",
        "version": 6,
        "params": {
            "note": {
                "deckName": deck_name, 
                "modelName": "Inglês Automático",
                "fields": {
                    "Frente": frente, 
                    "Verso": verso    
                },
                "options": {
                    "allowDuplicate": False,
                    "duplicateScope": "deck" 
                },
                "audio": [{
                    "url": f"https://translate.google.com/translate_tts?ie=UTF-8&tl=en&client=tw-ob&q={frente}",
                    "filename": f"audio_gerado_{frente}.mp3",
                    "fields": ["Audio"]
                }]
            }
        }
    }
    
    try:
        resposta = requests.post(URL_ANKI, json=pacote, timeout=10)
        resultado = resposta.json()
        
        if resultado.get('error') is not None:
            return False, resultado['error']
        return True, "Adicionado com sucesso!"
        
    except requests.exceptions.ConnectionError:
        return False, "Erro de conexão. O Anki está aberto?"
    except Exception as e:
        return False, f"Erro: {str(e)}"

# 2. A INTERFACE DO SITE:

# Título da página
st.title(" ✂️ Automação do Anki")
st.write("Adicione dezenas de palavras com áudio ao seu Anki em segundos.")

# Caixa para o usuário digitar o nome do baralho
nome_do_baralho = st.text_input("Qual o nome do baralho no Anki?", value="teste1")

# Botão de Upload para o arquivo de texto
arquivo_enviado = st.file_uploader("Envie seu arquivo de palavras (.txt)", type=["txt"])

# Se o usuário enviou um arquivo, mostramos um botão para iniciar
if arquivo_enviado is not None:
    if st.button("Iniciar Automação"):
        
        # Lemos o conteúdo do arquivo que foi upado no site
        conteudo = arquivo_enviado.getvalue().decode("utf-8")
        linhas = conteudo.strip().split('\n')
        
        # Criamos uma barra de progresso visual
        barra_progresso = st.progress(0)
        status_texto = st.empty()
        
        erros = []
        sucessos = 0
        
        # Começamos a esteira de produção
        for i, linha in enumerate(linhas):
            if ',' not in linha:
                continue # Pula linhas vazias ou formatadas errado
                
            frente, verso = linha.strip().split(',', 1)
            
            # Atualiza o texto na tela para o usuário ver o que está acontecendo
            status_texto.write(f"Processando: **{frente}**...")
            
            deu_certo, mensagem = adicionar_ao_anki(frente, verso, nome_do_baralho)
            
            if deu_certo:
                sucessos += 1
            else:
                erros.append(f"{frente}: {mensagem}")
                
            # Atualiza a barra de progresso
            progresso_atual = (i + 1) / len(linhas)
            barra_progresso.progress(progresso_atual)
            
        # Resumo Final na tela
        status_texto.write("Processamento concluído!")
        st.success(f"🎉 Automação finalizada! {sucessos} cartões adicionados.")
        
        # Se teve erro (como duplicatas), mostra um aviso em amarelo
        if erros:
            st.warning("Alguns cartões não foram adicionados:")
            for erro in erros:
                st.write(f"- {erro}")