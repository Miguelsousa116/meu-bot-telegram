import os
from http.server import HTTPServer, BaseHTTPRequestHandler
import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
import threading

# 1. Servidor web para o Render manter o bot acordado
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

# 2. As tuas credenciais
CHAVE_API = "8529787659:AAH142nF67POXbzTc60W229WBEYY4vtuXiw"
bot = telebot.TeleBot(CHAVE_API)

TEU_CHAT_ID = 1963927934
CANAL_ID = "@JACKPOT_ZONE"

SEU_LINK = "https://partners.meratrack.xyz/click?o=901&a=1367"
SEU_SUPORTE = "https://t.me/Paulo_miguel_23"

# 3. Eliminar o webhook antigo para evitar o Erro 409
try:
    bot.remove_webhook()
except Exception:
    pass

# 4. Resposta ao comando /start (com os teus botões e aviso para ti)
@bot.message_handler(commands=['start'])
def enviar_start(mensagem):
    user = mensagem.from_user
    nome = user.first_name
    username = f"@{user.username}" if user.username else "Sem username"
    user_id = user.id

    # Envia o aviso para o teu chat privado
    aviso = f"🚨 NOVO UTILIZADOR NO BOT!\n\nNome: {nome}\nUser: {username}\nID: {user_id}"
    bot.send_message(TEU_CHAT_ID, aviso, parse_mode="Markdown")

    # Mensagem de boas-vindas com a promoção para o utilizador
    texto_boas_vindas = (
        "🎰 BEM-VINDO AO JACKPOT ZONE!\n\n"
        "🎁 PROMOÇÃO EXCLUSIVA DE HOJE:\n"
        "➡️ Deposita no mínimo 20€ e ganhas +20€ grátis\n"
        "➡️ Mais bónus buy na slot Big Bass 1000\n"
        "➡️ Acesso Instantâneo à plataforma VIP\n\n"
        "👇 Clica no botão abaixo para abrir a plataforma e resgatar a promoção:"
    )

    teclado = InlineKeyboardMarkup()
    teclado.add(InlineKeyboardButton("🎰 ABRIR PLATAFORMA & GANHAR BÓNUS", url=SEU_LINK))
    teclado.add(InlineKeyboardButton("💬 Suporte VIP", url=SEU_SUPORTE))

    bot.send_message(mensagem.chat.id, texto_boas_vindas, reply_markup=teclado, parse_mode="Markdown")

# 5. Arranque principal (Servidor + Bot)
if name == "main":
    # Arranca o servidor web numa thread separada
    threading.Thread(target=iniciar_servidor, daemon=True).start()
    
    print("Bot a iniciar e pronto a receber mensagens...")
    # Arranca o bot do Telegram sem conflitos
    bot.infinity_polling()
