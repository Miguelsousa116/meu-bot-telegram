import os
import time
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

TEU_CHAT_ID = 1963927934
SEU_LINK = "https://partners.meratrack.xyz/click?o=901&a=1367"
SEU_SUPORTE = "https://t.me/Paulo_miguel_23"

membros_registados = set()

@bot.message_handler(commands=['start'])
def enviar_start(mensagem):
    user = mensagem.from_user
    user_id = user.id
    nome = user.first_name
    
    membros_registados.add(user_id)
    total_membros = len(membros_registados)
    
    texto = (
        "🔥 **BEM-VINDO AO JACKPOT ZONE!** 🔥\n\n"
        "🎁 **PROMOÇÃO EXCLUSIVA DE HOJE:**\n\n"
        "➡️ Deposita no mínimo 20€ e ganhas +20€ grátis!\n"
        "➡️ Mais Bónus Buy de graça na slot Big Bass 1000!\n"
        "➡️ Acesso Instantâneo à plataforma VIP!\n\n"
        f"👥 **Membros no Bot:** {total_membros}\n\n"
        "👇 Clica no botão abaixo para abrir a plataforma e resgatar a tua promoção:"
    )
    
    teclado = InlineKeyboardMarkup()
    teclado.add(InlineKeyboardButton("🎰 ABRIR PLATAFORMA & GANHAR BÓNUS", url=SEU_LINK))
    teclado.add(InlineKeyboardButton("💬 Suporte VIP", url=SEU_SUPORTE))

    # Envia a mensagem para o utilizador
    try:
        bot.send_message(mensagem.chat.id, texto, reply_markup=teclado, parse_mode="Markdown")
    except Exception as e:
        print(f"Erro ao enviar mensagem: {e}")

    # Envia a notificação para o teu chat privado (TEU_CHAT_ID)
    if mensagem.chat.id != TEU_CHAT_ID:
        try:
            bot.send_message(TEU_CHAT_ID, f"👤 **Novo membro no bot!**\nNome: {nome}\nID: `{user_id}`\nTotal de membros: {total_membros}", parse_mode="Markdown")
        except Exception as e:
            print(f"Erro ao enviar notificação para o admin: {e}")

if __name__ == "__main__":
    threading.Thread(target=iniciar_servidor, daemon=True).start()
    
    try:
        bot.remove_webhook()
        time.sleep(1)
    except:
        pass

    print("Bot a iniciar...")
    
    while True:
        try:
            bot.polling(none_stop=True, interval=1, timeout=20)
        except Exception as e:
            print(f"Reconectando devido a: {e}")
            time.sleep(3)
