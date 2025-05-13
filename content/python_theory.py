python_theory_texts = {
    "🔢 Змінні та типи даних": (
    "<b>Змінні</b> — це іменовані комірки памʼяті для зберігання значень.\n\n"
    "У Python <b>не потрібно вказувати тип явно</b> — він визначається автоматично.\n"
    "<pre><code class='language-python'>age = 25\nname = \"Anna\"\npi = 3.14\nis_active = True</code></pre>\n"
    "<b>Основні типи даних:</b>\n"
    "• <code>int</code> — цілі числа (25)\n"
    "• <code>float</code> — дробові числа (3.14)\n"
    "• <code>str</code> — рядки (\"Hello\")\n"
    "• <code>bool</code> — логічні значення (True/False)\n"
    "• <code>list</code> — списки ([1, 2, 3])\n"
    "• <code>dict</code> — словники ({'key': 'value'})\n"
    "• <code>None</code> — відсутність значення\n\n"
    "<b>Перевірка типу:</b> <code>type(value)</code>\n"
    "<pre><code class='language-python'>print(type(age))  # &lt;class 'int'&gt;</code></pre>\n\n"
    "<b>Python — мова з динамічною типізацією:</b> тип змінної може змінюватися в процесі виконання."
),
"🔁 Цикли (for, while)": (
    "<b>Цикли</b> дозволяють багаторазово виконувати блок коду.\n\n"
    "<b>Цикл for:</b> використовується для проходу по колекціях чи діапазону чисел.\n"
    "<pre><code class='language-python'>for i in range(1, 6):\n    print(\"Крок:\", i)</code></pre>\n"
    "• <code>range(start, stop)</code> генерує послідовність чисел\n\n"
    "<b>Цикл while:</b> виконується, поки умова істинна.\n"
    "<pre><code class='language-python'>count = 0\nwhile count &lt; 3:\n    print(\"Лічильник:\", count)\n    count += 1</code></pre>\n\n"
    "<b>Корисні оператори в циклах:</b>\n"
    "• <code>break</code> — зупиняє цикл достроково\n"
    "• <code>continue</code> — переходить до наступної ітерації\n"
    "• <code>else</code> — виконується після завершення циклу, якщо не було break\n\n"
    "<b>Приклад break/continue:</b>\n"
    "<pre><code class='language-python'>for i in range(5):\n    if i == 3:\n        break\n    print(i)</code></pre>\n"
    "<pre><code class='language-python'>for i in range(5):\n    if i == 2:\n        continue\n    print(i)</code></pre>\n\n"
    "<b>Цикл for по списку:</b>\n"
    "<pre><code class='language-python'>names = [\"Anna\", \"Oleh\", \"Ira\"]\nfor name in names:\n    print(name)</code></pre>"
),
"📥 Умовні оператори": (
    "<b>Умовні оператори</b> дозволяють виконувати різний код залежно від умови.\n\n"
    "<b>if, elif, else:</b>\n"
    "<pre><code class='language-python'>age = 18\nif age &gt;= 18:\n    print(\"Дорослий\")\nelif age &gt;= 13:\n    print(\"Підліток\")\nelse:\n    print(\"Дитина\")</code></pre>\n\n"
    "• Умови записуються за допомогою операторів порівняння: <code>==</code>, <code>!=</code>, <code>&gt;</code>, <code>&lt;</code>, <code>&gt;=</code>, <code>&lt;=</code>\n"
    "• Можна об'єднувати умови логічними операторами: <code>and</code>, <code>or</code>, <code>not</code>\n\n"
    "<b>Приклад з and / or:</b>\n"
    "<pre><code class='language-python'>score = 75\nif score &gt;= 50 and score &lt; 100:\n    print(\"Склав тест\")</code></pre>\n"
    "<pre><code class='language-python'>color = \"red\"\nif color == \"red\" or color == \"blue\":\n    print(\"Це червоний або синій\")</code></pre>\n\n"
    "<b>Тернарний оператор (коротка форма if):</b>\n"
    "<pre><code class='language-python'>age = 20\nstatus = \"Дорослий\" if age &gt;= 18 else \"Дитина\"\nprint(status)</code></pre>\n\n"
    "<i>Памʼятайте:</i> відступ (4 пробіли) визначає блок коду в Python!"
),
    "📦 Функції": (
    "<b>Методи</b> (або функції) — це блоки коду, які можна викликати багаторазово.\n\n"
    "<b>Оголошення функції:</b>\n"
    "<pre><code class='language-python'>def greet(name):\n    print(f\"Привіт, {name}!\")\n\ngreet(\"Анна\")</code></pre>\n\n"
    "• <code>def</code> — ключове слово для створення функції\n"
    "• Параметри вказуються у дужках\n"
    "• Відступ визначає тіло функції\n\n"
    "<b>Функція з поверненням значення:</b>\n"
    "<pre><code class='language-python'>def add(a, b):\n    return a + b\n\nresult = add(3, 5)\nprint(result)</code></pre>\n\n"
    "<b>Параметри за замовчуванням:</b>\n"
    "<pre><code class='language-python'>def greet(name=\"Гість\"):\n    print(f\"Привіт, {name}!\")\n\ngreet()  # Виведе: Привіт, Гість!</code></pre>\n\n"
    "<b>Іменовані аргументи:</b>\n"
    "<pre><code class='language-python'>def info(name, age):\n    print(f\"{name}, {age} років\")\n\ninfo(age=30, name=\"Олег\")</code></pre>\n\n"
    "<b>Анонімні функції (lambda):</b>\n"
    "<pre><code class='language-python'>square = lambda x: x * x\nprint(square(4))  # 16</code></pre>\n\n"
    "<i>Методи допомагають організувати код, робити його зрозумілішим і повторно використовуваним.</i>"
),
    "🧱 Списки, масиви, словники": (
    "<b>У Python</b> найчастіше використовуються <b>списки</b> (lists) для зберігання колекцій елементів.\n\n"
    "<b>Список (list):</b>\n"
    "<pre><code class='language-python'>nums = [1, 2, 3, 4]\nprint(nums[0])  # 1</code></pre>\n"
    "• Динамічний розмір — можна додавати та видаляти елементи\n"
    "• Може містити елементи різних типів\n\n"
    "<b>Основні операції зі списками:</b>\n"
    "<pre><code class='language-python'>nums.append(5)  # Додати елемент\nnums.remove(2)  # Видалити елемент\nlen(nums)      # Довжина списку\nnums[1] = 10   # Заміна елементу</code></pre>\n\n"
    "<b>Кортежі (tuple):</b> незмінні списки\n"
    "<pre><code class='language-python'>coordinates = (10, 20)\nprint(coordinates[0])</code></pre>\n"
    "• Не можна змінювати після створення\n\n"
    "<b>Множини (set):</b> унікальні елементи\n"
    "<pre><code class='language-python'>unique = {1, 2, 3}\nunique.add(4)</code></pre>\n"
    "• Не зберігає порядок\n"
    "• Автоматично видаляє дублікати\n\n"
    "<b>Словники (dict):</b> пари ключ-значення\n"
    "<pre><code class='language-python'>person = {\"name\": \"Анна\", \"age\": 25}\nprint(person[\"name\"])</code></pre>\n"
    "• Дуже зручні для зберігання повʼязаних даних\n\n"
    "<i>Колекції дозволяють ефективно працювати з групами даних у Python.</i>"
),
    "🧮 Оператори": (
    "<b>Оператори</b> дозволяють виконувати різні дії над змінними та значеннями у Python.\n\n"

    "<b>Арифметичні оператори:</b>\n"
    "<pre><code class='language-python'>a = 10\nb = 3\nprint(a + b)   # 13\nprint(a - b)   # 7\nprint(a * b)   # 30\nprint(a / b)   # 3.333\nprint(a // b)  # 3 (цілочисельне ділення)\nprint(a % b)   # 1 (остача)\nprint(a ** b)  # 1000 (ступінь)</code></pre>\n\n"

    "<b>Оператори порівняння:</b>\n"
    "<pre><code class='language-python'>x = 5\ny = 10\nprint(x == y)  # False\nprint(x != y)  # True\nprint(x &lt; y)   # True\nprint(x &gt;= y)  # False</code></pre>\n\n"

    "<b>Логічні оператори:</b>\n"
    "<pre><code class='language-python'>a = True\nb = False\nprint(a and b)  # False\nprint(a or b)   # True\nprint(not a)    # False</code></pre>\n\n"

    "<b>Оператори присвоєння:</b>\n"
    "<pre><code class='language-python'>x = 5\nx += 3  # x = x + 3 → 8\nx *= 2  # x = x * 2 → 16</code></pre>\n\n"

    "<b>Комбіновані вирази:</b>\n"
    "<pre><code class='language-python'>age = 25\nif age &gt;= 18 and age &lt; 65:\n    print(\"Дорослий\")</code></pre>\n\n"

    "<i>Вирази — це комбінації змінних, значень та операторів, які повертають результат.</i>"
),
    "🗂️ Робота з файлами": (
    "<b>Робота з файлами</b> дозволяє читати і записувати дані у зовнішні файли.\n\n"

    "<b>Відкриття та читання файлу:</b>\n"
    "<pre><code class='language-python'>with open(\"data.txt\", \"r\", encoding=\"utf-8\") as file:\n    content = file.read()\n    print(content)</code></pre>\n"
    "• <code>\"r\"</code> — режим читання (read)\n"
    "• <code>with</code> — автоматично закриває файл після завершення\n\n"

    "<b>Читання рядок за рядком:</b>\n"
    "<pre><code class='language-python'>with open(\"data.txt\", \"r\", encoding=\"utf-8\") as file:\n    for line in file:\n        print(line.strip())</code></pre>\n\n"

    "<b>Запис у файл (перезапис):</b>\n"
    "<pre><code class='language-python'>with open(\"output.txt\", \"w\", encoding=\"utf-8\") as file:\n    file.write(\"Привіт, світ!\")</code></pre>\n"
    "• <code>\"w\"</code> — режим запису (write), видаляє старий вміст\n\n"

    "<b>Додавання до файлу (append):</b>\n"
    "<pre><code class='language-python'>with open(\"output.txt\", \"a\", encoding=\"utf-8\") as file:\n    file.write(\"\\nНовий рядок\")</code></pre>\n\n"

    "<b>Перевірка існування файлу:</b>\n"
    "<pre><code class='language-python'>import os\nif os.path.exists(\"data.txt\"):\n    print(\"Файл існує\")</code></pre>\n\n"

    "<i>Порада:</i> Завжди використовуйте <code>with open(...)</code> — це безпечніше, бо файл гарантовано закриється навіть у разі помилки."
),
    "🧪 Обробка помилок": (
    "<b>Обробка помилок</b> дозволяє ловити та обробляти помилки під час виконання програми.\n\n"

    "<b>Базовий try-except:</b>\n"
    "<pre><code class='language-python'>try:\n    result = 10 / 0\nexcept ZeroDivisionError:\n    print(\"Помилка: ділення на нуль\")</code></pre>\n\n"

    "<b>Обробка кількох типів помилок:</b>\n"
    "<pre><code class='language-python'>try:\n    number = int(\"abc\")\nexcept ValueError:\n    print(\"Це не число\")\nexcept Exception as e:\n    print(\"Інша помилка:\", e)</code></pre>\n"
    "• <code>Exception</code> — базовий клас для всіх винятків\n\n"

    "<b>finally — виконується завжди:</b>\n"
    "<pre><code class='language-python'>try:\n    file = open(\"data.txt\")\nexcept FileNotFoundError:\n    print(\"Файл не знайдено\")\nfinally:\n    print(\"Операція завершена\")</code></pre>\n\n"

    "<b>Викидання власного винятку:</b>\n"
    "<pre><code class='language-python'>def divide(a, b):\n    if b == 0:\n        raise ValueError(\"b не може бути 0\")\n    return a / b</code></pre>\n\n"

    "<b>Навіщо це потрібно?</b>\n"
    "• Запобігти аварійному завершенню програми\n"
    "• Надати користувачу зрозуміле повідомлення про помилку\n"
    "• Гарантувати закриття файлів, ресурсів тощо\n\n"

    "<i>Порада:</i> Не ловуйте <code>Exception</code> без потреби — ловіть конкретні помилки для кращого контролю."
),
"🔄 Рекурсія": (
    "<b>Рекурсія</b> — це техніка програмування, коли функція викликає сама себе для розв'язання підзадачі.\n\n"

    "<b>Приклад рекурсії (факторіал):</b>\n"
    "<pre><code class='language-python'>def factorial(n):\n    if n == 0:\n        return 1\n    return n * factorial(n - 1)\n\nprint(factorial(5))  # 120</code></pre>\n\n"

    "<b>Ключові поняття:</b>\n"
    "• <b>Базовий випадок</b> — умова завершення рекурсії (зупиняє виклики)\n"
    "• <b>Рекурсивний випадок</b> — виклик функції сама себе з новими аргументами\n\n"

    "<b>Приклад рекурсії (Фібоначчі):</b>\n"
    "<pre><code class='language-python'>def fib(n):\n    if n &lt;= 1:\n        return n\n    return fib(n - 1) + fib(n - 2)\n\nprint(fib(6))  # 8</code></pre>\n\n"

    "<b>Переваги рекурсії:</b>\n"
    "• Зручно для задач на дерева, графи, комбінації\n"
    "• Код стає коротким і зрозумілим для рекурсивних задач\n\n"

    "<b>Недоліки:</b>\n"
    "• Висока витрата памʼяті при великій глибині (StackOverflow)\n"
    "• Іноді повільніше за ітераційні рішення\n\n"

    "<b>Порада (оптимізація):</b>\n"
    "Можна кешувати результати викликів для пришвидшення:\n"
    "<pre><code class='language-python'>from functools import lru_cache\n\n@lru_cache(maxsize=None)\ndef fib(n):\n    if n &lt;= 1:\n        return n\n    return fib(n - 1) + fib(n - 2)</code></pre>\n\n"

    "<i>Висновок:</i> Рекурсія — потужний інструмент, але її потрібно використовувати обережно і з чітким базовим випадком."
),
    "⏳ Алгоритмічна складність": (
    "<b>Складність алгоритму</b> — це оцінка того, скільки часу або памʼяті займе виконання програми залежно від розміру вхідних даних.\n\n"

    "<b>Часова складність (Big O):</b>\n"
    "• <b>O(1)</b> — постійна: час не залежить від обсягу даних.\n"
    "<pre><code class='language-python'>arr = [10, 20, 30]\nprint(arr[0])  # O(1)</code></pre>\n\n"

    "• <b>O(n)</b> — лінійна: час пропорційний кількості елементів.\n"
    "<pre><code class='language-python'>for x in arr:\n    print(x)  # O(n)</code></pre>\n\n"

    "• <b>O(n²)</b> — квадратична: вкладені цикли.\n"
    "<pre><code class='language-python'>for i in arr:\n    for j in arr:\n        print(i, j)  # O(n²)</code></pre>\n\n"

    "• <b>O(log n)</b> — логарифмічна: наприклад, бінарний пошук.\n"
    "<pre><code class='language-python'>import bisect\nindex = bisect.bisect_left(arr, 20)  # O(log n)</code></pre>\n\n"

    "<b>Просторова складність</b> — скільки памʼяті використовує алгоритм.\n"
    "Наприклад, створення нового списку займає O(n) памʼяті.\n\n"

    "<b>Чому важливо?</b>\n"
    "• Дозволяє оцінити ефективність алгоритму\n"
    "• Вибирати найшвидші рішення для великих обсягів даних\n\n"

    "<b>Порада:</b> Якщо можливо — прагни зменшити складність з O(n²) до O(n log n) або O(n)\n\n"

    "<i>Висновок:</i> Знання Big O допомагає писати швидкий та оптимальний код!"
)
}