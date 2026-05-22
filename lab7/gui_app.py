"""
Лабораторная работа №7
GUI приложение (Medium уровень)
Используем tkinter
"""

import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext
import json

from .lab4_rare.solution import count_recursive, count_iterative, calculate_x_recursive, calculate_x_iterative
from .lab5_rare.solution import make_calc, repeat
from .lab6_rare.solution import random_number_generator

class Lab7GUI:
    """Графический интерфейс для лабораторной работы №7"""
    
    def __init__(self, root):
        self.root = root
        self.root.title("Лабораторная работа №7 - Пакеты и модули")
        self.root.geometry("800x700")
        
        # Создаем вкладки
        self.notebook = ttk.Notebook(root)
        self.notebook.pack(fill='both', expand=True, padx=10, pady=10)
        
        # Вкладка 1: Lab 4
        self.tab_lab4 = ttk.Frame(self.notebook)
        self.notebook.add(self.tab_lab4, text='Lab 4 (Рекурсия)')
        self.create_lab4_tab()
        
        # Вкладка 2: Lab 5
        self.tab_lab5 = ttk.Frame(self.notebook)
        self.notebook.add(self.tab_lab5, text='Lab 5 (Замыкания)')
        self.create_lab5_tab()
        
        # Вкладка 3: Lab 6
        self.tab_lab6 = ttk.Frame(self.notebook)
        self.notebook.add(self.tab_lab6, text='Lab 6 (Генераторы)')
        self.create_lab6_tab()
        
        # Вкладка 4: Результаты
        self.tab_results = ttk.Frame(self.notebook)
        self.notebook.add(self.tab_results, text='Результаты')
        self.create_results_tab()
    
    def create_lab4_tab(self):
        """Создание вкладки Lab 4"""
        # Frame для подсчёта элементов
        count_frame = ttk.LabelFrame(self.tab_lab4, text="Подсчёт элементов в списке", padding=10)
        count_frame.pack(fill="x", padx=10, pady=5)
        
        ttk.Label(count_frame, text="Введите список (JSON формат):").pack(anchor="w")
        self.entry_list = ttk.Entry(count_frame, width=60)
        self.entry_list.insert(0, "[1, 2, [3, 4, [5]], 6]")
        self.entry_list.pack(pady=5)
        
        ttk.Button(count_frame, text="Рекурсивно", 
                  command=self.count_recursive).pack(side="left", padx=5)
        ttk.Button(count_frame, text="Итеративно", 
                  command=self.count_iterative).pack(side="left", padx=5)
        
        # Frame для последовательности
        seq_frame = ttk.LabelFrame(self.tab_lab4, text="Расчёт последовательности", padding=10)
        seq_frame.pack(fill="x", padx=10, pady=5)
        
        ttk.Label(seq_frame, text="Номер элемента (n):").pack(anchor="w")
        self.entry_n = ttk.Entry(seq_frame, width=20)
        self.entry_n.insert(0, "10")
        self.entry_n.pack(pady=5)
        
        ttk.Button(seq_frame, text="Вычислить x_n", 
                  command=self.calculate_sequence).pack(pady=5)
    
    def create_lab5_tab(self):
        """Создание вкладки Lab 5"""
        # Frame для калькулятора
        calc_frame = ttk.LabelFrame(self.tab_lab5, text="Калькулятор с замыканием", padding=10)
        calc_frame.pack(fill="x", padx=10, pady=5)
        
        ttk.Label(calc_frame, text="Операция (+, -, *, /):").pack(anchor="w")
        self.entry_operation = ttk.Entry(calc_frame, width=10)
        self.entry_operation.insert(0, "+")
        self.entry_operation.pack(pady=5)
        
        ttk.Label(calc_frame, text="Начальное значение:").pack(anchor="w")
        self.entry_initial = ttk.Entry(calc_frame, width=20)
        self.entry_initial.insert(0, "0")
        self.entry_initial.pack(pady=5)
        
        ttk.Label(calc_frame, text="Значения (через запятую):").pack(anchor="w")
        self.entry_values = ttk.Entry(calc_frame, width=40)
        self.entry_values.insert(0, "10, 5, 3")
        self.entry_values.pack(pady=5)
        
        ttk.Button(calc_frame, text="Вычислить", 
                  command=self.calculate).pack(pady=5)
    
    def create_lab6_tab(self):
        """Создание вкладки Lab 6"""
        # Frame для генератора
        gen_frame = ttk.LabelFrame(self.tab_lab6, text="Генератор случайных чисел", padding=10)
        gen_frame.pack(fill="x", padx=10, pady=5)
        
        ttk.Label(gen_frame, text="Количество чисел:").pack(anchor="w")
        self.entry_count = ttk.Entry(gen_frame, width=20)
        self.entry_count.insert(0, "10")
        self.entry_count.pack(pady=5)
        
        ttk.Label(gen_frame, text="Минимум:").pack(anchor="w")
        self.entry_min = ttk.Entry(gen_frame, width=20)
        self.entry_min.insert(0, "0")
        self.entry_min.pack(pady=5)
        
        ttk.Label(gen_frame, text="Максимум:").pack(anchor="w")
        self.entry_max = ttk.Entry(gen_frame, width=20)
        self.entry_max.insert(0, "100")
        self.entry_max.pack(pady=5)
        
        ttk.Button(gen_frame, text="Сгенерировать", 
                  command=self.generate_random).pack(pady=5)
    
    def create_results_tab(self):
        """Создание вкладки результатов"""
        self.results_text = scrolledtext.ScrolledText(self.tab_results, wrap=tk.WORD, width=80, height=30)
        self.results_text.pack(fill="both", expand=True, padx=10, pady=10)
        
        ttk.Button(self.tab_results, text="Очистить", 
                  command=self.clear_results).pack(pady=5)
    
    # ===== МЕТОДЫ ОБРАБОТКИ =====
    
    def add_result(self, title, result):
        """Добавление результата в лог"""
        self.results_text.insert(tk.END, f"\n{'='*60}\n")
        self.results_text.insert(tk.END, f"{title}\n")
        self.results_text.insert(tk.END, f"{'='*60}\n")
        self.results_text.insert(tk.END, f"{result}\n\n")
        self.results_text.see(tk.END)
    
    def clear_results(self):
        """Очистка результатов"""
        self.results_text.delete(1.0, tk.END)
    
    def count_recursive(self):
        """Рекурсивный подсчёт"""
        try:
            lst = json.loads(self.entry_list.get())
            result = count_recursive(lst)
            self.add_result("Подсчёт элементов (рекурсивно)", 
                          f"Список: {lst}\nРезультат: {result}")
        except Exception as e:
            messagebox.showerror("Ошибка", str(e))
    
    def count_iterative(self):
        """Итеративный подсчёт"""
        try:
            lst = json.loads(self.entry_list.get())
            result = count_iterative(lst)
            self.add_result("Подсчёт элементов (итеративно)", 
                          f"Список: {lst}\nРезультат: {result}")
        except Exception as e:
            messagebox.showerror("Ошибка", str(e))
    
    def calculate_sequence(self):
        """Расчёт последовательности"""
        try:
            n = int(self.entry_n.get())
            result = calculate_x_iterative(n)
            self.add_result(f"Расчёт последовательности x_{n}", 
                          f"x_{n} = {result:.10f}")
        except Exception as e:
            messagebox.showerror("Ошибка", str(e))
    
    def calculate(self):
        """Калькулятор"""
        try:
            operation = self.entry_operation.get()
            initial = float(self.entry_initial.get())
            values = [float(x.strip()) for x in self.entry_values.get().split(",")]
            
            calc = make_calc(operation, initial)
            for val in values:
                result = calc(val)
            
            self.add_result("Калькулятор", 
                          f"Операция: {operation}\nНачальное: {initial}\n"
                          f"Значения: {values}\nРезультат: {result}")
        except Exception as e:
            messagebox.showerror("Ошибка", str(e))
    
    def generate_random(self):
        """Генерация случайных чисел"""
        try:
            count = int(self.entry_count.get())
            min_val = int(self.entry_min.get())
            max_val = int(self.entry_max.get())
            
            gen = random_number_generator(min_val, max_val)
            numbers = [next(gen) for _ in range(count)]
            
            self.add_result("Генератор случайных чисел", 
                          f"Диапазон: [{min_val}, {max_val}]\n"
                          f"Количество: {count}\nЧисла: {numbers}")
        except Exception as e:
            messagebox.showerror("Ошибка", str(e))


def main():
    root = tk.Tk()
    app = Lab7GUI(root)
    root.mainloop()


if __name__ == "__main__":
    main()