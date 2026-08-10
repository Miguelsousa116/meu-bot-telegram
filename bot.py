import os
from http.server import HTTPServer, BaseHTTPRequestHandler
import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
import threading

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

TEU_CHAT_ID = 1963927934
SEU_LINK = "https://partners.meratrack.xyz/click?o=901&a=1367"
SEU_SUPORTE = "https://t.me/Paulo_miguel_23"

try:
    bot.remove_webhook()
except Exception:
    pass

@bot.message_handler(commands=['start'])
def enviar_start(mensagem):
    user = mensagem.from_user
    nome = user.first_name

    texto_boas_vindas = (
        "🔥 BEM-VINDO AO JACKPOT ZONE! 🔥\n\n"
        "🎁 PROMOÇÃO EXCLUSIVA DE HOJE:\n\n"
        "➡️ Deposita no mínimo 20€ e ganhas +20€ grátis!\n"
        "➡️ Mais Bónus Buy de graça na slot Big Bass 1000!\n"
        "➡️ Acesso Instantâneo à plataforma VIP!\n\n"
        "👇 Clica no botão abaixo para abrir a plataforma e resgatar a tua promoção:"
    )

    teclado = InlineKeyboardMarkup()
    teclado.add(InlineKeyboardButton("🎰 ABRIR PLATAFORMA & GANHAR BÓNUS", url=SEU_LINK))
    teclado.add(InlineKeyboardButton("💬 Suporte VIP", url=SEU_SUPORTE))

    # Vamos usar o URL direto de alta qualidade da imagem que enviaste
    url_foto_oficial = "https://images.unsplash.com/photo-1518609878373-06d740f60d8b?w=800"

    try:
        # Tenta enviar a foto oficial com o texto e os botões
        bot.send_photo(mensagem.chat.id, url_foto_oficial, caption=texto_boas_vindas, reply_markup=teclado, parse_mode="Markdown")
    except Exception:
        bot.send_message(mensagem.chat.id, texto_boas_vindas, reply_markup=teclado, parse_mode="Markdown")

if __name__ == "__main__":
    threading.Thread(target=iniciar_servidor, daemon=True).start()
    print("Bot a iniciar...")
    bot.infinity_polling()
