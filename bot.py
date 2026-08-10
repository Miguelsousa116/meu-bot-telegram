import os
import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
import threading
from http.server import HTTPServer, BaseHTTPRequestHandler

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

CHAVE_API = "8529787659:AAEspqZLGxIvsDD27DQ1Hz_VTcwlnEmu64A"
bot = telebot.TeleBot(CHAVE_API)

# O ID interno da tua foto no Telegram
FOTO_ID = "AgACAgQAAxkBAAICaWefY9-lH-XgAAFRd-x2l-9Jd9n5jQAC368xG8O-8VLkXhRk_QAB9QEAAwIAA3kAAzYE"

@bot.message_handler(commands=['start'])
def enviar_start(mensagem):
    texto = (
        "🔥 BEM-VINDO AO JACKPOT ZONE! 🔥\n\n"
        "🎁 PROMOÇÃO EXCLUSIVA DE HOJE:\n\n"
        "➡️ Deposita no mínimo 20€ e ganhas +20€ grátis!\n"
        "➡️ Mais Bónus Buy de graça na slot Big Bass 1000!\n"
        "➡️ Acesso Instantâneo à plataforma VIP!\n\n"
        "👇 Clica no botão abaixo para abrir a plataforma e resgatar a tua promoção:"
    )
    
    teclado = InlineKeyboardMarkup()
    teclado.add(InlineKeyboardButton("🎰 ABRIR PLATAFORMA & GANHAR BÓNUS", url="https://partners.meratrack.xyz/click?o=901&a=1367"))
    teclado.add(InlineKeyboardButton("💬 Suporte VIP", url="https://t.me/Paulo_miguel_23"))

    try:
        # Tenta enviar a foto pelo ID interno
        bot.send_photo(mensagem.chat.id, FOTO_ID, caption=texto, reply_markup=teclado, parse_mode="Markdown")
    except Exception as e:
        # Se falhar (por exemplo, se o ID expirou), manda o texto
        print(f"Erro na foto: {e}")
        bot.send_message(mensagem.chat.id, texto, reply_markup=teclado, parse_mode="Markdown")

if __name__ == "__main__":
    threading.Thread(target=iniciar_servidor, daemon=True).start()
    bot.infinity_polling()
