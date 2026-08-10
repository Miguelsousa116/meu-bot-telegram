import os
from http.server import HTTPServer, BaseHTTPRequestHandler
import telebot
import threading

class KeepAliveHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"Bot Online!")

def iniciar_servidor():
    porta = int(os.environ.get("PORT", 8080))
    servidor = HTTPServer(("0.0.0.0", porta), KeepAliveHandler)
    servidor.serve_forever()

CHAVE_API = "8529787659:AAEspqZLGxIvsDD27DQ1Hz_VTcwlnEmu64A"
bot = telebot.TeleBot(CHAVE_API)

# Este comando vai ajudar-nos a descobrir o ID
@bot.message_handler(func=lambda message: True)
def echo_all(message):
    if message.chat.type in ['group', 'supergroup']:
        bot.reply_to(message, f"O ID deste grupo é: {message.chat.id}")

if __name__ == "__main__":
    threading.Thread(target=iniciar_servidor, daemon=True).start()
    print("Bot a iniciar...")
    bot.infinity_polling()
