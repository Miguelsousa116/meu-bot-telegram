import os
import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
import threading
from http.server import HTTPServer, BaseHTTPRequestHandler

# Servidor para o Render
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

# Lista de membros
membros_registados = set()

@bot.message_handler(commands=['start'])
def enviar_start(mensagem):
    membros_registados.add(mensagem.from_user.id)
    total_membros = len(membros_registados)
    
    texto = (
        "🔥 BEM-VINDO AO JACKPOT ZONE! 🔥\n\n"
        f"👥 Membros no Bot: {total_membros}\n\n"
        "👇 Clica no botão abaixo:"
    )
    
    teclado = InlineKeyboardMarkup()
    teclado.add(InlineKeyboardButton("🎰 ABRIR PLATAFORMA", url="https://partners.meratrack.xyz/click?o=901&a=1367"))

    # AQUI ESTÁ A MUDANÇA: Abrimos a foto que está na mesma pasta do código
    try:
        with open('foto.jpg', 'rb') as photo:
            bot.send_photo(mensagem.chat.id, photo, caption=texto, reply_markup=teclado, parse_mode="Markdown")
    except Exception as e:
        # Se falhar, manda texto simples
        bot.send_message(mensagem.chat.id, texto, reply_markup=teclado, parse_mode="Markdown")
        print(f"Erro ao ler foto: {e}")

if __name__ == "__main__":
    threading.Thread(target=iniciar_servidor, daemon=True).start()
    bot.infinity_polling()
