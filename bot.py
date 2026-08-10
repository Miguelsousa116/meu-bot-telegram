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

# ESTE É O FILE_ID DA TUA FOTO QUE O TELEGRAM RECONHECE
# Assim ele não precisa de links da internet, envia a foto que já lá está
FOTO_ID = "AgACAgQAAxkBAAICaWefY9-lH-XgAAFRd-x2l-9Jd9n5jQAC368xG8O-8VLkXhRk_QAB9QEAAwIAA3kAAzYE"

membros_registados = set()

@bot.message_handler(commands=['start'])
def enviar_start(mensagem):
    user_id = mensagem.from_user.id
    membros_registados.add(user_id)
    total_membros = len(membros_registados)

    texto_boas_vindas = (
        "🔥 BEM-VINDO AO JACKPOT ZONE! 🔥\n\n"
        "🎁 PROMOÇÃO EXCLUSIVA DE HOJE:\n\n"
        "➡️ Deposita no mínimo 20€ e ganhas +20€ grátis!\n"
        "➡️ Mais Bónus Buy de graça na slot Big Bass 1000!\n"
        "➡️ Acesso Instantâneo à plataforma VIP!\n\n"
        f"👥 Membros no Bot: {total_membros}\n\n"
        "👇 Clica no botão abaixo para abrir a plataforma e resgatar a tua promoção:"
    )

    teclado = InlineKeyboardMarkup()
    teclado.add(InlineKeyboardButton("🎰 ABRIR PLATAFORMA & GANHAR BÓNUS", url=SEU_LINK))
    teclado.add(InlineKeyboardButton("💬 Suporte VIP", url=SEU_SUPORTE))

    # Envio forçado da foto pelo ID interno
    bot.send_photo(mensagem.chat.id, FOTO_ID, caption=texto_boas_vindas, reply_markup=teclado, parse_mode="Markdown")

    if mensagem.chat.id != TEU_CHAT_ID:
        bot.send_message(TEU_CHAT_ID, f"👤 Novo membro: {mensagem.from_user.first_name} (ID: {user_id})")

if __name__ == "__main__":
    threading.Thread(target=iniciar_servidor, daemon=True).start()
    bot.infinity_polling()
