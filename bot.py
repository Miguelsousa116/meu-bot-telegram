import os
import threading
from http.server import HTTPServer, BaseHTTPRequestHandler
import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

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

threading.Thread(target=iniciar_servidor, daemon=True).start()

CHAVE_API = "8529787659:AAH142nF67POXbzTc60W229WBEYY4vtuXiw"
bot = telebot.TeleBot(CHAVE_API)

TEU_CHAT_ID = 1963927934
CANAL_ID = "@JACKPOT_ZONE"

SEU_LINK = "https://partners.meratrack.xyz/click?o=901&a=1367"
SEU_SUPORTE = "https://t.me/Paulo_miguel_23"

def menu_afiliado():
    markup = InlineKeyboardMarkup()
    btn_link = InlineKeyboardButton("🎰 ABRIR PLATAFORMA & GANHAR BÓNUS", url=SEU_LINK)
    btn_suporte = InlineKeyboardButton("💬 Suporte VIP", url=SEU_SUPORTE)
    markup.add(btn_link)
    markup.add(btn_suporte)
    return markup

@bot.message_handler(commands=["start"])
def enviar_boas_vindas(mensagem):
    user_id = mensagem.from_user.id
    first_name = mensagem.from_user.first_name
    username = mensagem.from_user.username or "Sem username"
    
    try:
        if not os.path.exists("utilizadores.txt"):
            with open("utilizadores.txt", "w") as f:
                pass
        with open("utilizadores.txt", "r") as f:
            lista = f.read().splitlines()
        if str(user_id) not in lista:
            with open("utilizadores.txt", "a") as f:
                f.write(f"{user_id}\n")
        msg_aviso = (
            f"🔔 *NOVO UTILIZADOR NO BOT!*\n\n"
            f"👤 Nome: {first_name}\n"
            f"🔗 User: @{username}\n"
            f"🆔 ID: {user_id}"
        )
        bot.send_message(TEU_CHAT_ID, msg_aviso, parse_mode="Markdown")
    except Exception as e:
        print(f"Erro no registo: {e}")

    texto_cliente = (
        "🎰 *BEM-VINDO AO JACKPOT ZONE!*\n\n"
        "🎁 *PROMOÇÃO EXCLUSIVA DE HOJE:*\n\n"
        "➡️ Deposita no mínimo 20€ e ganhas +20€ grátis\n"
        "➡️ Mais bónus buy na slot Big Bass 1000\n"
        "➡️ Acesso Instantâneo à plataforma VIP\n\n"
        "👇 Clica no botão abaixo para abrir a plataforma e resgatar a tua promoção:"
    )
    try:
        bot.send_message(chat_id=user_id, text=texto_cliente, parse_mode="Markdown", reply_markup=menu_afiliado())
    except Exception as e:
        print(f"Erro ao enviar para o cliente: {e}")

    texto_canal = (
        "🎰 *JACKPOT ZONE 🎁*\n\n"
        "🔥 *RECURSO DE BÓNUS ADQUIRIDO!*\n"
        "Deposita 20€ e ganha mais 20€ extra + bónus buy grátis na slot Big Bass 1000!"
    )
    try:
        bot.send_message(chat_id=CANAL_ID, text=texto_canal, parse_mode="Markdown", reply_markup=menu_afiliado())
    except Exception as e:
        print(f"Erro ao enviar para o canal: {e}")

if name == "main":
    print("Bot a iniciar...")
    bot.infinity_polling()
