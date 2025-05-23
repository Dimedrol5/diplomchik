java_theory_texts = {
"🔢 Змінні та типи даних": (
    "<b>Змінні</b> в Java — це іменовані комірки памʼяті, які зберігають дані певного типу. "
    "У Java потрібно <b>явно вказувати тип</b> змінної при її оголошенні.\n\n"
    "<b>Синтаксис оголошення змінної:</b>\n"
    "<pre><code class='language-java'>тип_даних імʼя_змінної = значення;</code></pre>\n\n"
    "<b>Приклади:</b>\n"
    "<pre><code class='language-java'>int age = 25;\nString name = \"Anna\";\ndouble pi = 3.14;\nboolean isActive = true;</code></pre>\n\n"
    "<b>Типи даних у Java поділяються на:</b>\n"
    "1️⃣ <u><b>Примітивні типи</b></u> (Primitive types)\n"
    "• <code>byte</code> (1 байт) — ціле число від -128 до 127\n"
    "• <code>short</code> (2 байти)\n"
    "• <code>int</code> (4 байти)\n"
    "• <code>long</code> (8 байтів)\n"
    "• <code>float</code> (4 байти) — число з плаваючою точкою\n"
    "• <code>double</code> (8 байтів)\n"
    "• <code>char</code> (2 байти) — символ Unicode\n"
    "• <code>boolean</code> — <code>true</code> або <code>false</code>\n\n"
    "2️⃣ <u><b>Складені (Reference) типи</b></u>\n"
    "• <code>String</code> — текстові рядки\n"
    "• Масиви (Arrays)\n"
    "• Класи (Classes), Інтерфейси (Interfaces)\n\n"
    "<b>Важливо:</b>\n"
    "• Java — це <b>мовa зі статичною типізацією</b>. Тип змінної визначається під час компіляції.\n"
    "• Після оголошення типу змінної — <b>змінити тип не можна</b>.\n\n"
    "<b>Неініціалізовані змінні:</b>\n"
    "• Локальні змінні <b>обовʼязково</b> потрібно ініціалізувати перед використанням.\n"
    "• Для полів класу Java задає <b>значення за замовчуванням</b> (0, false, null).\n\n"
    "<b>Приклад неправильного коду:</b>\n"
    "<pre><code class='language-java'>int x;\nSystem.out.println(x); // ❌ Помилка — змінна не ініціалізована</code></pre>\n\n"
    "<b>Ключові слова:</b> <code>final</code> (константа)\n"
    "<pre><code class='language-java'>final int DAYS_IN_WEEK = 7;</code></pre>\n"
    "Змінній <b>final</b> можна надати значення лише один раз.\n\n"
    "✅ Підсумок:\n"
    "• Чітко вказуй тип при оголошенні.\n"
    "• Ініціалізуй змінні перед використанням.\n"
    "• Використовуй <code>final</code> для констант."
),


"🔁 Цикли (for, while, do-while)": (
    "<b>Цикли</b> дозволяють багаторазово виконувати певний блок коду, поки умова істинна.\n\n"
    "<b>Цикл for</b> — використовується, коли кількість повторень відома наперед:\n"
    "<pre>for (int i = 0; i &lt; 5; i++) {\n    System.out.println(i);\n}</pre>\n\n"
    "<b>Цикл while</b> — використовується, коли кількість повторень невідома:\n"
    "<pre>int i = 0;\nwhile (i &lt; 5) {\n    System.out.println(i);\n    i++;\n}</pre>\n\n"
    "<b>Цикл do-while</b> — виконує тіло циклу хоча б один раз:\n"
    "<pre>int i = 0;\ndo {\n    System.out.println(i);\n    i++;\n} while (i &lt; 5);</pre>\n\n"
    "<b>Корисні оператори для циклів:</b>\n"
    "• <b>break</b> — перериває виконання циклу повністю.\n"
    "• <b>continue</b> — переходить до наступної ітерації циклу, пропускаючи залишок тіла циклу."
),

    "📥 Умовні оператори": (
    "<b>Умовні оператори</b> в Java дозволяють виконувати різні блоки коду залежно від певної умови.\n\n"
    "<b>Оператор if / else if / else</b> — дозволяє перевіряти одну або кілька умов:\n"
    "<pre>int age = 18;\nif (age &gt;= 18) {\n    System.out.println(&quot;Дорослий&quot;);\n} else {\n    System.out.println(&quot;Дитина&quot;);\n}</pre>\n\n"
    "<b>Оператор switch</b> — зручно використовувати для вибору між багатьма варіантами:\n"
    "<pre>int day = 2;\nswitch (day) {\n    case 1:\n        System.out.println(&quot;Понеділок&quot;);\n        break;\n    case 2:\n        System.out.println(&quot;Вівторок&quot;);\n        break;\n    default:\n        System.out.println(&quot;Інший день&quot;);\n}</pre>\n\n"
    "<b>Пояснення:</b>\n"
    "• <b>if</b> — перевіряє основну умову.\n"
    "• <b>else if</b> — перевіряє додаткову умову.\n"
    "• <b>else</b> — виконується, якщо жодна умова не істинна.\n"
    "• <b>switch</b> — обирає варіант на основі значення змінної.\n"
    "• <b>break</b> — завершує виконання блоку <code>case</code> у switch."
),


    "📦 Методи": (
    "<b>Методи</b> — це блоки коду, які виконують певне завдання і можуть бути викликані багаторазово.\n\n"
    "Методи допомагають структурувати програму, зробити її зрозумілішою та уникнути повторення коду.\n\n"
    "<b>Приклад оголошення методу:</b>\n"
    "<pre><code class='language-java'>public static int add(int a, int b) {\n    return a + b;\n}</code></pre>\n"
    "<b>Виклик методу:</b> <code>int result = add(3, 5);</code>\n\n"
    "<b>Складові методу:</b>\n"
    "• <code>public</code> — модифікатор доступу (метод доступний з інших класів)\n"
    "• <code>static</code> — метод належить класу, а не обʼєкту (можна викликати без створення обʼєкта)\n"
    "• <code>int</code> — тип повернення (що метод повертає)\n"
    "• <code>add</code> — імʼя методу\n"
    "• <code>(int a, int b)</code> — параметри методу (вхідні дані)\n\n"
    "<b>Методи без повернення:</b>\n"
    "Методи, які нічого не повертають, мають тип <code>void</code>.\n"
    "<pre><code class='language-java'>public static void greet() {\n    System.out.println(\"Привіт!\");\n}</code></pre>\n"
    "<b>Виклик:</b> <code>greet();</code>\n\n"
    "<b>Перевантаження методів (Overloading)</b> — це коли кілька методів мають однакове імʼя, але різні параметри.\n"
    "<pre><code class='language-java'>public static int add(int a, int b) {\n    return a + b;\n}\n\npublic static int add(int a, int b, int c) {\n    return a + b + c;\n}</code></pre>\n"
    "✅ <i>Java автоматично вибере правильний метод залежно від кількості та типу аргументів при виклику.</i>\n"
),


    "🧱 Масиви, списки, колекції": (
    "<b>Масиви (Arrays)</b> — це структури даних фіксованої довжини, які зберігають елементи одного типу.\n\n"
    "<b>Приклад оголошення масиву:</b>\n"
    "<pre><code class='language-java'>int[] nums = {1, 2, 3};\nSystem.out.println(nums[0]); // Виведе 1</code></pre>\n"
    "• Довжина масиву задається під час створення і не може змінюватися.\n"
    "• Індексація починається з нуля.\n"
    "• Щоб отримати довжину масиву: <code>nums.length</code>\n\n"
    "<b>Інший спосіб створення масиву:</b>\n"
    "<pre><code class='language-java'>int[] numbers = new int[5];\nnumbers[0] = 10;</code></pre>\n\n"
    "<b>Списки (ArrayList)</b> — це динамічні колекції, які дозволяють додавати або видаляти елементи під час виконання програми.\n\n"
    "<b>Приклад використання ArrayList:</b>\n"
    "<pre><code class='language-java'>import java.util.ArrayList;\n\nArrayList&lt;String&gt; list = new ArrayList&lt;&gt;();\nlist.add(\"Java\");\nlist.add(\"Python\");\nSystem.out.println(list.get(0)); // Виведе Java</code></pre>\n"
    "• ArrayList автоматично змінює розмір при додаванні або видаленні елементів.\n"
    "• Основні методи:\n"
    "   • <code>add(element)</code> — додати елемент\n"
    "   • <code>get(index)</code> — отримати елемент\n"
    "   • <code>remove(index)</code> — видалити елемент\n"
    "   • <code>size()</code> — дізнатись кількість елементів\n\n"
    "<b>Цикл по елементах списку:</b>\n"
    "<pre><code class='language-java'>for (String lang : list) {\n    System.out.println(lang);\n}</code></pre>\n\n"
    "<b>Інші колекції в Java:</b>\n"
    "• <code>HashSet</code> — множина (унікальні елементи)\n"
    "• <code>HashMap</code> — асоціативний масив (ключ-значення)\n"
    "• <code>LinkedList</code> — двозвʼязний список\n\n"
    "✅ <i>ArrayList найчастіше використовується для списків із довільною кількістю елементів.</i>\n"
),


"🧮 Оператори та вирази": (
    "<b>Оператори</b> — це символи або ключові слова, які виконують операції над змінними та значеннями.\n\n"
    "<b>Арифметичні оператори:</b>\n"
    "• <code>+</code> — додавання\n"
    "• <code>-</code> — віднімання\n"
    "• <code>*</code> — множення\n"
    "• <code>/</code> — ділення\n"
    "• <code>%</code> — остача від ділення\n"
    "<pre>int a = 10;\nint b = 3;\nSystem.out.println(a + b);\nSystem.out.println(a % b);</pre>\n\n"
    "<b>Оператори порівняння:</b>\n"
    "• <code>==</code> — рівність\n"
    "• <code>!=</code> — нерівність\n"
    "• <code>&gt;</code> — більше\n"
    "• <code>&lt;</code> — менше\n"
    "• <code>&gt;=</code> — більше або дорівнює\n"
    "• <code>&lt;=</code> — менше або дорівнює\n"
    "<pre>int x = 5;\nSystem.out.println(x == 5);\nSystem.out.println(x != 3);</pre>\n\n"
    "<b>Логічні оператори:</b>\n"
    "• <code>&&</code> — логічне І\n"
    "• <code>||</code> — логічне АБО\n"
    "• <code>!</code> — заперечення (NOT)\n"
    "<pre>int x = 5;\nif (x &gt; 3 &amp;&amp; x &lt; 10) {\n    System.out.println(\"x в діапазоні\");\n}</pre>\n\n"
    "<b>Комбіновані оператори присвоєння:</b>\n"
    "• <code>+=</code>, <code>-=</code>, <code>*=</code>, <code>/=</code>\n"
    "<pre>int y = 5;\ny += 3;\nSystem.out.println(y);</pre>\n\n"
    "<b>Інкремент та декремент:</b>\n"
    "• <code>++</code> — збільшити на 1\n"
    "• <code>--</code> — зменшити на 1\n"
    "<pre>int count = 0;\ncount++;\nSystem.out.println(count);</pre>\n\n"
    "✅ <i>Вирази комбінують змінні, значення та оператори для обчислення нового значення.</i>"
),

    "🗂️ Робота з файлами": (
    "<b>Робота з файлами</b> дозволяє читати і записувати дані у зовнішні файли.\n\n"
    "<b>Зчитування з файлу:</b>\n"
    "Використовуємо <code>BufferedReader</code> разом з <code>FileReader</code>.\n"
    "<pre>BufferedReader reader = new BufferedReader(new FileReader(\"file.txt\"));\nString line = reader.readLine();\nreader.close();</pre>\n\n"
    "<b>Запис у файл:</b>\n"
    "Використовуємо <code>BufferedWriter</code> разом з <code>FileWriter</code>.\n"
    "<pre>BufferedWriter writer = new BufferedWriter(new FileWriter(\"file.txt\"));\nwriter.write(\"Привіт!\");\nwriter.close();</pre>\n\n"
    "<b>Читання всіх рядків у циклі:</b>\n"
    "<pre>BufferedReader reader = new BufferedReader(new FileReader(\"file.txt\"));\nString line;\nwhile ((line = reader.readLine()) != null) {\n    System.out.println(line);\n}\nreader.close();</pre>\n\n"
    "<b>Особливості:</b>\n"
    "• Не забудьте <code>import java.io.*;</code>\n"
    "• Необхідно обробляти винятки (<code>try-catch</code>) або додавати <code>throws IOException</code>\n\n"
    "✅ <i>Файли слід завжди закривати після використання, щоб уникнути витоків ресурсів.</i>"
),

"🧪 Обробка виключень": (
    "<b>Обробка виключень</b> дозволяє програмі реагувати на помилки без краху.\n\n"
    "<b>try-catch:</b>\n"
    "Блокує помилку та дозволяє обробити її у catch-блоці.\n"
    "<pre>try {\n    int x = 5 / 0;\n} catch (ArithmeticException e) {\n    System.out.println(\"Помилка: ділення на 0\");\n}</pre>\n\n"
    "<b>finally:</b>\n"
    "Цей блок виконується завжди — незалежно від того, була помилка чи ні.\n"
    "<pre>finally {\n    System.out.println(\"Завершення програми\");\n}</pre>\n\n"
    "<b>Обробка кількох типів виключень:</b>\n"
    "<pre>try {\n    // код\n} catch (IOException e) {\n    System.out.println(\"IO помилка\");\n} catch (Exception e) {\n    System.out.println(\"Інша помилка\");\n}</pre>\n\n"
    "<b>Власні винятки (створення своїх класів-винятків):</b>\n"
    "<pre>class MyException extends Exception {\n    public MyException(String message) {\n        super(message);\n    }\n}</pre>\n\n"
    "<b>Особливості:</b>\n"
    "• Для багатьох методів, що працюють з файлами або мережею, потрібне <code>throws IOException</code>\n"
    "• Виключення — це об'єкти, які успадковують <code>Throwable</code>\n"
    "• <i>Обробка помилок робить програму надійнішою і безпечнішою.</i>"
),

"🔄 Рекурсія": (
    "<b>Рекурсія</b> — це коли метод викликає сам себе для розв’язання підзадачі.\n\n"
    "<b>Приклад — факторіал числа:</b>\n"
    "<pre>public static int factorial(int n) {\n    if (n == 1) return 1;\n    return n * factorial(n - 1);\n}</pre>\n\n"
    "<b>Ключові моменти:</b>\n"
    "• Обовʼязковий <i>базовий випадок</i> (умова зупинки), щоб уникнути нескінченних викликів.\n"
    "• Виклики формують стек (stack) — зберігаються стану кожного виклику.\n\n"
    "<b>Приклад — обхід масиву:</b>\n"
    "<pre>public static void printArray(int[] arr, int index) {\n    if (index == arr.length) return;\n    System.out.println(arr[index]);\n    printArray(arr, index + 1);\n}</pre>\n\n"
    "<b>Переваги:</b>\n"
    "• Спрощує код для складних задач (дерева, графи, пошук шляху).\n"
    "• Природньо виражає задачі, що мають повторювану структуру.\n\n"
    "<b>Недоліки:</b>\n"
    "• Велика глибина рекурсії може призвести до <code>StackOverflowError</code>\n"
    "• У деяких випадках краще використовувати ітеративний підхід.\n\n"
    "<i>Рекурсія — потужний інструмент, якщо використовувати її обережно!</i>"
),

"⏳ Складність алгоритмів": (
    "<b>Складність алгоритмів</b> — це оцінка того, скільки ресурсів (часу або памʼяті) "
    "потрібно алгоритму залежно від розміру вхідних даних.\n\n"

    "<b>Основні види часової складності:</b>\n\n"

    "• <b>O(1)</b> — постійна (доступ до елементу масиву)\n"
    "<pre>int x = array[0];</pre>\n\n"

    "• <b>O(n)</b> — лінійна (одне проходження масиву)\n"
    "<pre>for (int i = 0; i &lt; n; i++) {\n    System.out.println(array[i]);\n}</pre>\n\n"

    "• <b>O(n^2)</b> — квадратична (вкладені цикли)\n"
    "<pre>for (int i = 0; i &lt; n; i++) {\n    for (int j = 0; j &lt; n; j++) {\n        // ...\n    }\n}</pre>\n\n"

    "• <b>O(log n)</b> — логарифмічна (бінарний пошук)\n"
    "<pre>int low = 0, high = n - 1;\nwhile (low &lt;= high) {\n    int mid = (low + high) / 2;\n    // ...\n}</pre>\n\n"

    "<b>Чому це важливо?</b>\n"
    "• Допомагає оцінити ефективність алгоритмів\n"
    "• Вибирайте алгоритми з меншою складністю для великих обсягів даних\n"
    "• Враховуйте і просторову складність (скільки памʼяті споживає алгоритм)\n\n"

    "<i>Чим нижча складність — тим швидше працюватиме програма при великих даних.</i>"
)
}