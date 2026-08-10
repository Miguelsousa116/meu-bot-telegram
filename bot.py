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

SEU_LINK = "https://partners.meratrack.xyz/click?o=901&a=1367"
SEU_SUPORTE = "https://t.me/Paulo_miguel_23"

membros_registados = set()

@bot.message_handler(commands=['start'])
def enviar_start(mensagem):
    user_id = mensagem.from_user.id
    membros_registados.add(user_id)
    total_membros = len(membros_registados)
    
    texto = (
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

    try:
        bot.send_message(mensagem.chat.id, texto, reply_markup=teclado, parse_mode="Markdown")
    except Exception as e:
        print(f"Erro ao enviar mensagem: {e}")

if __name__ == "__main__":
    # Inicia o servidor Keep-Alive
    threading.Thread(target=iniciar_servidor, daemon=True).start()
    
    print("A limpar conexões antigas do Telegram...")
    try:
        # FORÇA A ELIMINAÇÃO DE QUALQUER SESSÃO ANTERIOR PRESA
        bot.remove_webhook()
    except Exception:
        pass

    print("Bot a iniciar polling...")
    bot.infinity_polling(skip_pending=True)
