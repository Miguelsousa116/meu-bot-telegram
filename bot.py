import os
import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

# Configurações principais do Bot
CHAVE_API = "8529787659:AAH142nF67POXbzTc60W229WBEYY4vtuXiw"
bot = telebot.TeleBot(CHAVE_API)

# O teu ID do Telegram para receber as notificações de novos utilizadores
TEU_CHAT_ID = 1963927934

# ID ou Username do teu canal (ex: "@nome_do_canal" ou o ID numérico -100...)
# Certifica-te de que o bot é administrador do canal para conseguir enviar mensagens para lá.
CANAL_ID = "@JACKPOT_ZONE"  # Substitui pelo username exato do teu canal se necessário

# Links configurados
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
    
    # 1. Registar utilizador em segurança (opcional/mantido do teu código)
    try:
        if not os.path.exists("utilizadores.txt"):
            with open("utilizadores.txt", "w") as f:
                pass
    except Exception as e:
        print(f"Erro ao criar ficheiro: {e}")

    # 2. Enviar notificação para ti (Administrador)
    try:
        texto_admin = (
            f"🔔 NOVO UTILIZADOR NO BOT!\n\n"
            f"👤 Nome: {first_name}\n"
            f"🔗 User: @{username}\n"
            f"🆔 ID: {user_id}"
        )
        bot.send_message(TEU_CHAT_ID, texto_admin, parse_mode="Markdown")
    except Exception as e:
        print(f"Erro ao notificar admin: {e}")

    # 3. Enviar a mensagem de boas-vindas com botões para o utilizador que deu /start
    texto_boas_vindas = (
        "🔥 BEM-VINDO AO JACKPOT ZONE!\n\n"
        "🎁 PROMOÇÃO EXCLUSIVA DE HOJE:\n"
        "➡️ Recebes mais 20€ grátis\n"
        "➡️ Mais bónus buy na slot big bass 1000\n"
        "➡️ Acesso Instantâneo à plataforma VIP\n\n"
        "👇 Clica no botão abaixo para abrir a plataforma e resgatar a tua promoção:"
    )
    
    try:
        bot.send_message(
            chat_id=user_id,
            text=texto_boas_vindas,
            parse_mode="Markdown",
            reply_markup=menu_afiliado()
        )
    except Exception as e:
        print(f"Erro ao enviar boas-vindas: {e}")

    # 4. Enviar automaticamente a postagem para o Canal
    texto_canal = (
        "🎰 JACKPOT ZONE 🎁\n\n"
        "🔥 RECURSO DE BÓNUS ADQUIRIDO!\n"
        "Deposita 20€ e recebe mais 20€ extra + bónus buy grátis na slot Big Bass 1000!"
    )
    
    try:
        # Se quiseres enviar uma foto para o canal, descomenta a linha abaixo e coloca o link/file_id da imagem:
        # bot.send_photo(chat_id=CANAL_ID, photo="URL_DA_FOTO", caption=texto_canal, parse_mode="Markdown", reply_markup=menu_afiliado())
        
        # Ou envia apenas em texto/post para o canal:
        bot.send_message(
            chat_id=CANAL_ID,
            text=texto_canal,
            parse_mode="Markdown",
            reply_markup=menu_afiliado()
        )
    except Exception as e:
        print(f"Erro ao enviar post para o canal: {e}")

# Iniciar o bot
if name == "main":
    print("Bot a iniciar...")
    bot.infinity_polling()
