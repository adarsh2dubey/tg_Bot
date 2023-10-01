
import os
import random
import time
import telebot
from pytube import YouTube
import ctypes

# List of inspirational quotes
quotes = [
    "The only way to do great work is to love what you do. - Steve Jobs",
    "Success is not final, failure is not fatal: It is the courage to continue that counts. - Winston Churchill",
    "Believe you can and you're halfway there. - Theodore Roosevelt",
    "In the middle of every difficulty lies opportunity. - Albert Einstein",
    "The only thing that stands between you and your dream is the will to try and the belief that it is actually possible. - Joel Brown",
    "Don't watch the clock; do what it does. Keep going. - Sam Levenson",
    "You are never too old to set another goal or to dream a new dream. - C.S. Lewis",
    "The future belongs to those who believe in the beauty of their dreams. - Eleanor Roosevelt"
    "कर्मण्येवाधिकारस्ते मा फलेषु कदाचन। - श्रीमद् भगवद गीता",
    "योगस्थः कुरु कर्माणि संगं त्यक्त्वा धनंजय। - श्रीमद् भगवद गीता",
    "श्रेयान्स्वधर्मो विगुणः परधर्मात्स्वनुष्ठितात्। - श्रीमद् भगवद गीता"
]

jokes=[
    "अगर किसी लड़की का नाम खुशी हो और वह रो रही हो, तो कोई गंभीरता से नहीं लेगा! क्योंकि लोग सोचेंगे- 'ये खुशी के आंसू' हैं।",
    "अगर श्रीदेवी अपना एक शोरूम खोलें, तो वह कहेंगी, 'अभी 'बोनी' का टाइम है!",
    "बड़ा अच्छा लगता है जब-जब सोनी का फोन हैंग होता है, क्योंकि- 'सोनी के नखरे सोणे लग दे मैनू...",
    "एक क्रिकेट टीम के जब सारे प्लेयर आउट हो जाते हैं, तो सारे मच्छर भाग जाते हैं। \n . \n. \n. \n.  सोचो सोचो क्यों... \n . \n. \n. \n. \n. क्योंकि टीम 'ऑल आउट' है न! ",
     "Why did the scarecrow win an award? Because he was outstanding in his field!",
    "What do you call a bear with no teeth? A gummy bear!",
    "Why don't scientists trust atoms? Because they make up everything!",
    "How does a penguin build its house? Igloos it together!",
    "What do you call a fish with no eyes? Fsh!",
    "Why did the bicycle fall over? Because it was two-tired!",
    "What's orange and sounds like a parrot? A carrot!"
]
BOT_TOKEN = "6454257657:AAG7nV4TfjRCmE3Z_rtf-zA5KfAGfTg5vTo"
INSTAGRAM_PROFILE = "https://www.instagram.com/adarsh_.dubey_/"  # Replace with your Instagram profile URL
max_attempts =200
interval = 2 
bot = telebot.TeleBot(BOT_TOKEN)
exist_file='adarsh'
@bot.message_handler(commands=['start', 'hello'])
def send_welcome(message):
    bot.reply_to(message, "Howdy, how are you doing?")

@bot.message_handler(commands=['admin'])
def get_admin_name(message):
    bot.reply_to(message, "The admin of this bot is Adarsh Dubey.")

@bot.message_handler(commands=['quote','quotes','kotes','qote'])
def send_random_quote(message):
    # Get a random quote from the list
    random_quote = random.choice(quotes)
    
    # Send the random quote to the user
    bot.reply_to(message, random_quote)

@bot.message_handler(commands=['joke'])
def send_random_joke(message):
    # Get a random joke from the list
    random_joke = random.choice(jokes)
    bot.reply_to(message, random_joke)

@bot.message_handler(func=lambda msg: True)
def handle_message(message):
    global exist_file
    if message.text.startswith("https://www.youtube.com/") or message.text.startswith("https://youtu.be/"):
        try:
            if exist_file != 'adarsh':
                os.remove(exist_file)
             

            # Download the audio from the YouTube video
            yt = YouTube(message.text)
            stream = yt.streams.filter(only_audio=True).first()
            audio_file = stream.download()
            # Send the audio as a voice message
            audio = open(audio_file, 'rb')
            bot.send_voice(message.chat.id, audio)
            bot.reply_to(message, f"If you also want to create such type of bot for free, Dm me @ {INSTAGRAM_PROFILE}.")

            audio_filename = os.path.basename(audio_file)
            exist_file=audio_filename
           
        
        except Exception as e:
            print(e)
            bot.reply_to(message, "An error occurred.. try again...")
    else:
        bot.reply_to(message, f"I can only process YouTube video URLs.. If you are still facing issue, You can find me on [Instagram]({INSTAGRAM_PROFILE}).")

def force_remove_windows(file_path):
 # Wait for 2 seconds between attempts

    for _ in range(max_attempts):
        try:
            os.remove(file_path)
            print(f"File '{file_path}' removed successfully.")
            break  # Exit the loop if deletion is successful
        except OSError as e:
            print(f"Error: {e}")
            time.sleep(interval)
    else:
        print(f"Unable to remove the file after {max_attempts} attempts.")

bot.polling()
