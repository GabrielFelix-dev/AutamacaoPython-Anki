import requests

url = 'http://localhost:8765'

# 1. Abre o arquivo de texto no modo de leitura ('r' de read) e com suporte a acentos (utf-8)
with open('palavras.txt', 'r', encoding='utf-8') as arquivo_de_palavras:
    
    # 2. Varredura no arquivo txt
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
                    "deckName": "teste2", # <-- INSIRA AQUI O NOME DO BARALHO
                    "modelName": "Inglês Automático", # <-- CERTIFIQUE-SE DE TER CRIADO A NOTA DE ACORDO COM O README
                    "fields": {
                        "Frente": frente, # Injeta a palavra em inglês 
                        "Verso": verso    # Injeta a tradução 
                    },
                    "options": {
                        "allowDuplicate": False,
                        "duplicateScope": "deck" # Busca duplicatas apenas no baralho atual
                    },
                    "audio": [{
                        "url": f"https://translate.google.com/translate_tts?ie=UTF-8&tl=en&client=tw-ob&q={frente}",
                        "filename": f"audio_gerado_{frente}.mp3",
                        "fields": [
                            "Audio"
                        ]
                    }]
                }
            }
        }
        
                
        # 5. Tratamento de erros
        try:
            # Adicionamos o timeout (em segundos) direto no "carteiro"
            resposta = requests.post(url, json=pacote, timeout=10)
            
            # Extraímos a resposta do Anki
            resultado = resposta.json()
            
            if resultado.get('error') is not None:
                print(f"Falha na palavra '{frente}': {resultado['error']}")
            else:
                print(f"Sucesso! '{frente}' adicionada com áudio.")

        # 6. Exceptions:
        except requests.exceptions.Timeout:
            print(f"Demorou muito para processar '{frente}'. Pulando para a próxima...")
            
        except requests.exceptions.ConnectionError:
            print(f"Erro de conexão. O Anki está aberto? A internet caiu? Parando tudo.")
            break 
            
        except Exception as erro_generico:
            # Captura qualquer outro erro 
            print(f"Erro inesperado na palavra '{frente}': {erro_generico}")

