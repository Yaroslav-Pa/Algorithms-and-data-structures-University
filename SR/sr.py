import tkinter as tk
from tkinter import ttk, messagebox
import subprocess
import os
from ttkbootstrap import Style

class TaskInfoWindow(tk.Toplevel):
    def __init__(self, parent, title, message):
        super().__init__(parent)
        self.title(title)
        tk.Label(self, text=message, wraplength=480, justify=tk.LEFT,  font = ('Helvetica', 10)).pack(expand=True, fill='both', padx=10, pady=(10, 20))
class TaskValuesWindow(tk.Toplevel):
    def __init__(self, parent, title, values):
        super().__init__(parent)
        self.title(title)
        text_widget = tk.Text(self, wrap=tk.WORD, width=60, height=10, font=('Helvetica', 12))
        text_widget.insert(tk.END, values)
        text_widget.config(state=tk.DISABLED)
        text_widget.pack(expand=True, fill=tk.BOTH, padx=10, pady=10)

class LessonApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Лабораторні роботи")

        # Встановлення ttkbootstrap теми для всіх ttk елементів
        Style().theme_use('darkly')
        self.lab_works = {
            "Лабораторна робота 1": ["Завдання 1", "Завдання 2"],
            "Лабораторна робота 2": ["Завдання 1", "Завдання 2"],
            "Лабораторна робота 3": ["Завдання 1", "Завдання 2"],
            "Лабораторна робота 4": ["Завдання 1", "Завдання 2"],
            "Лабораторна робота 5": ["Завдання 1", "Завдання 2", "Завдання 3"],
            "Лабораторна робота 6": ["Завдання 1", "Завдання 2", "Завдання 3"],
        }
                
        self.task_variables_paths = {
            "Лабораторна робота 1": {
                "Завдання 1": "LR1/variables1.py",
                "Завдання 2": "LR1/variables2.py",
            },
            "Лабораторна робота 2": {
                "Завдання 1": "file.txt",
                "Завдання 2": "LR2/variables2.py",
            },
            "Лабораторна робота 3": {
                "Завдання 1": "LR3/variables1.py",
                "Завдання 2": "in.txt",
            },
            "Лабораторна робота 4": {
                "Завдання 1": "LR4/variables1.py",
                "Завдання 2": "LR4/variables2.py",
            },
            "Лабораторна робота 5": {
                "Завдання 1": "LR5/variables1.py",
                "Завдання 2": "LR5/variables2.py",
                "Завдання 3": "LR5/variables3.py",
            },
            "Лабораторна робота 6": {
                "Завдання 1": "LR6/variables1.py",
                "Завдання 2": "LR6/variables2.py",
                "Завдання 3": "LR6/variables3.py",
            },
        }

        self.task_paths = {
            "Лабораторна робота 1": {
                "Завдання 1": "LR1/1.py",
                "Завдання 2": "LR1/2.py",
            },
            "Лабораторна робота 2": {
                "Завдання 1": "LR2/1.py",
                "Завдання 2": "LR2/2.py",
            },
            "Лабораторна робота 3": {
                "Завдання 1": "LR3/1.py",
                "Завдання 2": "LR3/2.py",
            },
            "Лабораторна робота 4": {
                "Завдання 1": "LR4/1.py",
                "Завдання 2": "LR4/2.py",
            },
            "Лабораторна робота 5": {
                "Завдання 1": "LR5/1.py",
                "Завдання 2": "LR5/2.py",
                "Завдання 3": "LR5/3.py",
            },
            "Лабораторна робота 6": {
                "Завдання 1": "LR6/1.py",
                "Завдання 2": "LR6/2.py",
                "Завдання 3": "LR6/3.py",
            },
        }
        
        self.task_conditions = {
            "Лабораторна робота 1": {
                "Завдання 1": 
"""
    Розроблюваний програмний проєкт має складатися з окремих класів, що реалізують структури даних двозв’язний список та купа (черга з пріоритетами). На найвищий рівень може бутипередбачено графічну інтерфейсну взаємодію з користувачем для роботи зі створеними класами.
    Клас, що реалізує двозв’язний список, має дозволяти виконувати наступні операції на основі окремих методів: додавання вузла в початок списку, додавання вузла після заданого, пошук вузла в списку, видалення вузла, виведення вузлів на екран з початку та з кінця.
    Клас, що реалізує купу (чергу з пріоритетами), має дозволяти виконувати наступні операції на основі окремих методів: вставлення елементу, сортування елементів, побудова купи з невпорядкованого масиву, видалення елементу, сортування елементів із використанням купи, виведення елементів на екран.
""",
                "Завдання 2":                 
                """
На підприємстві дані про кожного співробітника в одному з
відділів включають наступні параметри:
– прізвище, ім’я, по батькові;
– посада;
– стаж;
– домашня адреса;
– дата народження.
Вивести перелік співробітників у порядку зменшення їх віку,
для кожного вказуючи кількість повних років. У випадку однакової
дати народження виводити спочатку співробітника з меншим стажем.
                """,
            },
            "Лабораторна робота 2": {
                "Завдання 1": """Створити геш-таблицю, що використовує метод відкритої адресації для розв’язання колізій, геш-функцію ділення з остачею та метод лінійного дослідження для обчислення послідовностей досліджень. Геш-таблицю заповнити на основі виділення інформації з текстового файлу, в якому містяться підказки для кожного зарезервованого слова. Виконати пошук інформації.""",
                "Завдання 2": """ Мобільний оператор повинен мати інформацію про абонентів для забезпечення послуг. Кожний абонент характеризується номером, прізвищем, ім’ям, по батькові, тарифним планом. Сформувати дерево з відповідної інформації про абонентів, забезпечити пошук інформації про абонента за його телефонним номером та визначення кількості підключень за кожним з тарифів.""",
            },
            "Лабораторна робота 3": {
                "Завдання 1": """   Інвестор оголосив конкурс на фінансування проєктів протягом заданого періоду часу. Після подачі заявок і попереднього відбору було сформовано відповідний пул заявок, кожну з яких визначено датою початку, датою завершення та прибутком, який даний проєкт принесе після виконання. Оцінивши надані заявки та власні ресурси, інвестор зрозумів, що зможе фінансувати не більше ніж один проєкт одночасно. Під час конкурсного відбору інвестор поставив задачу вибрати для виконання набір проєктів, які принесуть йому максимальну вигоду.""",
                "Завдання 2": """   Розробити програмне забезпечення, яке реалізує використання алгоритму Хаффмана для стискання даних текстового файлу у вигляді класу. Клас повинен мати методи, які дозволяють задати файл з даними, виконати стискання даних, визначити параметри виконаного стискання та зворотне перетворення, записати результати кодування/декодування в файл.""",
            },
            "Лабораторна робота 4": {
                "Завдання 1": """   Для заданого рядка символів визначити послідовність дій з розбиття рядка на задані частини, що характеризується мінімальними вимогами до часу виконання дій. Частини, на які необхідно розбити рядок, задаються порядковими номерами символів, які є межами частин рядка. Тобто якщо рядок довжиною 10 символів необхідно розділити на частини після символів 3, 5, то в результаті має бути сформовано три нові рядка: з першого до третього символу, з четвертого до восьмого та з дев'ятого до десятого. Дані розбиття можна виконати в порядку зліва направо або справо наліво (у випадку більшої кількості частин таких варіацій стає ще більше). Розбиття зліва направо має наступну вартість: 10 (розбиває рядок на 3 та 7 символів) + 7 (розбиває рядок на 5 та 2 символів). Таким чином, в результаті необхідно визначити послідовність розбиття рядка, що характеризується мінімальною загальною вартістю за часом, та вартість такого розбиття.""",
                "Завдання 2": """   У процесі формування тексту в текстовому редакторі виникає завдання переносу слів за рядками. Для розв’язання даного завдання задається текст, який складається з деякого набору слів, та кількість символів, яка може міститися в одному рядку. Визначити, яким чином розташувати слова за рядками тексту (тобто визначити слова, які будуть розташовані в першому рядку, другому тощо), залишаючи між ними по одному пробілу, таким чином, щоб мінімізувати кількість пробілів, яка при цьому сумарно залишається в кінці рядків (в якості критерію використати суму кубів кількості пробілів у кінці кожного рядка окрім останнього).""",
            },
            "Лабораторна робота 5": {
                "Завдання 1": """   Користувач визначає граф, задає вершину даного графа та деяку відстань. Визначити перелік всіх вершин графа, які знаходяться на заданій відстані від заданої вершини.""",
                "Завдання 2": """   У заданому графі пронумерувати вершини у відповідності з порядком обходу в глибину, визначити кількість ребер даного графа та кількість його вершин. Обчислити середню щільність графа у вигляді частки""",
                "Завдання 3": """   У квадратній коробці, що складається з чотирьох чарунок за горизонталлю і чотирьох чарунок за вертикаллю, лежать 15 пронумерованих кубиків. Кубики на початку перемішані деяким чином, тобто їх позиції та вільна чарунка визначені випадковим чином. Пересуваючи тільки один кубик за раз, необхідно отримати розташування, коли незайнятою у коробці буде задана користувачем позиція (наприклад, крайній нижній кут).""",
            },
            "Лабораторна робота 6": {
                "Завдання 1": """   Арбітражні операції дозволяють використовувати різницю в поточному курсі валюти для перетворення одиниці валюти у більшу кількість одиниць тієї ж валюти. Вхідні дані задаються таблицею обмінних курсів, яка визначає, скільки за одну одиницю однієї валюти можна купити одиниць іншої валюти. Знайти для заданої користувачем валюти найвигіднішу можливість виконання таких арбітражних операцій. Необхідні перетворення можна виконати за допомогою логарифмування.""",
                "Завдання 2": """   Компанія забезпечує інтернет-підключення користувачів за допомогою оптичного кабелю. Для підключення нових абонентів було сформовано граф, який представляє можливі траси оптичного з’єднання. На графі ребрами представлені кабельні канали, а вершинами – місця, де є можливість вибору подальшого напрямку прокладення кабелю. Визначити трасу, яка з’єднає дві задані точки на мапі і буде мати при цьому найменшу довжину.""",
                "Завдання 3": """   Враховуючи, що граф, описаний у попередньому завданні, представляє можливості з’єднання району з існуючими магістральними лініями, визначити всі найкоротші шляхи всередині графу.""",
            },
        }
        
        self.topic_mapping = {
            "Лабораторна робота 1": "Лінійні структури даних",
            "Лабораторна робота 2": "Дерева та геш-таблиці",
            "Лабораторна робота 3": "Жадібні алгоритми",
            "Лабораторна робота 4": "Динамічне програмування",
            "Лабораторна робота 5": "Алгоритми для роботи з графами. Алгоритми обходу графів",
            "Лабораторна робота 6": "Алгоритми для роботи з графами. Алгоритми пошуку найкоротших шляхів",
        }

        self.lab_var = tk.StringVar()
        self.lab_var.set("Виберіть лабораторну роботу")
        self.lab_menu = ttk.Combobox(root, textvariable=self.lab_var, values=list(self.lab_works.keys()), state="readonly", font=('Helvetica', 12))
        self.lab_menu.grid(row=0, column=0, padx=10, pady=10, sticky="ew")


        self.code_entry = tk.Text(root, height=10, width=50, wrap=tk.WORD, font=('Helvetica', 12))
        self.code_entry.grid(row=2, column=0, padx=10, pady=10, sticky="nsew")
        self.code_entry.config()

        self.input_entry = tk.Entry(root, font=('Helvetica', 12))
        self.input_entry.grid(row=3, column=0, padx=10, pady=10, sticky="ew")

        self.task_var = tk.StringVar()
        self.task_var.set("Виберіть завдання")
        self.task_menu = ttk.Combobox(root, textvariable=self.task_var, state="disabled", font=('Helvetica', 12))
        self.task_menu.grid(row=0, column=1, padx=10, pady=10, sticky="ew")

        self.lab_menu.bind("<<ComboboxSelected>>", self.update_tasks)
        self.task_menu.bind("<<ComboboxSelected>>", self.run_selected_task)

        self.rerun_button = tk.Button(root, text="Перезапустити завдання", command=self.rerun_current_task, state=tk.DISABLED, font=('Helvetica', 12))
        self.rerun_button.grid(row=2, column=1, padx=10, pady=10, sticky="nwe")

        self.info_button = tk.Button(root, text="Про завдання", command=self.show_task_info, state=tk.DISABLED, font=('Helvetica', 12))
        self.info_button.grid(row=2, column=1, padx=10, pady=70, sticky="nwe")

        self.see_values_button = tk.Button(root, text="Показати початкові значення", command=self.show_task_values, state=tk.DISABLED, font=('Helvetica', 12))
        self.see_values_button.grid(row=2, column=1, padx=10, pady=110, sticky="nwe")

        self.change_values_button = tk.Button(root, text="Змінити значення", command=self.change_initial_values, state=tk.DISABLED, font=('Helvetica', 12))
        self.change_values_button.grid(row=2, column=1, padx=10, pady=150, sticky="nwe")

        self.see_code_button = tk.Button(root, text="Продивитись код програми", command=self.see_code_of_task, state=tk.DISABLED, font=('Helvetica', 12))
        self.see_code_button.grid(row=2, column=1, padx=10, pady=190, sticky="nwe")

        self.show_compressed_button = tk.Button(root, text="Показати скомпресований файл", command=self.show_compressed_file, font=('Helvetica', 12))
        self.show_compressed_button.grid(row=3, column=1, padx=10, pady=10, sticky="nwe")
        self.hide_button(self.show_compressed_button)

        self.show_decompressed_button = tk.Button(root, text="Показати декомпресований файл", command=self.show_decompressed_file, font=('Helvetica', 12))
        self.show_decompressed_button.grid(row=3, column=0, padx=10, pady=10, sticky="nwe")
        self.hide_button(self.show_decompressed_button)

        self.current_topic_var = tk.StringVar()
        self.current_topic_var.set("Оберіть лабораторну роботу та завдання")

        self.current_topic_entry = tk.Entry(root, textvariable=self.current_topic_var, font=('Helvetica', 12), width=80)
        self.current_topic_entry.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")

        root.grid_rowconfigure(1, weight=0)
        root.grid_rowconfigure(2, weight=1)  
        root.grid_columnconfigure(0, weight=1)
        root.grid_columnconfigure(1, weight=1) 



    def update_tasks(self, event):
        selected_lab = self.lab_var.get()
        selected_task = self.task_var.get()
        tasks = self.lab_works.get(selected_lab, [])
        self.task_menu["values"] = tasks
        self.task_var.set("Виберіть завдання")
        self.info_button.config(state=tk.DISABLED)
        self.rerun_button.config(state=tk.DISABLED)
        self.change_values_button.config(state=tk.DISABLED)
        self.see_values_button.config(state=tk.DISABLED)
        self.see_code_button.config(state=tk.DISABLED)
        self.task_menu.config(state="readonly" if tasks else "disabled")
        self.update_current_topic()

    def update_current_topic(self):
        selected_lab = self.lab_var.get()
        selected_task = self.task_var.get()
        current_topic = self.topic_mapping.get(selected_lab, "Невідома тема")
        self.current_topic_var.set(current_topic)


    def run_selected_task(self, event):
        selected_lab = self.lab_var.get()
        selected_task = self.task_var.get()

        if selected_task:
            self.info_button.config(state=tk.NORMAL)
            self.rerun_button.config(state=tk.NORMAL)
            self.change_values_button.config(state=tk.NORMAL)
            self.see_values_button.config(state=tk.NORMAL)
            self.see_code_button.config(state=tk.NORMAL)
            self.show_button(self.current_topic_entry)
            self.update_current_topic()
            script_path = self.task_paths[selected_lab][selected_task]
            result = self.run_script(script_path)
            self.code_entry.delete("1.0", tk.END)  
            self.code_entry.insert(tk.END, result)
        else:
            self.info_button.config(state=tk.DISABLED)
            self.rerun_button.config(state=tk.DISABLED)
            self.change_values_button.config(state=tk.DISABLED)
            self.see_values_button.config(state=tk.DISABLED)
            self.see_code_button.config(state=tk.DISABLED)
            self.hide_button(self.current_topic_entry)
            self.code_entry.delete("1.0", tk.END)

        if selected_lab == "Лабораторна робота 3" and selected_task == "Завдання 2":
            self.show_button(self.show_compressed_button)
            self.show_button(self.show_decompressed_button)
        else:
            self.hide_button(self.show_compressed_button)
            self.hide_button(self.show_decompressed_button)

    def run_script(self, script_path):
        try:
            result = subprocess.check_output(["python", script_path], universal_newlines=True, stderr=subprocess.STDOUT)
            return result
        except subprocess.CalledProcessError as e:
            return e.output

    def rerun_current_task(self):
        selected_lab = self.lab_var.get()
        selected_task = self.task_var.get()

        if selected_task:
            self.info_button.config(state=tk.NORMAL)
            self.rerun_button.config(state=tk.NORMAL)
            self.change_values_button.config(state=tk.NORMAL)
            self.see_code_button.config(state=tk.NORMAL)
            self.show_button(self.current_topic_entry)
            script_path = self.task_paths.get(selected_lab, {}).get(selected_task)
            result = self.run_script(script_path)
            self.code_entry.delete("1.0", tk.END)
            self.code_entry.insert(tk.END, result)
        else:
            self.info_button.config(state=tk.DISABLED)
            self.rerun_button.config(state=tk.DISABLED)
            self.change_values_button.config(state=tk.DISABLED)
            self.see_code_button.config(state=tk.DISABLED)
            self.hide_button(self.current_topic_entry)
            self.code_entry.delete("1.0", tk.END)

    def show_task_info(self):
        selected_lab = self.lab_var.get()
        selected_task = self.task_var.get()
        if selected_task:
            task_info = self.task_conditions.get(selected_lab, {}).get(selected_task, "Немає умови для цього завдання.")
            info_window = TaskInfoWindow(self.root, title=f"Умова для {selected_task}", message=task_info)
            info_window.focus_set()

    def show_task_values(self):
        selected_lab = self.lab_var.get()
        selected_task = self.task_var.get()
        if selected_task:
            values_path = self.task_variables_paths.get(selected_lab, {}).get(selected_task)
            if values_path:
                with open(values_path, "r") as file:
                    values_content = file.read()
                    values_window = TaskValuesWindow(self.root, title=f"Поточні значення для {selected_task}", values=values_content)
                    values_window.focus_set()

    def change_initial_values(self):
        selected_lab = self.lab_var.get()
        selected_task = self.task_var.get()

        if selected_task:
            script_path = self.task_variables_paths[selected_lab][selected_task] 
            try:
                subprocess.Popen(["code.cmd", script_path])  
            except FileNotFoundError:
                
                subprocess.Popen(["notepad.exe", script_path])

    def see_code_of_task(self):
        selected_lab = self.lab_var.get()
        selected_task = self.task_var.get()

        if selected_task:
            script_path = self.task_paths[selected_lab][selected_task] 
            try:
                subprocess.Popen(["code.cmd", script_path])  
            except FileNotFoundError:
                
                subprocess.Popen(["notepad.exe", script_path])

    def show_compressed_file(self):
        file_path = "compress.bin"
        if os.path.exists(file_path):
            with open(file_path, "r") as file:
                file_content = file.read()
                self.show_file_content("Вміст скомпресованого файлу", file_content)
        else:
            messagebox.showinfo("Помилка", "Файл не знайдено.")

    def show_decompressed_file(self):
        file_path = "out.txt"
        if os.path.exists(file_path):
            with open(file_path, "r") as file:
                file_content = file.read()
                self.show_file_content("Вміст декомпресованого файлу", file_content)
        else:
            messagebox.showinfo("Помилка", "Файл не знайдено.")

    def show_file_content(self, title, content):
        messagebox.showinfo(title, content)

    def hide_button(self, button):
        button.grid_remove()

    def show_button(self, button):
        button.grid()

root = tk.Tk()

app = LessonApp(root)
root.mainloop()
