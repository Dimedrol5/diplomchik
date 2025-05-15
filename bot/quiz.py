from telegram import ReplyKeyboardMarkup
from bot.states import increment_quiz_stats, get_user_state
import random

async def start_quiz(update, context, language):
    quiz = random.choice(QUIZ_QUESTION[language])


QUIZ_QUESTION = {
    "Python": [],
    "Java": [],
    "HTML/CSS/JS": []
}

# Питання для Python
python_questions = [
    {
        "question": "❓ Що робить функція len() у Python?",
        "options": ["Повертає довжину об'єкта", "Виводить текст", "Завершує програму"],
        "answer": "Повертає довжину об'єкта",
        "explanation": "✅ Правильно! len() повертає довжину (кількість елементів) об'єкта."
    },
    {
        "question": "❓ Як створити список у Python?",
        "options": ["list = []", "list = {}", "list = ()"],
        "answer": "list = []",
        "explanation": "✅ Правильно! Списки створюються з допомогою квадратних дужок []."
    },
    {
        "question": "❓ Який тип даних повертає функція input()?",
        "options": ["str", "int", "bool"],
        "answer": "str",
        "explanation": "✅ Правильно! input() завжди повертає рядок (str)."
    },
    {
        "question": "❓ Що робить оператор ==?",
        "options": ["Перевіряє рівність", "Присвоює значення", "Порівнює типи"],
        "answer": "Перевіряє рівність",
        "explanation": "✅ Правильно! == перевіряє чи рівні значення."
    },
    {
        "question": "❓ Як зробити цикл від 0 до 4 у Python?",
        "options": ["for i in range(5)", "for i in range(4)", "for i in range(1,5)"],
        "answer": "for i in range(5)",
        "explanation": "✅ Правильно! range(5) генерує числа 0,1,2,3,4."
    },
    {
        "question": "❓ Як викликати функцію my_func()?",
        "options": ["my_func()", "call my_func", "my_func"],
        "answer": "my_func()",
        "explanation": "✅ Правильно! Функція викликається як my_func()."
    },
    {
        "question": "❓ Що повертає type(123)?",
        "options": ["<class 'int'>", "<class 'float'>", "<class 'str'>"],
        "answer": "<class 'int'>",
        "explanation": "✅ Правильно! Це тип int (ціле число)."
    },
    {
        "question": "❓ Як оголосити змінну зі значенням 5?",
        "options": ["x = 5", "int x = 5", "var x = 5"],
        "answer": "x = 5",
        "explanation": "✅ Правильно! Python не потребує вказання типу — просто x = 5."
    },
    {
        "question": "❓ Як імпортувати модуль math?",
        "options": ["import math", "using math", "include math"],
        "answer": "import math",
        "explanation": "✅ Правильно! import math — це стандарт імпорту модуля."
    },
    {
        "question": "❓ Який результат вираза 2 ** 3?",
        "options": ["8", "6", "9"],
        "answer": "8",
        "explanation": "✅ Правильно! 2 ** 3 = 2 в степені 3 = 8."
    }
]

# Питання для Java
java_questions = [
    {
        "question": "❓ Як оголосити ціле число в Java?",
        "options": ["int x = 5;", "integer x = 5;", "var x = 5;"],
        "answer": "int x = 5;",
        "explanation": "✅ Правильно! Для оголошення цілого числа використовується int x = 5;."
    },
    {
        "question": "❓ Яке ключове слово використовується для створення класу в Java?",
        "options": ["class", "struct", "object"],
        "answer": "class",
        "explanation": "✅ Правильно! Класи оголошуються з ключовим словом class."
    },
    {
        "question": "❓ Який оператор використовується для порівняння значень у Java?",
        "options": ["==", "=", "equals"],
        "answer": "==",
        "explanation": "✅ Правильно! Оператор == використовується для порівняння значень примітивних типів."
    },
    {
        "question": "❓ Як почати головний метод (main) у Java програмі?",
        "options": ["public static void main(String[] args)", "void main()", "static main(String args)"],
        "answer": "public static void main(String[] args)",
        "explanation": "✅ Правильно! Це стандартне оголошення методу main в Java."
    },
    {
        "question": "❓ Як створити новий об'єкт класу MyClass?",
        "options": ["MyClass obj = new MyClass();", "MyClass obj;", "new MyClass obj();"],
        "answer": "MyClass obj = new MyClass();",
        "explanation": "✅ Правильно! Новий об'єкт створюється через new MyClass();."
    },
    {
        "question": "❓ Який оператор використовується для виклику методу або доступу до поля об'єкта?",
        "options": [". (крапка)", ":: (подвійна двокрапка)", "-> (стрілка)"],
        "answer": ". (крапка)",
        "explanation": "✅ Правильно! В Java для доступу до методів чи полів використовується крапка (.)."
    },
    {
        "question": "❓ Який тип даних використовується для зберігання символів?",
        "options": ["char", "string", "Character"],
        "answer": "char",
        "explanation": "✅ Правильно! Символи зберігаються в типі char."
    },
    {
        "question": "❓ Яке ключове слово використовується для наслідування класу?",
        "options": ["extends", "implements", "inherits"],
        "answer": "extends",
        "explanation": "✅ Правильно! Наслідування реалізується через ключове слово extends."
    },
    {
        "question": "❓ Як створити нескінченний цикл у Java?",
        "options": ["while(true)", "for(;;)", "do {} while(true)"],
        "answer": "while(true)",
        "explanation": "✅ Правильно! while(true) створює нескінченний цикл (як і for(;;) та інші варіанти)."
    },
    {
        "question": "❓ Який результат виразу 5 + 3 * 2 у Java?",
        "options": ["11", "16", "13"],
        "answer": "11",
        "explanation": "✅ Правильно! Операції виконуються згідно з порядком: 3 * 2 = 6, потім 5 + 6 = 11."
    }
]

# Питання для HTML/CSS/JS
html_questions = [
    {
        "question": "❓ Який тег використовується для створення гіперпосилання в HTML?",
        "options": ["<a>", "<link>", "<href>"],
        "answer": "<a>",
        "explanation": "✅ Правильно! Тег <a> використовується для створення гіперпосилань."
    },
    {
        "question": "❓ Як вставити зображення на вебсторінку в HTML?",
        "options": ["<img src='image.jpg'>", "<image src='image.jpg'>", "<src img='image.jpg'>"],
        "answer": "<img src='image.jpg'>",
        "explanation": "✅ Правильно! Для вставки зображень використовується тег <img> із атрибутом src."
    },
    {
        "question": "❓ Яке CSS властивість використовується для зміни кольору тексту?",
        "options": ["color", "background-color", "text-color"],
        "answer": "color",
        "explanation": "✅ Правильно! Властивість color змінює колір тексту."
    },
    {
        "question": "❓ Який метод використовується в JavaScript для виводу повідомлення у вікно браузера?",
        "options": ["alert()", "console.log()", "prompt()"],
        "answer": "alert()",
        "explanation": "✅ Правильно! alert() виводить повідомлення у вигляді спливаючого вікна."
    },
    {
        "question": "❓ Який тег використовується для створення нумерованого списку в HTML?",
        "options": ["<ol>", "<ul>", "<li>"],
        "answer": "<ol>",
        "explanation": "✅ Правильно! Тег <ol> створює нумерований список."
    },
    {
        "question": "❓ Як в JavaScript перевірити чи значення змінної x дорівнює 5?",
        "options": ["if (x === 5)", "if (x == 5)", "if (x = 5)"],
        "answer": "if (x === 5)",
        "explanation": "✅ Правильно! === перевіряє як значення, так і тип змінної."
    },
    {
        "question": "❓ Яке CSS властивість використовується для встановлення фону елемента?",
        "options": ["background-color", "color", "border-color"],
        "answer": "background-color",
        "explanation": "✅ Правильно! background-color задає колір фону елемента."
    },
    {
        "question": "❓ Який оператор використовується для конкатенації (з'єднання) рядків у JavaScript?",
        "options": ["+", "&", "."],
        "answer": "+",
        "explanation": "✅ Правильно! Оператор + використовується для з'єднання рядків у JavaScript."
    },
    {
        "question": "❓ Який HTML тег використовується для найважливішого заголовка?",
        "options": ["<h1>", "<header>", "<heading>"],
        "answer": "<h1>",
        "explanation": "✅ Правильно! <h1> — це найважливіший (найвищий рівень) заголовок."
    },
    {
        "question": "❓ Як підключити зовнішній CSS файл до HTML документу?",
        "options": ["<link rel='stylesheet' href='style.css'>", "<style src='style.css'>", "<css link='style.css'>"],
        "answer": "<link rel='stylesheet' href='style.css'>",
        "explanation": "✅ Правильно! Для підключення зовнішнього CSS-файлу використовується тег <link> з атрибутами rel і href."
    }
]

# Додаємо питання в словник
all_questions = {
    "Python": python_questions,
    "Java": java_questions,
    "HTML/CSS/JS": html_questions
}


for category, questions in all_questions.items():
    for raw_q in questions:
        options = raw_q["options"].copy()
        random.shuffle(options)

        # Знаходимо правильну відповідь після перемішування
        correct_option = raw_q["answer"]
        labeled_options = [f"{chr(65 + i)}) {opt}" for i, opt in enumerate(options)]
        correct_index = options.index(correct_option)
        answer = labeled_options[correct_index]

        QUIZ_QUESTION[category].append({
            "question": raw_q["question"],
            "options": labeled_options,
            "answer": answer,
            "explanation": raw_q["explanation"]
        })

# Скільки питань показувати
QUIZ_QUESTION_COUNT = 10

def get_quiz_keyboard(options):
    return ReplyKeyboardMarkup([[opt] for opt in options] + [["🔙 Назад"]], resize_keyboard=True)

async def start_quiz(update, context, language):
    # Перемішуємо питання і беремо до 10
    questions = random.sample(QUIZ_QUESTION[language], k=min(QUIZ_QUESTION_COUNT, len(QUIZ_QUESTION[language])))

    # Зберігаємо в контекст
    context.user_data["quiz_questions"] = questions
    context.user_data["quiz_index"] = 0
    context.user_data["quiz_correct"] = 0  # лічильник правильних відповідей

    await send_next_question(update, context)

async def send_next_question(update, context):
    index = context.user_data.get("quiz_index", 0)
    questions = context.user_data.get("quiz_questions", [])

    if index < len(questions):
        quiz = questions[index]
        await update.message.reply_text(
            quiz["question"],
            reply_markup=get_quiz_keyboard(quiz["options"])
        )
        context.user_data["quiz_answer"] = quiz["answer"]
        context.user_data["quiz_explanation"] = quiz["explanation"]
    else:
        await show_quiz_summary(update, context)

async def handle_quiz_answer(update, context):
    user_answer = update.message.text
    correct_answer = context.user_data.get("quiz_answer")
    explanation = context.user_data.get("quiz_explanation")

    if user_answer == correct_answer:
        await update.message.reply_text(f"{explanation}")
        context.user_data["quiz_correct"] += 1
    else:
        await update.message.reply_text(f"Правильна відповідь: {correct_answer}\n{explanation}")

    context.user_data["quiz_index"] += 1
    await send_next_question(update, context)

async def show_quiz_summary(update, context):
    correct = context.user_data.get("quiz_correct", 0)
    total = len(context.user_data.get("quiz_questions", []))

    # Записуємо статистику
    user_id = update.effective_user.id
    language = get_user_state(user_id).get("language")
    increment_quiz_stats(user_id, language, correct, total)

    # Визначаємо оцінку
    if correct <= total * 0.4:
        comment = "😕 Ви могли б краще. Попрактикуйтесь ще!"
    elif correct <= total * 0.7:
        comment = "🙂 Непогано! Але є куди рости."
    else:
        comment = "🎉 Відмінно! Ви чудово впорались!"

    await update.message.reply_text(f"📊 Підсумок вікторини:\nПравильних відповідей: {correct} з {total}\n\n{comment}")

    # Чистимо контекст
    keys_to_clear = ["quiz_questions", "quiz_index", "quiz_correct", "quiz_answer", "quiz_explanation"]
    for key in keys_to_clear:
        context.user_data.pop(key, None)
