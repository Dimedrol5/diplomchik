import sqlite3

conn = sqlite3.connect("bot.db")
cursor = conn.cursor()

# Таблиця для станів користувача
cursor.execute("""
CREATE TABLE IF NOT EXISTS user_states (
    user_id INTEGER PRIMARY KEY,
    state TEXT,
    language TEXT
)
""")

# 📊 Таблиця для статистики
cursor.execute("""
CREATE TABLE IF NOT EXISTS user_stats (
    user_id INTEGER,
    language TEXT,
    stat_type TEXT,
    count INTEGER,
    quiz_correct INTEGER DEFAULT 0,
    quiz_total INTEGER DEFAULT 0,
    PRIMARY KEY (user_id, language, stat_type)
)
""")

conn.commit()

# ----------------- STATE ФУНКЦІЇ -------------------

def set_user_state(user_id: int, state: str, language: str = None):
    # Отримати поточну мову, якщо language не передано
    if language is None:
        cursor.execute("SELECT language FROM user_states WHERE user_id = ?", (user_id,))
        result = cursor.fetchone()
        language = result[0] if result else None

    cursor.execute(
        "INSERT OR REPLACE INTO user_states VALUES (?, ?, ?)",
        (user_id, state, language)
    )
    conn.commit()

def get_user_state(user_id: int):
    cursor.execute("SELECT state, language FROM user_states WHERE user_id = ?", (user_id,))
    result = cursor.fetchone()
    return {"state": result[0], "language": result[1]} if result else None

# ----------------- 📊 СТАТИСТИКА ФУНКЦІЇ -------------------

def init_user_stats(user_id):
    languages = ["Python", "Java", "HTML/CSS/JS"]
    stat_types = ["quiz", "ordering"]
    for lang in languages:
        for stat in stat_types:
            cursor.execute("""
                INSERT OR IGNORE INTO user_stats (user_id, language, stat_type, count, quiz_correct, quiz_total)
                VALUES (?, ?, ?, 0, 0, 0)
            """, (user_id, lang, stat))
    conn.commit()

def increment_stat(user_id, language, stat_type):
    init_user_stats(user_id)
    cursor.execute("""
        UPDATE user_stats
        SET count = count + 1
        WHERE user_id = ? AND language = ? AND stat_type = ?
    """, (user_id, language, stat_type))
    conn.commit()

def increment_quiz_stats(user_id, language, correct, total):
    init_user_stats(user_id)
    cursor.execute("""
        UPDATE user_stats
        SET quiz_correct = quiz_correct + ?,
            quiz_total = quiz_total + ?
        WHERE user_id = ? AND language = ? AND stat_type = 'quiz'
    """, (correct, total, user_id, language))
    conn.commit()

def get_user_stats_text(user_id):
    init_user_stats(user_id)
    cursor.execute("""
        SELECT language, stat_type, count, quiz_correct, quiz_total
        FROM user_stats
        WHERE user_id = ?
    """, (user_id,))
    rows = cursor.fetchall()

    # Структуруємо результати
    stats = {
        "Python": {"quiz": 0, "ordering": 0, "quiz_correct": 0, "quiz_total": 0},
        "Java": {"quiz": 0, "ordering": 0, "quiz_correct": 0, "quiz_total": 0},
        "HTML/CSS/JS": {"quiz": 0, "ordering": 0, "quiz_correct": 0, "quiz_total": 0}
    }

    for lang, stat_type, count, quiz_correct, quiz_total in rows:
        stats[lang][stat_type] = count
        if stat_type == "quiz":
            stats[lang]["quiz_correct"] = quiz_correct
            stats[lang]["quiz_total"] = quiz_total

    # Генеруємо текст
    text = "📊 <b>Ваша статистика:</b>\n\n"
    for lang, data in stats.items():
        text += f"🔹 <b>{lang}</b>\n"
        text += f"   🧩 Завдань на порядок: {data['ordering']}\n"
        text += f"   ❓ Квізів пройдено: {data['quiz']}\n"
        if data['quiz_total'] > 0:
            avg_score = int((data['quiz_correct'] / data['quiz_total']) * 100)
            text += f"   📈 Середній бал квізів: {avg_score}%\n\n"
        else:
            text += f"   📈 Середній бал квізів: 0%\n\n"

    return text