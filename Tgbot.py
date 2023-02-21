import telebot

# створення бота
bot = telebot.TeleBot("TOKEN")

# функція, яка виконує пошук фільму за кодом
def find_movie(code):
    # тут потрібно реалізувати пошук фільму за кодом у базі даних фільмів
    movie = "The Matrix"
    return movie

# відповідь на повідомлення з кодом фільму
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Привіт! Введіть код фільму:")

# обробка повідомлення з кодом фільму
@bot.message_handler(func=lambda message: True)
def send_movie(message):
    movie_code = message.text
    movie = find_movie(movie_code)
    bot.reply_to(message, movie)

# запуск бота
bot.polling()
