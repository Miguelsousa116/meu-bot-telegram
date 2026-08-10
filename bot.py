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

# ID fixo da imagem oficial do Big Bass que enviaste para o bot
FOTO_BIG_BASS = "AgACAgQAAxkBAAICaWefY... (coloca aqui o teu file_id ou usa o link direto da imagem)"

# Lista para guardar os membros do bot
membros_registados = set()

try:
    bot.remove_webhook()
except Exception:
    pass

@bot.message_handler(commands=['start'])
def enviar_start(mensagem):
    user = mensagem.from_user
    nome = user.first_name
    user_id = user.id

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

    # Vamos usar o file_id direto da imagem que o bot recebeu de ti
    # Dica: Se preferires colocar um link direto da web para a imagem, substitui por "https://telegra.ph/file/..."
    
    try:
        # Se enviaste a foto para o bot, podes usar o ID exato dela ou enviar diretamente por URL válida
        bot.send_photo(mensagem.chat.id, "https://telegra.ph/file/aqui_o_link.jpg", caption=texto_boas_vindas, reply_markup=teclado, parse_mode="Markdown")
    except Exception:
        # Alternativa segura caso queiras usar o envio direto da tua última mensagem ao bot:
        pass

    if mensagem.chat.id != TEU_CHAT_ID:
        try:
            aviso_admin = (
                f"👤 NOVO MEMBRO NO BOT!\n\n"
                f"• Nome: {nome}\n"
                f"• ID: {user_id}\n"
                f"• Total no bot: {total_membros}"
            )
            bot.send_message(TEU_CHAT_ID, aviso_admin, parse_mode="Markdown")
        except Exception as e:
            print(f"Erro: {e}")

if __name__ == "__main__":
    threading.Thread(target=iniciar_servidor, daemon=True).start()
    print("Bot a iniciar...")
    bot.infinity_polling()
