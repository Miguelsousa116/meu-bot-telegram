import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

CHAVE_API = "8529787659:AAHl42nF67POXbzTc6OW229WBEYY4vtuXiw"
bot = telebot.TeleBot(CHAVE_API)

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
    texto = (
        "🔥 *BEM-VINDO AO JACKPOT ZONE!*\n\n"
        "> 🎁 *PROMOÇÃO EXCLUSIVA DE HOJE:*\n"
        "> \n"
        "> ➡️ *Recebes mais 20 gratis*\n"
        "> ➡️ *Mais bonus buy na slot big bass 1000*\n"
        "> ➡️ *Acesso Instantâneo à plataforma VIP*\n\n"
        "👇 Clica no botão abaixo para abrir a plataforma e resgatar a tua promoção:"
    )
    bot.send_message(mensagem.chat.id, texto, parse_mode="Markdown", reply_markup=menu_afiliado())

@bot.message_handler(func=lambda msg: True)
def resposta_padrao(mensagem):
    texto = "👇 Clica no botão abaixo para abrir a plataforma:"
    bot.send_message(mensagem.chat.id, texto, reply_markup=menu_afiliado())

bot.polling()