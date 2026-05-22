"""
Модуль работы с базой данных SQLite
"""

import sqlite3
from datetime import datetime
from typing import List, Tuple, Optional
import os


class TodoDatabase:
    """Класс для работы с базой данных ToDo задач"""
    
    def __init__(self, db_name: str = "todo.db"):
        """
        Инициализация подключения к БД
        """
        self.db_name = db_name
        self.conn = None
        self.cursor = None
        self.connect()
        self.create_tables()
    
    def connect(self):
        """Подключение к базе данных"""
        try:
            self.conn = sqlite3.connect(self.db_name)
            self.cursor = self.conn.cursor()
            print(f"✓ Подключено к базе данных: {self.db_name}")
        except sqlite3.Error as e:
            print(f"✗ Ошибка подключения к БД: {e}")
            raise
    
    def create_tables(self):
        """Создание таблиц если они не существуют"""
        # Таблица категорий
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS categories (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL UNIQUE,
                color TEXT DEFAULT '#FFFFFF'
            )
        ''')
        
        # Таблица задач
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS tasks (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                description TEXT,
                category_id INTEGER,
                priority INTEGER DEFAULT 1,
                status TEXT DEFAULT 'pending',
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                due_date TIMESTAMP,
                completed_at TIMESTAMP,
                FOREIGN KEY (category_id) REFERENCES categories (id)
                    ON DELETE SET NULL
            )
        ''')
        
        self.conn.commit()
        
        # Добавляем стандартные категории если таблица пустая
        self.cursor.execute("SELECT COUNT(*) FROM categories")
        if self.cursor.fetchone()[0] == 0:
            default_categories = [
                ('Работа', '#FF6B6B'),
                ('Личное', '#4ECDC4'),
                ('Учёба', '#45B7D1'),
                ('Покупки', '#FFA07A'),
                ('Здоровье', '#98D8C8')
            ]
            self.cursor.executemany(
                "INSERT INTO categories (name, color) VALUES (?, ?)",
                default_categories
            )
            self.conn.commit()
            print("✓ Добавлены категории по умолчанию")
    
    # ===== КАТЕГОРИИ =====
    
    def get_categories(self) -> List[Tuple]:
        """Получить все категории"""
        self.cursor.execute("SELECT * FROM categories")
        return self.cursor.fetchall()
    
    def add_category(self, name: str, color: str = '#FFFFFF') -> int:
        """Добавить категорию"""
        try:
            self.cursor.execute(
                "INSERT INTO categories (name, color) VALUES (?, ?)",
                (name, color)
            )
            self.conn.commit()
            return self.cursor.lastrowid
        except sqlite3.IntegrityError:
            print(f"✗ Категория '{name}' уже существует")
            return -1
    
    def delete_category(self, category_id: int):
        """Удалить категорию"""
        self.cursor.execute("DELETE FROM categories WHERE id = ?", (category_id,))
        self.conn.commit()
    
    # ===== ЗАДАЧИ =====
    
    def add_task(self, title: str, description: str = "", 
                 category_id: int = None, priority: int = 1,
                 due_date: str = None) -> int:
        """
        Добавить новую задачу
        Возвращает ID созданной задачи
        """
        self.cursor.execute('''
            INSERT INTO tasks (title, description, category_id, priority, due_date)
            VALUES (?, ?, ?, ?, ?)
        ''', (title, description, category_id, priority, due_date))
        self.conn.commit()
        return self.cursor.lastrowid
    
    def get_tasks(self, status: str = None, category_id: int = None,
                  priority: int = None) -> List[Tuple]:
        """
        Получить задачи с фильтрацией
        """
        query = '''
            SELECT t.id, t.title, t.description, c.name, t.priority,
                   t.status, t.created_at, t.due_date, t.completed_at
            FROM tasks t
            LEFT JOIN categories c ON t.category_id = c.id
            WHERE 1=1
        '''
        params = []
        
        if status:
            query += " AND t.status = ?"
            params.append(status)
        
        if category_id:
            query += " AND t.category_id = ?"
            params.append(category_id)
        
        if priority:
            query += " AND t.priority = ?"
            params.append(priority)
        
        query += " ORDER BY t.priority DESC, t.created_at DESC"
        
        self.cursor.execute(query, params)
        return self.cursor.fetchall()
    
    def update_task(self, task_id: int, **kwargs):
        """
        Обновить задачу
        kwargs: title, description, category_id, priority, status, due_date
        """
        if not kwargs:
            return
        
        set_clause = ", ".join([f"{key} = ?" for key in kwargs.keys()])
        values = list(kwargs.values()) + [task_id]
        
        query = f"UPDATE tasks SET {set_clause} WHERE id = ?"
        self.cursor.execute(query, values)
        self.conn.commit()
    
    def complete_task(self, task_id: int):
        """Отметить задачу как выполненную"""
        self.cursor.execute('''
            UPDATE tasks 
            SET status = 'completed', completed_at = ?
            WHERE id = ?
        ''', (datetime.now().strftime("%Y-%m-%d %H:%M:%S"), task_id))
        self.conn.commit()
    
    def delete_task(self, task_id: int):
        """Удалить задачу"""
        self.cursor.execute("DELETE FROM tasks WHERE id = ?", (task_id,))
        self.conn.commit()
    
    def get_statistics(self) -> dict:
        """Получить статистику по задачам"""
        stats = {}
        
        # Общее количество задач
        self.cursor.execute("SELECT COUNT(*) FROM tasks")
        stats['total'] = self.cursor.fetchone()[0]
        
        # Выполненные
        self.cursor.execute("SELECT COUNT(*) FROM tasks WHERE status = 'completed'")
        stats['completed'] = self.cursor.fetchone()[0]
        
        # В процессе
        self.cursor.execute("SELECT COUNT(*) FROM tasks WHERE status = 'pending'")
        stats['pending'] = self.cursor.fetchone()[0]
        
        # По приоритетам
        self.cursor.execute('''
            SELECT priority, COUNT(*) 
            FROM tasks 
            GROUP BY priority
        ''')
        stats['by_priority'] = dict(self.cursor.fetchall())
        
        return stats
    
    def close(self):
        """Закрыть подключение к БД"""
        if self.conn:
            self.conn.close()
            print("✓ Подключение к БД закрыто")
    
    def __del__(self):
        """Деструктор"""
        self.close()