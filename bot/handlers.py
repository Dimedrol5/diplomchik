import asyncio
from telegram import Update
from telegram.ext import ContextTypes
from bot.keyboards import *
from bot.keyboards import get_java_theory_menu
from bot.states import *
from content.python_theory import python_theory_texts
from content.java_theory import java_theory_texts
from content.html_theory import html_theory_texts
from bot.quiz import start_quiz, handle_quiz_answer
from bot.ordering import start_ordering_task, handle_ordering_answer
from bot.states import increment_stat, get_user_stats_text

def clean_html(text: str) -> str:
    return text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    set_user_state(user.id, "language_selection")
    await update.message.reply_text(
        f"Привіт, {user.first_name}! 👋\nОберіть мову:",
        reply_markup=get_language_menu()
    )

async def secret_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Чи не ввели ви цю команду випадково?🤨🤨🤨")
    await asyncio.sleep(10)
    await update.message.reply_text("Нікуся, ти найкраща!❤️ \n\nЯ ніколи не бачив більш приємної і прекрасної людини за тебе")

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    text = update.message.text
    state = get_user_state(user.id)

    if not state:
        await start(update, context)
        return

    if state["state"] == "language_selection":
        if text in ["Python", "Java", "HTML/CSS/JS"]:
            set_user_state(user.id, "main_menu", text)
            await update.message.reply_text(
                f"Ви обрали {text}. Що далі?",
                reply_markup=get_main_menu()
            )
            return

        elif text == "📊 Моя статистика":
            stats_text = get_user_stats_text(user.id)
            await update.message.reply_text(stats_text, parse_mode="HTML")
            return


    elif state["state"] == "main_menu":
        language = state.get("language")

        if text == "📚 Навчання":
            set_user_state(user.id, "learning", language)
            if language == "Python":
                await update.message.reply_text("Виберіть розділ:", reply_markup=get_python_learning_menu())
            elif language == "Java":
                await update.message.reply_text("Виберіть розділ:", reply_markup=get_java_learning_menu())
            elif language == "HTML/CSS/JS":
                await update.message.reply_text("Виберіть розділ:", reply_markup=get_html_learning_menu())
            else:
                await update.message.reply_text("Матеріал для цієї мови ще не додано.")
            return

        elif text == "🧠 Практика":
            set_user_state(user.id, "practice", language)
            if language == "Python":
                await update.message.reply_text("Оберіть тип практики:", reply_markup=get_python_practice_menu())
            elif language == "Java":
                await update.message.reply_text("Оберіть тип практики:", reply_markup=get_java_practice_menu())
            elif language == "HTML/CSS/JS":
                await update.message.reply_text("Оберіть тип практики:", reply_markup=get_html_practice_menu())
            else:
                await update.message.reply_text("Практика для цієї мови ще не реалізована.")
            return

        elif text == "🔙 Назад":
            set_user_state(user.id, "language_selection", language=None)
            await update.message.reply_text("⬅️ Повернення до вибору мови.", reply_markup=get_language_menu())
            return

    elif state["state"] == "learning":
        language = state.get("language")

        if (language == "Python" and text == "📘 Теорія Python") or \
           (language == "Java" and text == "📘 Теорія Java") or \
           (language == "HTML/CSS/JS" and text == "📘 Теорія HTML/CSS/JS"):

            if language == "Python":
                set_user_state(user.id, "python_theory", language)
                await update.message.reply_text("📘 Оберіть тему:", reply_markup=get_python_theory_menu())
            elif language == "Java":
                set_user_state(user.id, "java_theory", language)
                await update.message.reply_text("📘 Оберіть тему:", reply_markup=get_java_theory_menu())
            elif language == "HTML/CSS/JS":
                set_user_state(user.id, "html_theory", language)
                await update.message.reply_text("📘 Оберіть тему:", reply_markup=get_html_theory_menu())
            return

        elif text == "🔙 Назад":
            set_user_state(user.id, "main_menu", language)
            await update.message.reply_text("⬅️ Повернення до головного меню.", reply_markup=get_main_menu())
            return

    elif state["state"] == "practice":
        language = state.get("language")

        if text == "🧩 Завдання на порядок (Drag & Drop) Python" or \
           text == "🧩 Завдання на порядок (Drag & Drop) Java" or \
           text == "🧩 Завдання на порядок (Drag & Drop) HTML/CSS/JS":
            await start_ordering_task(update, context, language)
            return

        elif text == "➡️ Наступне завдання":
            await start_ordering_task(update, context, language)
            return

        elif text == "❓ Квіз Python" or text == "❓ Квіз Java" or text == "❓ Квіз HTML/CSS/JS":
            increment_stat(user.id, language, "quiz")
            await start_quiz(update, context, language)
            return

        elif text == "🔙 Назад":
            if "ordering_answer" in context.user_data:
                if language == "Python":
                    menu = get_python_practice_menu()
                elif language == "Java":
                    menu = get_java_practice_menu()
                elif language == "HTML/CSS/JS":
                    menu = get_html_practice_menu()
                else:
                    menu = get_main_menu()

                await update.message.reply_text("⬅️ Ви повернулись до практики.", reply_markup=menu)
                context.user_data.pop("ordering_answer", None)
                return

            else:
                set_user_state(user.id, "main_menu", language)
                await update.message.reply_text(f"Ви обрали {language}. Що далі?", reply_markup=get_main_menu())
                return

        elif any(text.startswith(prefix) for prefix in ["A)", "B)", "C)"]):
            await handle_quiz_answer(update, context)
            return

        elif "ordering_answer" in context.user_data:
            await handle_ordering_answer(update, context)
            return

    elif state["state"] == "java_theory":
        if text in java_theory_texts:
            await update.message.reply_text(java_theory_texts[text], parse_mode="HTML")
            return
        elif text == "🔙 Назад":
            set_user_state(user.id, "learning", "Java")
            await update.message.reply_text("⬅️ Повернення до навчання.", reply_markup=get_java_learning_menu())
            return

    elif state["state"] == "python_theory":
        if text in python_theory_texts:
            await update.message.reply_text(python_theory_texts[text], parse_mode="HTML")
            return
        elif text == "🔙 Назад":
            set_user_state(user.id, "learning", "Python")
            await update.message.reply_text("⬅️ Повернення до навчання.", reply_markup=get_python_learning_menu())
            return

    elif state["state"] == "html_theory":
        if text in html_theory_texts:
            await update.message.reply_text(html_theory_texts[text], parse_mode="HTML")
            return
        elif text == "🔙 Назад":
            set_user_state(user.id, "learning", "HTML/CSS/JS")
            await update.message.reply_text("⬅️ Повернення до навчання.", reply_markup=get_html_learning_menu())
            return