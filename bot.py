import telebot
from telebot import types

# 🔹 Telegram Bot Token (GitHub Secrets မှာ ထည့်ထားရမယ်)
import os
BOT_TOKEN = os.getenv("7943930374:AAGH_fuU2ycZBL8muVum-9r-9nIjKks-F98")

bot = telebot.TeleBot(BOT_TOKEN)

# 📌 Bot Start Command
@bot.message_handler(commands=['start'])
def start_message(message):
    bot.reply_to(message, "🎬 မင်္ဂလာပါ! Movies Myanmar Bot မှာ ကြိုဆိုပါတယ်။\n\n🔍 မိမိလိုချင်သော ဇာတ်ကားနာမည်ကို ရိုက်ထည့်ပြီး ရှာဖွေနိုင်ပါသည်။")

# 📌 Movie Name ရိုက်လိုက်တာနဲ့ ချန်နယ်ကနေ တင်ပေးမယ့် Function
@bot.message_handler(func=lambda message: True)
def search_movie(message):
    movie_name = message.text.strip()
    if not movie_name:
        bot.reply_to(message, "⚠️ ဇာတ်ကားနာမည်ကို ရိုက်ထည့်ပါ။")
        return
    
    # 🔹 Telegram Channel ID (🔻သင့် Channel ID/Username ထည့်ပါ)
    CHANNEL_ID = "@WinPyaeKyaw0078"
    
    # 🔹 Forwarding Messages (Channel Name မပါအောင်)
    forwarded_messages = bot.forward_message(message.chat.id, CHANNEL_ID, message.message_id, disable_notification=True)

    if forwarded_messages:
        bot.reply_to(message, f"✅ '{movie_name}' ကို တွေ့ရှိခဲ့ပါသည်။ ကြည့်ရှုနိုင်ပါသည်။")
    else:
        bot.reply_to(message, f"❌ '{movie_name}' ကို မတွေ့ရှိပါ။")

# 🔹 Bot ကို Run ချမယ်
print("🚀 Bot is running...")
bot.polling()
