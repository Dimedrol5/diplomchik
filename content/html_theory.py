html_theory_texts = {
    "🔢 Змінні та типи даних": (
    "<b>Змінні та типи даних у JavaScript</b> — це основа для зберігання і роботи з інформацією.\n\n"

    "<b>Оголошення змінних:</b>\n"
    "• <code>var</code> — стара форма (уникайте використання)\n"
    "• <code>let</code> — сучасна змінна, яку можна переприсвоїти\n"
    "• <code>const</code> — константа (не можна переприсвоїти)\n"
    "<pre>let name = \"Anna\";\nconst pi = 3.14;</pre>\n\n"

    "<b>Основні типи даних:</b>\n"
    "• <b>Number</b> — числа (цілі та дробові)\n"
    "<pre>let age = 25;\nlet price = 19.99;</pre>\n\n"

    "• <b>String</b> — рядки тексту\n"
    "<pre>let greeting = \"Привіт\";</pre>\n\n"

    "• <b>Boolean</b> — логічні значення (true / false)\n"
    "<pre>let isOnline = true;</pre>\n\n"

    "• <b>Array</b> — масиви (набір значень)\n"
    "<pre>let fruits = [\"apple\", \"banana\", \"cherry\"];</pre>\n\n"

    "• <b>Object</b> — обʼєкти (пари ключ-значення)\n"
    "<pre>let user = {name: \"Anna\", age: 25};</pre>\n\n"

    "<b>Додатково:</b>\n"
    "• <b>null</b> — відсутність значення\n"
    "• <b>undefined</b> — змінна без значення\n"
    "• <b>typeof</b> — оператор для перевірки типу:\n"
    "<pre>typeof age; // \"number\"</pre>\n\n"

    "<i>Правильний вибір типів даних — основа ефективного коду!</i>"
),
    "🔁 Цикли (for, while)": (
    "<b>Цикли</b> в JavaScript дозволяють повторювати виконання коду кілька разів.\n\n"

    "<b>Цикл for:</b>\n"
    "Використовується, коли відома кількість повторень.\n"
    "<pre>for (let i = 0; i &lt; 5; i++) {\n  console.log(i);\n}</pre>\n\n"

    "<b>Цикл while:</b>\n"
    "Виконує код, поки умова істинна.\n"
    "<pre>let i = 0;\nwhile (i &lt; 5) {\n  console.log(i);\n  i++;\n}</pre>\n\n"

    "<b>Цикл do...while:</b>\n"
    "Виконує код хоча б один раз.\n"
    "<pre>let i = 0;\ndo {\n  console.log(i);\n  i++;\n} while (i &lt; 5);</pre>\n\n"

    "<b>Цикл for...of:</b>\n"
    "Ітерація по масивах або колекціях.\n"
    "<pre>let fruits = [\"apple\", \"banana\", \"cherry\"];\nfor (let fruit of fruits) {\n  console.log(fruit);\n}</pre>\n\n"

    "<b>Цикл for...in:</b>\n"
    "Ітерація по ключах обʼєкта.\n"
    "<pre>let user = {name: \"Anna\", age: 25};\nfor (let key in user) {\n  console.log(key + \": \" + user[key]);\n}</pre>\n\n"

    "<i>Цикли — основа для обробки колекцій і масивів!</i>"
),

"📥 Умовні оператори": (
    "<b>Умовні оператори</b> дозволяють виконувати різний код залежно від умов.\n\n"

    "<b>if, else if, else:</b>\n"
    "Основна конструкція умов.\n"
    "<pre>let age = 18;\nif (age &gt;= 18) {\n  console.log(\"Дорослий\");\n} else {\n  console.log(\"Дитина\");\n}</pre>\n\n"

    "<b>Оператор тернарний (?:)</b>\n"
    "Скорочена форма if...else.\n"
    "<pre>let result = (age &gt;= 18) ? \"Дорослий\" : \"Дитина\";</pre>\n\n"

    "<b>switch:</b>\n"
    "Зручно використовувати для багатьох варіантів.\n"
    "<pre>let day = 2;\nswitch (day) {\n  case 1:\n    console.log(\"Понеділок\");\n    break;\n  case 2:\n    console.log(\"Вівторок\");\n    break;\n  default:\n    console.log(\"Інший день\");\n}</pre>\n\n"

    "<b>Логічні оператори:</b>\n"
    "Можна комбінувати умови.\n"
    "<pre>if (age &gt;= 18 &amp;&amp; age &lt; 65) {\n  console.log(\"Працездатний вік\");\n}</pre>\n\n"

    "<i>Умовні оператори — основа прийняття рішень у коді!</i>"
),

"📦 Методи": (
    "<b>Функції</b> (методи) — це блоки коду, які можна викликати багаторазово.\n\n"

    "<b>Оголошення функції:</b>\n"
    "<pre>function add(a, b) {\n  return a + b;\n}</pre>\n"
    "• Виклик: <code>let result = add(3, 5);</code>\n\n"

    "<b>Функціональний вираз:</b>\n"
    "<pre>const multiply = function(a, b) {\n  return a * b;\n};</pre>\n"
    "• Зберігається у змінній\n\n"

    "<b>Стрілкові функції (arrow functions):</b>\n"
    "<pre>const square = (n) =&gt; n * n;</pre>\n"
    "• Короткий запис функцій\n\n"

    "<b>Параметри за замовчуванням:</b>\n"
    "<pre>function greet(name = \"Гість\") {\n  console.log(\"Привіт, \" + name);\n}</pre>\n"
    "• Якщо аргумент не передано, використовується значення за замовчуванням\n\n"

    "<b>Повернення значення:</b>\n"
    "<pre>function subtract(a, b) {\n  return a - b;\n}</pre>\n"
    "• <code>return</code> завершує функцію і повертає значення\n\n"

    "<i>Функції допомагають структурувати код і уникати дублювання.</i>"
),
"🧱 Масиви, списки, колекції": (
    "<b>Масиви</b> — це впорядковані списки елементів.\n\n"

    "<b>Створення масиву:</b>\n"
    "<pre>let fruits = [\"Apple\", \"Banana\", \"Orange\"];</pre>\n"
    "• Доступ до елементів: <code>fruits[0]</code> → <code>\"Apple\"</code>\n"
    "• Довжина масиву: <code>fruits.length</code>\n\n"

    "<b>Основні методи масивів:</b>\n"
    "• <code>push()</code> — додати елемент в кінець\n"
    "<pre>fruits.push(\"Grape\");</pre>\n"
    "• <code>pop()</code> — видалити останній елемент\n"
    "<pre>fruits.pop();</pre>\n"
    "• <code>shift()</code> — видалити перший елемент\n"
    "<pre>fruits.shift();</pre>\n"
    "• <code>unshift()</code> — додати на початок\n"
    "<pre>fruits.unshift(\"Mango\");</pre>\n\n"

    "<b>Перебір масиву:</b>\n"
    "<pre>for (let fruit of fruits) {\n  console.log(fruit);\n}</pre>\n\n"

    "<b>Об'єкти</b> — це колекції пар \"ключ-значення\".\n"
    "<pre>let person = {\n  name: \"Anna\",\n  age: 25\n};</pre>\n"
    "• Доступ до властивостей: <code>person.name</code> → <code>\"Anna\"</code>\n"
    "• Додавання властивості:\n"
    "<pre>person.city = \"Kyiv\";</pre>\n\n"

    "<i>Масиви і обʼєкти — основа роботи з даними у JavaScript.</i>"
),
"🧮 Оператори та вирази": (
    "<b>Оператори</b> — це символи або ключові слова, які виконують дії над значеннями.\n\n"

    "<b>Арифметичні оператори:</b>\n"
    "<code>+</code>, <code>-</code>, <code>*</code>, <code>/</code>, <code>%</code> (остача)\n"
    "<pre>let result = 5 + 3; // 8</pre>\n\n"

    "<b>Оператори порівняння:</b>\n"
    "<code>==</code> (рівність), <code>===</code> (строга рівність), <code>!=</code>, <code>!==</code>\n"
    "<code>&gt;</code>, <code>&lt;</code>, <code>&gt;=</code>, <code>&lt;=</code>\n"
    "<pre>5 === \"5\" // false\n5 == \"5\" // true</pre>\n\n"

    "<b>Логічні оператори:</b>\n"
    "<code>&&</code> (і), <code>||</code> (або), <code>!</code> (не)\n"
    "<pre>if (age &gt;= 18 && citizen === true) {\n  console.log(\"Доступ дозволено\");\n}</pre>\n\n"

    "<b>Оператор присвоєння:</b>\n"
    "<code>=</code>, <code>+=</code>, <code>-=</code>, <code>*=</code>, <code>/=</code>\n"
    "<pre>let x = 10;\nx += 5; // x = 15</pre>\n\n"

    "<b>Тернарний оператор:</b>\n"
    "<pre>let status = (age &gt;= 18) ? \"Дорослий\" : \"Дитина\";</pre>\n\n"

    "<i>Оператори і вирази — основа написання умов, циклів і обчислень у JavaScript.</i>"
),
"🗂️ Робота з файлами": (
    "<b>У браузері (HTML5):</b>\n\n"
    "<b>Зчитування файлу (File API):</b>\n"
    "<pre><code class='language-javascript'>let input = document.querySelector('input[type=file]');\ninput.addEventListener('change', function() {\n  let file = input.files[0];\n  let reader = new FileReader();\n  reader.onload = function() {\n    console.log(reader.result);\n  };\n  reader.readAsText(file);\n});</code></pre>\n"
    "• Користувач сам вибирає файл із компʼютера\n"
    "• <code>FileReader</code> дозволяє читати вміст як текст чи дані\n\n"

    "<b>Збереження файлу (Blob + посилання):</b>\n"
    "<pre><code class='language-javascript'>let text = 'Hello, world!';\nlet blob = new Blob([text], { type: 'text/plain' });\nlet link = document.createElement('a');\nlink.href = URL.createObjectURL(blob);\nlink.download = 'example.txt';\nlink.click();</code></pre>\n"
    "• Створюється тимчасовий файл і завантажується на компʼютер\n\n"

    "<b>У Node.js (серверна частина):</b>\n"
    "<b>Зчитування файлу:</b>\n"
    "<pre><code class='language-javascript'>const fs = require('fs');\nlet data = fs.readFileSync('file.txt', 'utf8');\nconsole.log(data);</code></pre>\n\n"
    "<b>Запис у файл:</b>\n"
    "<pre><code class='language-javascript'>fs.writeFileSync('file.txt', 'Hello, Node!');</code></pre>\n\n"

    "• У Node.js є модуль <code>fs</code> (file system)\n"
    "• На сервері доступна повна робота з файлами\n\n"

    "<i>У браузері робота з файлами обмежена для безпеки, а на сервері (Node.js) — повноцінна.</i>"
),
"🧪 Обробка виключень": (
    "<b>Обробка помилок у JavaScript</b> здійснюється за допомогою конструкції <code>try-catch</code>.\n\n"
    "<b>Основна структура:</b>\n"
    "<pre><code class='language-javascript'>try {\n  // код, який може викликати помилку\n  let result = 5 / 0;\n} catch (error) {\n  console.log('Сталася помилка:', error);\n}</code></pre>\n"
    "• <code>try</code> — виконує код\n"
    "• <code>catch</code> — ловить помилки та працює з ними\n\n"

    "<b>finally</b> — виконується завжди (незалежно від помилки):\n"
    "<pre><code class='language-javascript'>try {\n  console.log('Початок');\n} catch (e) {\n  console.log('Помилка');\n} finally {\n  console.log('Завжди виконується');\n}</code></pre>\n\n"

    "<b>Викидання власних помилок (throw):</b>\n"
    "<pre><code class='language-javascript'>function divide(a, b) {\n  if (b === 0) {\n    throw new Error('Ділення на нуль неможливе');\n  }\n  return a / b;\n}\n\ntry {\n  divide(10, 0);\n} catch (e) {\n  console.log(e.message);\n}</code></pre>\n\n"

    "• <code>throw</code> дозволяє вручну створити помилку\n"
    "• Обробка виключень допомагає зробити код надійним і зрозумілим\n\n"
    "<i>Рекомендується завжди обробляти можливі помилки, особливо при роботі з файлами, мережею та введенням користувача.</i>"
),
"🔄 Рекурсія": (
    "<b>Рекурсія</b> — це коли функція викликає сама себе для розвʼязання задачі.\n\n"
    "<b>Приклад рекурсії: обчислення факторіала</b>\n"
    "<pre><code class='language-javascript'>function factorial(n) {\n  if (n === 1) {\n    return 1;\n  }\n  return n * factorial(n - 1);\n}\n\nconsole.log(factorial(5)); // 120</code></pre>\n\n"

    "• Обовʼязково має бути <b>базовий випадок</b> (умова зупинки), щоб уникнути нескінченних викликів.\n"
    "• Функція поступово «розкладається» на простіші задачі.\n\n"

    "<b>Приклад рекурсії: обхід масиву</b>\n"
    "<pre><code class='language-javascript'>function printArray(arr, index = 0) {\n  if (index >= arr.length) {\n    return;\n  }\n  console.log(arr[index]);\n  printArray(arr, index + 1);\n}\n\nprintArray(['a', 'b', 'c']);</code></pre>\n\n"

    "<b>Коли корисна рекурсія?</b>\n"
    "• Алгоритми на деревах (обхід DOM-дерева)\n"
    "• Робота з вкладеними структурами (наприклад, вкладені списки або JSON)\n"
    "• Алгоритми сортування (наприклад, quicksort, mergesort)\n\n"

    "<b>Порада:</b> Рекурсію варто використовувати, коли задача природно розбивається на підзадачі того ж типу. "
    "При великих обʼємах даних краще використовувати <b>ітерацію</b> (цикли), щоб уникнути переповнення стеку.\n\n"
    "<i>Рекурсія — потужний інструмент, але потребує уважного контролю умови завершення.</i>"
),
"⏳ Складність алгоритмів": (
    "<b>Складність алгоритму</b> показує, як швидко зростає кількість операцій або використання памʼяті при збільшенні розміру даних.\n\n"
    "<b>Основні типи складності (Big O):</b>\n"
    "• <b>O(1)</b> — постійна: доступ до елементу масиву <code>arr[0]</code>\n"
    "• <b>O(n)</b> — лінійна: перебір масиву <code>arr.forEach(x =&gt; console.log(x))</code>\n"
    "• <b>O(n²)</b> — квадратична: вкладені цикли\n"
    "• <b>O(log n)</b> — логарифмічна: бінарний пошук\n"
    "• <b>O(n log n)</b> — сортування швидкими алгоритмами (наприклад, QuickSort)\n\n"
    "<b>Приклад:</b>\n"
    "Якщо масив має 1000 елементів:\n"
    "• O(n) ≈ 1000 операцій\n"
    "• O(n²) ≈ 1 000 000 операцій\n"
    "• O(log n) ≈ 10 операцій\n\n"
    "<b>Навіщо це знати?</b>\n"
    "• Допомагає оцінити ефективність алгоритму\n"
    "• Дає змогу уникнути повільних рішень при великих обʼємах даних\n"
    "• Полегшує вибір найкращого підходу\n\n"
    "<i>Порада:</i> Якщо можете — використовуйте алгоритми з O(n), O(log n) або краще, а не O(n²) чи O(2ⁿ)."
)
}