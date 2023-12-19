import tkinter as tk
from tkinter import ttk, messagebox
import subprocess
import os

class LessonApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Лабораторні роботи")
        
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
                "Завдання 1": "Умова для завдання 1 ЛР1",
                "Завдання 2": "Умова для завдання 2 ЛР1",
            },
            "Лабораторна робота 2": {
                "Завдання 1": "Умова для завдання 1 ЛР2",
                "Завдання 2": "Умова для завдання 2 ЛР2",
            },
            "Лабораторна робота 3": {
                "Завдання 1": "Умова для завдання 1 ЛР3",
                "Завдання 2": "Умова для завдання 2 ЛР3",
            },
            "Лабораторна робота 4": {
                "Завдання 1": "Умова для завдання 1 ЛР4",
                "Завдання 2": "Умова для завдання 2 ЛР4",
            },
            "Лабораторна робота 5": {
                "Завдання 1": "Умова для завдання 1 ЛР5",
                "Завдання 2": "Умова для завдання 2 ЛР5",
                "Завдання 3": "Умова для завдання 3 ЛР5",
            },
            "Лабораторна робота 6": {
                "Завдання 1": "Умова для завдання 1 ЛР6",
                "Завдання 2": "Умова для завдання 2 ЛР6",
                "Завдання 3": "Умова для завдання 3 ЛР6",
            },
        }
        
        self.topic_mapping = {
            "Лабораторна робота 1": "Тема 1",
            "Лабораторна робота 2": "Тема 2",
            "Лабораторна робота 3": "Тема 3",
            "Лабораторна робота 4": "Тема 4",
            "Лабораторна робота 5": "Тема 5",
            "Лабораторна робота 6": "Тема 6",
        }

        self.lab_var = tk.StringVar()
        self.lab_var.set("Виберіть лабораторну роботу")
        self.lab_menu = ttk.Combobox(root, textvariable=self.lab_var, values=list(self.lab_works.keys()))
        self.lab_menu.grid(row=0, column=0, padx=10, pady=10, sticky="ew")
        
        self.code_entry = tk.Text(root, height=10, width=50)
        self.code_entry.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")
        
        self.input_entry = tk.Entry(root)
        self.input_entry.grid(row=2, column=0, padx=10, pady=10, sticky="ew")
        
        self.task_var = tk.StringVar()
        self.task_var.set("Виберіть завдання")
        self.task_menu = ttk.Combobox(root, textvariable=self.task_var, state="disabled")
        self.task_menu.grid(row=0, column=1, padx=10, pady=10, sticky="ew")
        
        self.lab_menu.bind("<<ComboboxSelected>>", self.update_tasks)
        self.task_menu.bind("<<ComboboxSelected>>", self.run_selected_task)
        
        self.info_button = tk.Button(root, text="Про завдання", command=self.show_task_info, state=tk.DISABLED)
        self.info_button.grid(row=1, column=1, padx=10, pady=10, sticky="nwe") 

        self.see_code_button = tk.Button(root, text="Продивитись код програми", command=self.see_code_of_task, state=tk.DISABLED)
        self.see_code_button.grid(row=1, column=1, padx=10, pady=50, sticky="nwe")

        self.change_values_button = tk.Button(root, text="Змінити початкові значення", command=self.change_initial_values, state=tk.DISABLED)
        self.change_values_button.grid(row=1, column=1, padx=10, pady=90, sticky="nwe")

        self.show_compressed_button = tk.Button(root, text="Показати скомпресований файл", command=self.show_compressed_file)
        self.show_compressed_button.grid(row=2, column=1, padx=10, pady=10, sticky="nwe")
        self.hide_button(self.show_compressed_button)

        self.show_decompressed_button = tk.Button(root, text="Показати декомпресований файл", command=self.show_decompressed_file)
        self.show_decompressed_button.grid(row=2, column=0, padx=10, pady=10, sticky="nwe")
        self.hide_button(self.show_decompressed_button)

        self.current_topic_label = tk.Label(root, font=('Helvetica', 12))
        self.current_topic_label.grid(row=1, column=0, padx=10, pady=10, sticky="e")

        self.current_topic_var = tk.StringVar()
        self.current_topic_var.set("Оберіть лабораторну роботу та завдання")

        self.current_topic_entry = tk.Entry(root, textvariable=self.current_topic_var, state="readonly", font=('Helvetica', 12), width=50)
        self.current_topic_entry.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")

        root.grid_rowconfigure(1, weight=1)
        root.grid_rowconfigure(2, weight=0)  
        root.grid_columnconfigure(0, weight=1)
        root.grid_columnconfigure(1, weight=0) 



    def update_tasks(self, event):
        selected_lab = self.lab_var.get()
        selected_task = self.task_var.get()
        tasks = self.lab_works.get(selected_lab, [])
        self.task_menu["values"] = tasks
        self.task_var.set("Виберіть завдання")
        self.info_button.config(state=tk.DISABLED)
        self.change_values_button.config(state=tk.DISABLED)
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
            self.change_values_button.config(state=tk.NORMAL)
            self.see_code_button.config(state=tk.NORMAL)
            self.show_button(self.current_topic_label)
            self.show_button(self.current_topic_entry)
            self.update_current_topic()
            script_path = self.task_paths[selected_lab][selected_task]
            result = self.run_script(script_path)
            self.code_entry.delete("1.0", tk.END)  
            self.code_entry.insert(tk.END, result)
        else:
            self.info_button.config(state=tk.DISABLED)
            self.change_values_button.config(state=tk.DISABLED)
            self.see_code_button.config(state=tk.DISABLED)
            self.hide_button(self.current_topic_label)
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

    def show_task_info(self):
        selected_lab = self.lab_var.get()
        selected_task = self.task_var.get()
        if selected_task:
            task_info = self.task_conditions.get(selected_lab, {}).get(selected_task, "Немає умови для цього завдання.")
            messagebox.showinfo(f"Умова для {selected_task}", task_info)

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
