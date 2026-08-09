import os
import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

CHAVE_API = "8529787659:AAHl42nF67POXbzTc6OW229WBEYY4vtuXiw"
bot = telebot.TeleBot(CHAVE_API)

# O teu ID do Telegram para receber as notificações
TEU_CHAT_ID = 1963927934 

# Seus links configurados
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

    # 1. Registar utilizador em segurança
    try:
        # Cria o ficheiro se não existir
        if not os.path.exists("utilizadores.txt"):
            with open("utilizadores.txt", "w") as f:
                pass

        with open("utilizadores.txt", "r") as f:
            lista = f.read().splitlines()

        if str(user_id) not in lista:
            with open("utilizadores.txt", "a") as f:
                f.write(f"{user_id}\n")
            
            # Notificação para o teu Telegram
            msg_aviso = (
                f"🔔 *NOVO UTILIZADOR NO BOT!*\n\n"
                f"👤 *Nome:* {first_name}\n"
                f"🔗 *User:* @{username}\n"
                f"🆔 *ID:* {user_id}"
            )
            bot.send_message(TEU_CHAT_ID, msg_aviso, parse_mode="Markdown")
    except Exception as e:
        print(f"Erro no registo: {e}")

    # 2. Mensagem para o cliente
    texto = (
        "🔥 *BEM-VINDO AO JACKPOT ZONE!*\n\n"
        "> 🎁 *PROMOÇÃO EXCLUSIVA DE HOJE:*\n"
        "> \n"
        "> ➡️ *Deposita no mínimo 20€ e ganhas +20€ grátis*\n"
        "> ➡️ *Mais bonus buy na slot Big Bass 1000*\n"
        "> ➡️ *Acesso Instantâneo à plataforma VIP*\n\n"
        "👇 Clica no botão abaixo para abrir a plataforma e resgatar a tua promoção:"
    )
    bot.send_message(mensagem.chat.id, texto, parse_mode="Markdown", reply_markup=menu_afiliado())

@bot.message_handler(func=lambda msg: True)
def resposta_padrao(mensagem):
    texto = "👇 Clica no botão abaixo para abrir a plataforma:"
    bot.send_message(mensagem.chat.id, texto, reply_markup=menu_afiliado())

bot.polling(none_stop=True)
