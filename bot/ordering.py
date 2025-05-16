from telegram import ReplyKeyboardMarkup
import random
from bot.keyboards import get_html_practice_menu, get_java_practice_menu, get_python_practice_menu, get_main_menu, get_ordering_task_menu
from bot.states import get_user_state

# Список завдань на порядок для різних мов
RAW_ORDERING_TASKS = {
    "HTML/CSS/JS": [
    {
        "steps": [
            "Відкрити тег html",
            "Вставити тег head",
            "Додати тег body"
        ],
        "correct_order": "1-2-3",
        "title": "📝 Упорядкуйте кроки створення HTML-сторінки:"
    },
    {
        "steps": [
            "Підключити зовнішній CSS файл",
            "Написати стилі в CSS файлі",
            "Оновити HTML сторінку в браузері"
        ],
        "correct_order": "1-2-3",
        "title": "🎨 Упорядкуйте кроки для застосування стилів CSS:"
    },
    {
        "steps": [
            "Створити тег <a>",
            "Встановити атрибут href",
            "Вставити текст посилання"
        ],
        "correct_order": "1-2-3",
        "title": "🔗 Упорядкуйте кроки створення гіперпосилання в HTML:"
    },
    {
        "steps": [
            "Створити тег <script>",
            "Написати JavaScript код",
            "Вставити тег у HTML-документ"
        ],
        "correct_order": "1-2-3",
        "title": "🛠️ Упорядкуйте кроки підключення JavaScript до HTML:"
    },
    {
        "steps": [
            "Створити тег <img>",
            "Встановити атрибут src",
            "Додати альтернативний текст (alt)"
        ],
        "correct_order": "1-2-3",
        "title": "🖼️ Упорядкуйте кроки вставки зображення в HTML:"
    },
    {
        "steps": [
            "Створити тег <form>",
            "Додати поля введення (input)",
            "Додати кнопку відправки (submit)"
        ],
        "correct_order": "1-2-3",
        "title": "📨 Упорядкуйте кроки створення форми в HTML:"
    },
    {
        "steps": [
            "Створити тег <table>",
            "Додати рядки таблиці (tr)",
            "Додати комірки таблиці (td)"
        ],
        "correct_order": "1-2-3",
        "title": "📋 Упорядкуйте кроки створення таблиці в HTML:"
    },
    {
        "steps": [
            "Написати CSS селектор",
            "Визначити властивість (property)",
            "Задати значення властивості (value)"
        ],
        "correct_order": "1-2-3",
        "title": "🎨 Упорядкуйте кроки написання CSS-правила:"
    },
    {
        "steps": [
            "Написати функцію JavaScript",
            "Викликати функцію з події (onclick)",
            "Перевірити результат у браузері"
        ],
        "correct_order": "1-2-3",
        "title": "🖱️ Упорядкуйте кроки створення обробника подій в JavaScript:"
    },
    {
        "steps": [
            "Створити тег <ul>",
            "Додати елементи списку (li)",
            "Відобразити список у браузері"
        ],
        "correct_order": "1-2-3",
        "title": "📑 Упорядкуйте кроки створення маркованого списку в HTML:"
    }
],
    "Python": [
    {
        "steps": [
            "Написати код (наприклад: print('Hello'))",
            "Зберегти файл з розширенням .py",
            "Запустити програму через інтерпретатор Python"
        ],
        "correct_order": "1-2-3",
        "title": "🐍 Упорядкуйте кроки створення простої програми Python:"
    },
    {
        "steps": [
            "Імпортувати модуль (import math)",
            "Використати функцію модуля (math.sqrt())",
            "Запустити програму"
        ],
        "correct_order": "1-2-3",
        "title": "🧮 Упорядкуйте кроки використання модуля в Python:"
    },
    {
        "steps": [
            "Оголосити змінну",
            "Присвоїти значення змінній",
            "Вивести змінну на екран"
        ],
        "correct_order": "1-2-3",
        "title": "🖋 Упорядкуйте кроки для створення та використання змінної:"
    },
    {
        "steps": [
            "Відкрити файл у режимі читання (open)",
            "Зчитати дані з файлу (read)",
            "Закрити файл (close)"
        ],
        "correct_order": "1-2-3",
        "title": "📂 Упорядкуйте кроки для читання файлу в Python:"
    },
    {
        "steps": [
            "Створити функцію з def",
            "Визначити параметри функції",
            "Викликати функцію"
        ],
        "correct_order": "1-2-3",
        "title": "⚙️ Упорядкуйте кроки створення та виклику функції в Python:"
    },
    {
        "steps": [
            "Створити список",
            "Додати елемент до списку (append)",
            "Вивести список на екран"
        ],
        "correct_order": "1-2-3",
        "title": "🗂 Упорядкуйте кроки роботи зі списком в Python:"
    },
    {
        "steps": [
            "Написати цикл for",
            "Виконати тіло циклу",
            "Завершити цикл"
        ],
        "correct_order": "1-2-3",
        "title": "🔄 Упорядкуйте кроки виконання циклу for в Python:"
    },
    {
        "steps": [
            "Оголосити клас",
            "Створити метод __init__",
            "Створити екземпляр класу"
        ],
        "correct_order": "1-2-3",
        "title": "🏗 Упорядкуйте кроки створення класу в Python:"
    },
    {
        "steps": [
            "Написати умову if",
            "Перевірити умову",
            "Виконати тіло if"
        ],
        "correct_order": "1-2-3",
        "title": "🧐 Упорядкуйте кроки виконання умовного оператора if:"
    },
    {
        "steps": [
            "Імпортувати бібліотеку (import requests)",
            "Виконати HTTP запит (requests.get)",
            "Опрацювати відповідь"
        ],
        "correct_order": "1-2-3",
        "title": "🌐 Упорядкуйте кроки виконання HTTP-запиту в Python:"
    }
],
"Java": [
    {
        "steps": [
            "Написати код класу з методом main",
            "Скомпілювати файл за допомогою javac",
            "Запустити програму командою java"
        ],
        "correct_order": "1-2-3",
        "title": "☕️ Упорядкуйте кроки створення Java-програми:"
    },
    {
        "steps": [
            "Оголосити клас",
            "Оголосити змінні класу",
            "Створити методи класу"
        ],
        "correct_order": "1-2-3",
        "title": "📦 Упорядкуйте кроки створення класу в Java:"
    },
    {
        "steps": [
            "Імпортувати пакет (import java.util.*)",
            "Оголосити клас",
            "Створити об'єкт класу"
        ],
        "correct_order": "1-2-3",
        "title": "📚 Упорядкуйте кроки імпорту та використання класу в Java:"
    },
    {
        "steps": [
            "Оголосити масив",
            "Ініціалізувати масив значеннями",
            "Вивести масив на екран"
        ],
        "correct_order": "1-2-3",
        "title": "🗂 Упорядкуйте кроки роботи з масивами в Java:"
    },
    {
        "steps": [
            "Оголосити змінну типу int",
            "Присвоїти значення змінній",
            "Вивести змінну на екран"
        ],
        "correct_order": "1-2-3",
        "title": "🔢 Упорядкуйте кроки роботи зі змінною в Java:"
    },
    {
        "steps": [
            "Написати метод",
            "Визначити параметри методу",
            "Викликати метод у програмі"
        ],
        "correct_order": "1-2-3",
        "title": "⚙️ Упорядкуйте кроки створення і виклику методу в Java:"
    },
    {
        "steps": [
            "Створити цикл for",
            "Виконати тіло циклу",
            "Завершити цикл"
        ],
        "correct_order": "1-2-3",
        "title": "🔄 Упорядкуйте кроки виконання циклу for у Java:"
    },
    {
        "steps": [
            "Оголосити інтерфейс",
            "Оголосити методи інтерфейсу",
            "Реалізувати інтерфейс у класі"
        ],
        "correct_order": "1-2-3",
        "title": "🛠️ Упорядкуйте кроки створення і реалізації інтерфейсу в Java:"
    },
    {
        "steps": [
            "Оголосити конструктор класу",
            "Ініціалізувати поля класу",
            "Створити об'єкт класу за допомогою конструктора"
        ],
        "correct_order": "1-2-3",
        "title": "🏗️ Упорядкуйте кроки створення конструктора в Java:"
    },
    {
        "steps": [
            "Підключити бібліотеку (наприклад java.sql.*)",
            "Створити з'єднання з базою даних",
            "Виконати SQL-запит"
        ],
        "correct_order": "1-2-3",
        "title": "🛢️ Упорядкуйте кроки підключення до бази даних у Java:"
    }
]
}


# Функція для генерації тексту завдання з рандомізацією
def generate_ordering_task(raw_task):
    steps = raw_task["steps"]
    indices = list(range(len(steps)))
    random.shuffle(indices)

    shuffled_steps = [f"{i+1}️⃣ {steps[idx]}" for i, idx in enumerate(indices)]
    correct_order = "-".join(str(indices.index(i)+1) for i in range(len(steps)))

    text = raw_task["title"] + "\n\n" + "\n".join(shuffled_steps) + "\n\n✏️ Введіть правильний порядок у форматі 1-2-3 (наприклад: 1-3-2)"

    return text, correct_order


# Генеруємо ORDERING_TASKS з готовими текстами і правильними відповідями
ORDERING_TASKS = {}

for language, tasks in RAW_ORDERING_TASKS.items():
    ORDERING_TASKS[language] = []
    for task in tasks:
        question_text, correct_order = generate_ordering_task(task)
        ORDERING_TASKS[language].append({
            "question": question_text,
            "correct_order": correct_order
        })

async def start_ordering_task(update, context, language):
    tasks = ORDERING_TASKS.get(language)
    if tasks:
        task = random.choice(tasks)
        context.user_data["ordering_answer"] = task["correct_order"]
        await update.message.reply_text(task["question"])
    else:
        await update.message.reply_text("⚠️ Завдання для цієї мови ще не додано.")

async def handle_ordering_answer(update, context):
    user_id = update.effective_user.id
    user_input = update.message.text.strip()
    correct_answer = context.user_data.get("ordering_answer")

    
async def handle_ordering_answer(update, context):
    user_id = update.effective_user.id
    user_input = update.message.text.strip()
    correct_answer = context.user_data.get("ordering_answer")

    # Перевірка правильності вводу
    expected_set = set(correct_answer.split('-'))
    user_set = set(user_input.split('-'))

    if user_set != expected_set:
        await update.message.reply_text("⚠️ Некоректний ввід. Використовуйте числа у форматі 1-2-3 без пропусків.")
        return
    if user_input == correct_answer:
        await update.message.reply_text("✅ Правильно! Чудова робота! 🎉")
    else:
        await update.message.reply_text(f"❌ Неправильно.\nПравильна відповідь: {correct_answer}")
    
    await update.message.reply_text("⬇️ Що далі?", reply_markup=get_ordering_task_menu())