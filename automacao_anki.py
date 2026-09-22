import requests

url = 'http://localhost:8765'

# 1. Abre o arquivo de texto no modo de leitura ('r' de read) e com suporte a acentos (utf-8)
with open('palavras.txt', 'r', encoding='utf-8') as arquivo_de_palavras:
    
    # 2. O Loop: A partir daqui, o código se repete para cada linha do texto
    for linha in arquivo_de_palavras:
        
        # 3. Limpamos a linha e cortamos onde tem a vírgula
        # A primeira parte vai para a variável 'frente', a segunda para 'verso'
        texto_limpo = linha.strip()
        frente, verso = texto_limpo.split(',')
        
        # 4. Construímos o pacote usando as variáveis que acabamos de cortar
        pacote = {
            "action": "addNote",
            "version": 6,
            "params": {
                "note": {
                    "deckName": "Inglês", 
                    "modelName": "Básico",
                    "fields": {
                        "Frente": frente, # Injeta a palavra em inglês aqui
                        "Verso": verso    # Injeta a tradução aqui
                    },
                    "audio": [{
                        "url": f"https://translate.google.com/translate_tts?ie=UTF-8&tl=en&client=tw-ob&q={frente}",
                        "filename": f"audio_gerado_{frente}.mp3",
                        "fields": [
                            "Frente"
                        ]
                    }]
                }
            }
        }
        
        # 5. Enviamos para o Anki
        resposta = requests.post(url, json=pacote)
        
        # 6. Imprimimos um aviso visual no terminal para acompanhar o progresso
        print(f"Palavra '{frente}' enviada! Resposta do Anki: {resposta.json()}")

print("Automação concluída!")