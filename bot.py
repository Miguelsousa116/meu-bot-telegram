import os
import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
from flask import Flask, request

CHAVE_API = "8529787659:AAEspqZLGxIvsDD27DQ1Hz_VTcwlnEmu64A"
bot = telebot.TeleBot(CHAVE_API, threaded=False)

app = Flask(__name__)

TEU_CHAT_ID = 1963927934
SEU_LINK = "https://partners.meratrack.xyz/click?o=901&a=1367"
SEU_SUPORTE = "https://t.me/Paulo_miguel_23"
membros_registados = set()

@app.route(f'/{CHAVE_API}', methods=['POST'])
def receber_mensagem():
    json_string = request.get_data().decode('utf-8')
    update = telebot.types.Update.de_json(json_string)
    bot.process_new_updates([update])
    return "!", 200

@app.route('/')
def index():
    return "Bot Online!", 200

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

    try:
        bot.send_message(mensagem.chat.id, texto, reply_markup=teclado, parse_mode="Markdown")
    except Exception as e:
        print(f"Erro ao enviar mensagem: {e}")

    if mensagem.chat.id != TEU_CHAT_ID:
        try:
            bot.send_message(TEU_CHAT_ID, f"👤 **Novo membro no bot!**\nNome: {nome}\nID: `{user_id}`\nTotal: {total_membros}", parse_mode="Markdown")
        except Exception as e:
            print(f"Erro admin: {e}")

if __name__ == "__main__":
    # URL do teu serviço no Render (substitui se o teu link for ligeiramente diferente)
    RENDER_URL = "https://meu-bot-telegram-1-be72.onrender.com"
    
    bot.remove_webhook()
    bot.set_webhook(url=f"{RENDER_URL}/{CHAVE_API}")
    
    porta = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=porta)
