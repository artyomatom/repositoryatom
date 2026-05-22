"""
ToDo Application - GUI приложение на Tkinter
Лабораторная работа №8
"""

import tkinter as tk
from tkinter import ttk, messagebox, simpledialog
from datetime import datetime, timedelta
from typing import Optional

from database import TodoDatabase


class TodoApp:
    """Основное приложение ToDo"""
    
    def __init__(self, root):
        self.root = root
        self.root.title("📝 ToDo Manager")
        self.root.geometry("1000x700")
        self.root.minsize(800, 600)
        
        # Инициализация БД
        self.db = TodoDatabase()
        
        # Словарь категорий
        self.categories = {}
        self.load_categories()
        
        # Создание интерфейса
        self.create_widgets()
        self.refresh_task_list()
        
        # Обработка закрытия окна
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
    
    def load_categories(self):
        """Загрузить категории из БД"""
        self.categories = {}
        for cat_id, name, color in self.db.get_categories():
            self.categories[name] = (cat_id, color)
    
    def create_widgets(self):
        """Создание элементов интерфейса"""
        
        # ===== ПАНЕЛЬ УПРАВЛЕНИЯ =====
        control_frame = ttk.LabelFrame(self.root, text="Управление задачами", padding=10)
        control_frame.pack(fill="x", padx=10, pady=5)
        
        # Кнопки действий
        ttk.Button(control_frame, text="➕ Добавить задачу", 
                  command=self.add_task).pack(side="left", padx=5)
        ttk.Button(control_frame, text="✅ Выполнить", 
                  command=self.complete_task).pack(side="left", padx=5)
        ttk.Button(control_frame, text="🗑️ Удалить", 
                  command=self.delete_task).pack(side="left", padx=5)
        ttk.Button(control_frame, text="📊 Статистика", 
                  command=self.show_statistics).pack(side="left", padx=5)
        ttk.Button(control_frame, text="🔄 Обновить", 
                  command=self.refresh_task_list).pack(side="left", padx=5)
        
        # ===== ФИЛЬТРЫ =====
        filter_frame = ttk.LabelFrame(self.root, text="Фильтры", padding=10)
        filter_frame.pack(fill="x", padx=10, pady=5)
        
        # Фильтр по статусу
        ttk.Label(filter_frame, text="Статус:").pack(side="left", padx=5)
        self.status_var = tk.StringVar(value="all")
        status_combo = ttk.Combobox(filter_frame, textvariable=self.status_var,
                                   values=["all", "pending", "completed"],
                                   state="readonly", width=15)
        status_combo.pack(side="left", padx=5)
        status_combo.bind("<<ComboboxSelected>>", lambda e: self.refresh_task_list())
        
        # Фильтр по категории
        ttk.Label(filter_frame, text="Категория:").pack(side="left", padx=5)
        self.category_var = tk.StringVar(value="all")
        category_combo = ttk.Combobox(filter_frame, textvariable=self.category_var,
                                     values=["all"] + list(self.categories.keys()),
                                     state="readonly", width=15)
        category_combo.pack(side="left", padx=5)
        category_combo.bind("<<ComboboxSelected>>", lambda e: self.refresh_task_list())
        
        # Фильтр по приоритету
        ttk.Label(filter_frame, text="Приоритет:").pack(side="left", padx=5)
        self.priority_var = tk.StringVar(value="all")
        priority_combo = ttk.Combobox(filter_frame, textvariable=self.priority_var,
                                     values=["all", "1", "2", "3"],
                                     state="readonly", width=10)
        priority_combo.pack(side="left", padx=5)
        priority_combo.bind("<<ComboboxSelected>>", lambda e: self.refresh_task_list())
        
        # ===== ТАБЛИЦА ЗАДАЧ =====
        table_frame = ttk.Frame(self.root)
        table_frame.pack(fill="both", expand=True, padx=10, pady=5)
        
        # Создание Treeview
        columns = ("id", "title", "category", "priority", "status", "due_date", "created_at")
        self.task_tree = ttk.Treeview(table_frame, columns=columns, show="headings", height=15)
        
        # Настройка колонок
        self.task_tree.heading("id", text="ID")
        self.task_tree.heading("title", text="Название")
        self.task_tree.heading("category", text="Категория")
        self.task_tree.heading("priority", text="Приоритет")
        self.task_tree.heading("status", text="Статус")
        self.task_tree.heading("due_date", text="Срок")
        self.task_tree.heading("created_at", text="Создана")
        
        self.task_tree.column("id", width=50)
        self.task_tree.column("title", width=300)
        self.task_tree.column("category", width=100)
        self.task_tree.column("priority", width=70)
        self.task_tree.column("status", width=100)
        self.task_tree.column("due_date", width=120)
        self.task_tree.column("created_at", width=150)
        
        # Скроллбар
        scrollbar = ttk.Scrollbar(table_frame, orient="vertical", 
                                 command=self.task_tree.yview)
        self.task_tree.configure(yscrollcommand=scrollbar.set)
        
        self.task_tree.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
        
        # Привязка двойного клика
        self.task_tree.bind("<Double-1>", lambda e: self.edit_task())
        
        # ===== ИНФОРМАЦИОННАЯ ПАНЕЛЬ =====
        self.info_label = ttk.Label(self.root, text="Готово", 
                                   relief="sunken", anchor="w")
        self.info_label.pack(fill="x", padx=10, pady=5)
    
    def refresh_task_list(self):
        """Обновить список задач"""
        # Очистка таблицы
        for item in self.task_tree.get_children():
            self.task_tree.delete(item)
        
        # Получение фильтров
        status = None if self.status_var.get() == "all" else self.status_var.get()
        category = self.category_var.get()
        category_id = None
        if category != "all":
            category_id = self.categories.get(category, (None,))[0]
        
        priority = None if self.priority_var.get() == "all" else int(self.priority_var.get())
        
        # Получение задач из БД
        tasks = self.db.get_tasks(status=status, category_id=category_id, 
                                 priority=priority)
        
        # Добавление в таблицу
        for task in tasks:
            task_id, title, desc, cat_name, priority, status, created, due, completed = task
            
            # Форматирование статуса
            status_text = "✅ Выполнено" if status == "completed" else "⏳ В процессе"
            
            # Форматирование приоритета
            priority_text = {1: "🔴 Высокий", 2: "🟡 Средний", 3: "🟢 Низкий"}.get(priority, str(priority))
            
            self.task_tree.insert("", "end", 
                                values=(task_id, title, cat_name or "Без категории",
                                       priority_text, status_text, 
                                       due or "Не указан", created))
        
        self.info_label.config(text=f"Загружено задач: {len(tasks)}")
    
    def add_task(self):
        """Диалог добавления задачи"""
        dialog = AddTaskDialog(self.root, list(self.categories.keys()))
        
        if dialog.result:
            try:
                category_id = None
                if dialog.result['category'] and dialog.result['category'] != "Без категории":
                    category_id = self.categories.get(dialog.result['category'], (None,))[0]
                
                self.db.add_task(
                    title=dialog.result['title'],
                    description=dialog.result.get('description', ''),
                    category_id=category_id,
                    priority=dialog.result['priority'],
                    due_date=dialog.result.get('due_date')
                )
                
                self.refresh_task_list()
                messagebox.showinfo("Успех", "Задача успешно добавлена!")
            except Exception as e:
                messagebox.showerror("Ошибка", f"Не удалось добавить задачу:\n{e}")
    
    def edit_task(self):
        """Редактирование выбранной задачи"""
        selected = self.task_tree.selection()
        if not selected:
            messagebox.showwarning("Внимание", "Выберите задачу для редактирования")
            return
        
        item = self.task_tree.item(selected[0])
        task_id = item['values'][0]
        
        # Получение полной информации о задаче
        tasks = self.db.get_tasks()
        task = None
        for t in tasks:
            if t[0] == task_id:
                task = t
                break
        
        if not task:
            return
        
        dialog = EditTaskDialog(self.root, task, list(self.categories.keys()))
        
        if dialog.result:
            try:
                category_id = None
                if dialog.result['category'] and dialog.result['category'] != "Без категории":
                    category_id = self.categories.get(dialog.result['category'], (None,))[0]
                
                self.db.update_task(
                    task_id,
                    title=dialog.result['title'],
                    description=dialog.result.get('description', ''),
                    category_id=category_id,
                    priority=dialog.result['priority'],
                    due_date=dialog.result.get('due_date')
                )
                
                self.refresh_task_list()
                messagebox.showinfo("Успех", "Задача обновлена!")
            except Exception as e:
                messagebox.showerror("Ошибка", f"Не удалось обновить задачу:\n{e}")
    
    def complete_task(self):
        """Отметить задачу как выполненную"""
        selected = self.task_tree.selection()
        if not selected:
            messagebox.showwarning("Внимание", "Выберите задачу для завершения")
            return
        
        item = self.task_tree.item(selected[0])
        task_id = item['values'][0]
        task_title = item['values'][1]
        
        if messagebox.askyesno("Подтверждение", 
                              f"Отметить задачу '{task_title}' как выполненную?"):
            self.db.complete_task(task_id)
            self.refresh_task_list()
            messagebox.showinfo("Успех", "Задача выполнена! 🎉")
    
    def delete_task(self):
        """Удалить задачу"""
        selected = self.task_tree.selection()
        if not selected:
            messagebox.showwarning("Внимание", "Выберите задачу для удаления")
            return
        
        item = self.task_tree.item(selected[0])
        task_id = item['values'][0]
        task_title = item['values'][1]
        
        if messagebox.askyesno("Подтверждение", 
                              f"Удалить задачу '{task_title}'?\nЭто действие нельзя отменить."):
            self.db.delete_task(task_id)
            self.refresh_task_list()
            messagebox.showinfo("Успех", "Задача удалена")
    
    def show_statistics(self):
        """Показать статистику"""
        stats = self.db.get_statistics()
        
        stat_text = f"""
📊 СТАТИСТИКА ЗАДАЧ

Всего задач: {stats['total']}
✅ Выполнено: {stats['completed']}
⏳ В процессе: {stats['pending']}

Прогресс: {stats['completed']}/{stats['total']} ({stats['completed']*100//stats['total'] if stats['total'] > 0 else 0}%)

По приоритетам:
"""
        for priority, count in sorted(stats.get('by_priority', {}).items()):
            priority_name = {1: "🔴 Высокий", 2: "🟡 Средний", 3: "🟢 Низкий"}.get(priority, str(priority))
            stat_text += f"  {priority_name}: {count}\n"
        
        messagebox.showinfo("📊 Статистика", stat_text)
    
    def on_closing(self):
        """Обработка закрытия окна"""
        if messagebox.askokcancel("Выход", "Закрыть приложение?"):
            self.db.close()
            self.root.destroy()


# ===== ДИАЛОГ ДОБАВЛЕНИЯ ЗАДАЧИ =====

class AddTaskDialog(simpledialog.Dialog):
    """Диалоговое окно для добавления задачи"""
    
    def __init__(self, parent, categories):
        self.categories = categories
        self.result = None
        super().__init__(parent, "Добавить задачу")
    
    def body(self, master):
        ttk.Label(master, text="Название:").grid(row=0, column=0, sticky="w", pady=5)
        self.title_entry = ttk.Entry(master, width=50)
        self.title_entry.grid(row=0, column=1, pady=5)
        self.title_entry.focus()
        
        ttk.Label(master, text="Описание:").grid(row=1, column=0, sticky="nw", pady=5)
        self.desc_text = tk.Text(master, width=50, height=5)
        self.desc_text.grid(row=1, column=1, pady=5)
        
        ttk.Label(master, text="Категория:").grid(row=2, column=0, sticky="w", pady=5)
        self.category_var = tk.StringVar(value="Без категории")
        category_combo = ttk.Combobox(master, textvariable=self.category_var,
                                     values=["Без категории"] + self.categories,
                                     state="readonly", width=30)
        category_combo.grid(row=2, column=1, pady=5)
        
        ttk.Label(master, text="Приоритет:").grid(row=3, column=0, sticky="w", pady=5)
        self.priority_var = tk.StringVar(value="2")
        ttk.Radiobutton(master, text="🔴 Высокий", variable=self.priority_var, value="1").grid(row=3, column=1, sticky="w")
        ttk.Radiobutton(master, text="🟡 Средний", variable=self.priority_var, value="2").grid(row=4, column=1, sticky="w")
        ttk.Radiobutton(master, text="🟢 Низкий", variable=self.priority_var, value="3").grid(row=5, column=1, sticky="w")
        
        ttk.Label(master, text="Срок выполнения (ГГГГ-ММ-ДД):").grid(row=6, column=0, sticky="w", pady=5)
        self.due_date_entry = ttk.Entry(master, width=30)
        self.due_date_entry.grid(row=6, column=1, pady=5)
        self.due_date_entry.insert(0, (datetime.now() + timedelta(days=7)).strftime("%Y-%m-%d"))
        
        return self.title_entry
    
    def validate(self):
        if not self.title_entry.get().strip():
            messagebox.showwarning("Внимание", "Введите название задачи")
            return False
        return True
    
    def apply(self):
        self.result = {
            'title': self.title_entry.get().strip(),
            'description': self.desc_text.get("1.0", tk.END).strip(),
            'category': self.category_var.get(),
            'priority': int(self.priority_var.get()),
            'due_date': self.due_date_entry.get().strip() or None
        }


# ===== ДИАЛОГ РЕДАКТИРОВАНИЯ ЗАДАЧИ =====

class EditTaskDialog(simpledialog.Dialog):
    """Диалоговое окно для редактирования задачи"""
    
    def __init__(self, parent, task, categories):
        self.task = task
        self.categories = categories
        self.result = None
        super().__init__(parent, "Редактировать задачу")
    
    def body(self, master):
        # task: (id, title, description, category, priority, status, created, due, completed)
        ttk.Label(master, text="Название:").grid(row=0, column=0, sticky="w", pady=5)
        self.title_entry = ttk.Entry(master, width=50)
        self.title_entry.grid(row=0, column=1, pady=5)
        self.title_entry.insert(0, self.task[1])
        self.title_entry.focus()
        
        ttk.Label(master, text="Описание:").grid(row=1, column=0, sticky="nw", pady=5)
        self.desc_text = tk.Text(master, width=50, height=5)
        self.desc_text.grid(row=1, column=1, pady=5)
        self.desc_text.insert("1.0", self.task[2] or "")
        
        ttk.Label(master, text="Категория:").grid(row=2, column=0, sticky="w", pady=5)
        self.category_var = tk.StringVar(value=self.task[3] or "Без категории")
        category_combo = ttk.Combobox(master, textvariable=self.category_var,
                                     values=["Без категории"] + self.categories,
                                     state="readonly", width=30)
        category_combo.grid(row=2, column=1, pady=5)
        
        ttk.Label(master, text="Приоритет:").grid(row=3, column=0, sticky="w", pady=5)
        self.priority_var = tk.StringVar(value=str(self.task[4]))
        ttk.Radiobutton(master, text="🔴 Высокий", variable=self.priority_var, value="1").grid(row=3, column=1, sticky="w")
        ttk.Radiobutton(master, text="🟡 Средний", variable=self.priority_var, value="2").grid(row=4, column=1, sticky="w")
        ttk.Radiobutton(master, text="🟢 Низкий", variable=self.priority_var, value="3").grid(row=5, column=1, sticky="w")
        
        ttk.Label(master, text="Срок выполнения (ГГГГ-ММ-ДД):").grid(row=6, column=0, sticky="w", pady=5)
        self.due_date_entry = ttk.Entry(master, width=30)
        self.due_date_entry.grid(row=6, column=1, pady=5)
        self.due_date_entry.insert(0, self.task[7] or "")
        
        return self.title_entry
    
    def validate(self):
        if not self.title_entry.get().strip():
            messagebox.showwarning("Внимание", "Введите название задачи")
            return False
        return True
    
    def apply(self):
        self.result = {
            'title': self.title_entry.get().strip(),
            'description': self.desc_text.get("1.0", tk.END).strip(),
            'category': self.category_var.get(),
            'priority': int(self.priority_var.get()),
            'due_date': self.due_date_entry.get().strip() or None
        }


# ===== ЗАПУСК ПРИЛОЖЕНИЯ =====

def main():
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()