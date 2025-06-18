import pyautogui
import time
import webbrowser

# Número de destino (com código do país)
numero = "+"

# Mensagem a ser enviada
mensagem = "Sua mensagem aqui"

# Quantidade de mensagens a serem enviadas Exemplo: 200 pode ser alterada conforme necessário ou conforme o seu PC aguentar
quantidade = 200 

# Abre o WhatsApp Web no chat do número específico
webbrowser.open(f"https://web.whatsapp.com/send?phone={numero}")
time.sleep(15)  # Tempo para o usuário escanear o QR Code, se necessário

print("\n==== Iniciando envio de mensagens ====")

# Loop para enviar múltiplas mensagens sem reabrir o WhatsApp
for i in range(quantidade):
    pyautogui.write(mensagem)  # Digita a mensagem no campo de texto
    pyautogui.press("enter")   # Pressiona Enter para enviar
    time.sleep(15)  # Pequeno atraso entre as mensagens

print("\n✅✅✅ Envio concluído com sucesso!")
