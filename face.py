import telegram
import asyncio

# Cria o objeto de captura de vídeo
captura = cv2.VideoCapture(0)

# Cria o classificador de rosto
classificador_rosto = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Cria o bot com o token de acesso
bot = telegram.Bot(token=' seu token ')

# Variável para verificar se o rosto já foi detectado
rostro_detectado = False

while True:
    # Captura um quadro de vídeo
    ret, quadro = captura.read()

    # Converte o quadro para escala de cinza
    cinza = cv2.cvtColor(quadro, cv2.COLOR_BGR2GRAY)

    # Detecta os rostos no quadro
    rostos = classificador_rosto.detectMultiScale(cinza)

    # Desenha um retângulo em volta de cada rosto detectado
    for (x, y, w, h) in rostos:
        cv2.rectangle(quadro, (x, y), (x+w, y+h), (0, 255, 0), 2)
        
        # Verifica se o rosto já foi detectado para evitar o envio repetido da mensagem
        if not rostro_detectado:
            
            # Envia uma mensagem para o Telegram em uma nova tarefa
            await bot.send_message(chat_id=' ID do BOT ', text=' Texto de sua preferência! ')
            
            # Atualiza a variável para evitar o envio repetido da mensagem
            rostro_detectado = True
    else:
        # Se nenhum rosto foi detectado, reseta a variável para permitir o envio da mensagem novamente
        rostro_detectado = False

    # Exibe o quadro com os retângulos desenhados
    cv2.imshow('Reconhecimento de Rosto', quadro)

    # Espera por uma tecla pressionada
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Libera o objeto de captura de vídeo e fecha a janela
captura.release()
cv2.destroyAllWindows()