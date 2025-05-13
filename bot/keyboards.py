from telegram import ReplyKeyboardMarkup

def get_language_menu():
    return ReplyKeyboardMarkup(
        [["Python", "Java", "HTML/CSS/JS"], ["📊 Моя статистика"]],
        resize_keyboard=True
    )

def get_main_menu():
    return ReplyKeyboardMarkup(
        [["📚 Навчання", "🧠 Практика"], ["🔙 Назад"]],
        resize_keyboard=True
    )

def get_python_learning_menu():
    return ReplyKeyboardMarkup(
        [["📘 Теорія Python"], ["🔙 Назад"]],
        resize_keyboard=True
    )

def get_java_learning_menu():
    return ReplyKeyboardMarkup(
        [["📘 Теорія Java"], ["🔙 Назад"]],
        resize_keyboard=True
    )

def get_html_learning_menu():
    return ReplyKeyboardMarkup(
        [["📘 Теорія HTML/CSS/JS"], ["🔙 Назад"]],
        resize_keyboard=True
    )

def get_python_theory_menu():
    return ReplyKeyboardMarkup(
        [
            ["🔢 Змінні та типи даних", "🔁 Цикли (for, while)"],
            ["📥 Умовні оператори", "📦 Функції"],
            ["🧱 Списки, масиви, словники", "🧮 Оператори"],
            ["🗂️ Робота з файлами", "🧪 Обробка помилок"], 
            ["🔄 Рекурсія", "⏳ Алгоритмічна складність"],
            ["🔙 Назад"]
        ],
        resize_keyboard=True
    )

def get_java_theory_menu():
    return ReplyKeyboardMarkup(
        [
            ["🔢 Змінні та типи даних", "🔁 Цикли (for, while, do-while)"],
            ["📥 Умовні оператори", "📦 Методи"],
            ["🧱 Масиви, списки, колекції", "🧮 Оператори та вирази"],
            ["🗂️ Робота з файлами", "🧪 Обробка виключень"],
            ["🔄 Рекурсія", "⏳ Складність алгоритмів"],
            ["🔙 Назад"]
        ],
        resize_keyboard=True
    )
    
def get_html_theory_menu():
    return ReplyKeyboardMarkup(
        [
            ["🔢 Змінні та типи даних", "🔁 Цикли (for, while)"],
            ["📥 Умовні оператори", "📦 Методи"],
            ["🧱 Масиви, списки, колекції", "🧮 Оператори та вирази"],
            ["🗂️ Робота з файлами", "🧪 Обробка виключень"],
            ["🔄 Рекурсія", "⏳ Складність алгоритмів"],
            ["🔙 Назад"]
        ],
        resize_keyboard=True
    )

def get_python_practice_menu():
    return ReplyKeyboardMarkup(
        [["🧩 Завдання на порядок (Drag & Drop) Python", "❓ Квіз Python"], ["🔙 Назад"]],
        resize_keyboard=True
    )

def get_java_practice_menu():
    return ReplyKeyboardMarkup(
        [["🧩 Завдання на порядок (Drag & Drop) Java", "❓ Квіз Java"], ["🔙 Назад"]],
        resize_keyboard=True
    )

def get_html_practice_menu():
    return ReplyKeyboardMarkup(
        [["🧩 Завдання на порядок (Drag & Drop) HTML/CSS/JS", "❓ Квіз HTML/CSS/JS"], ["🔙 Назад"]],
        resize_keyboard=True
    )

# ---------- Меню після завдання на порядок ----------

def get_ordering_task_menu():
    return ReplyKeyboardMarkup(
        [["➡️ Наступне завдання", "🔙 Назад"]],
        resize_keyboard=True
    )