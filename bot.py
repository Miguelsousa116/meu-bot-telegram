import os
from http.server import HTTPServer, BaseHTTPRequestHandler
import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

# 1. Configurar o servidor web falso para o Render não desligar o bot
class KeepAliveHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"Bot Online!")
    def log_message(self, format, *args):
        return

def iniciar_servidor():
    porta = int(os.environ.get("PORT", 8080))
    servidor = HTTPServer(("0.0.0.0", porta), KeepAliveHandler)
    servidor.serve_forever()

# 2. As tuas credenciais e dados do bot
CHAVE_API = "8529787659:AAH142nF67POXbzTc60W229WBEYY4vtuXiw"
bot = telebot.TeleBot(CHAVE_API)

TEU_CHAT_ID = 1963927934
CANAL_ID = "@JACKPOT_ZONE"

SEU_LINK = "https://partners.meratrack.xyz/click?o=901&a=1367"
SEU_SUPORTE = "https://t.me/Paulo_miguel_23"

# 3. Arrancar o servidor web em primeiro plano (necessário para o Render)
if name == "main":
    import threading
    # Inicia o servidor web numa linha separada para manter a porta aberta
    threading.Thread(target=iniciar_servidor, daemon=True).start()
    
    print("Bot a iniciar...")
    # Inicia o bot do Telegram
    bot.infinity_polling()
