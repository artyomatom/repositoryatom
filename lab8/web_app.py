"""
ToDo Web API - Веб-приложение на FastAPI
"""

from fastapi import FastAPI, HTTPException, Query
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime
import uvicorn

from database import TodoDatabase

from .lab4_rare.solution import count_recursive, count_iterative, calculate_x_recursive, calculate_x_iterative
from .lab5_rare.solution import make_calc, repeat
from .lab6_rare.solution import random_number_generator

app = FastAPI(
    title="ToDo API",
    description="REST API для управления задачами",
    version="1.0.0"
)

# Инициализация БД
db = TodoDatabase()


# ===== МОДЕЛИ ДАННЫХ =====

class TaskCreate(BaseModel):
    title: str
    description: Optional[str] = ""
    category_id: Optional[int] = None
    priority: int = 2
    due_date: Optional[str] = None


class TaskUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    category_id: Optional[int] = None
    priority: Optional[int] = None
    status: Optional[str] = None
    due_date: Optional[str] = None


class TaskResponse(BaseModel):
    id: int
    title: str
    description: Optional[str]
    category: Optional[str]
    priority: int
    status: str
    created_at: str
    due_date: Optional[str]


# ===== HTML СТРАНИЦА =====

@app.get("/", response_class=HTMLResponse)
async def root():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>📝 ToDo API</title>
        <style>
            body { font-family: Arial; margin: 40px; background: #f5f5f5; }
            .container { max-width: 800px; margin: 0 auto; background: white;
                        padding: 30px; border-radius: 10px; box-shadow: 0 2px 10px rgba(0,0,0,0.1); }
            h1 { color: #4CAF50; }
            .endpoint { background: #f9f9f9; padding: 15px; margin: 10px 0;
                       border-left: 4px solid #4CAF50; }
            .method { display: inline-block; padding: 3px 10px; border-radius: 3px;
                     font-weight: bold; margin-right: 10px; }
            .get { background: #61affe; color: white; }
            .post { background: #49cc90; color: white; }
            .put { background: #fca130; color: white; }
            .delete { background: #f93e3e; color: white; }
            a { color: #4CAF50; }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>📝 ToDo API</h1>
            <p>REST API для управления задачами</p>
            
            <h2>📚 Endpoints:</h2>
            
            <div class="endpoint">
                <span class="method get">GET</span>
                <strong>/tasks</strong> - Получить все задачи<br>
                <small>Параметры: status, category_id, priority</small>
            </div>
            
            <div class="endpoint">
                <span class="method get">GET</span>
                <strong>/tasks/{task_id}</strong> - Получить задачу по ID
            </div>
            
            <div class="endpoint">
                <span class="method post">POST</span>
                <strong>/tasks</strong> - Создать задачу<br>
                <small>Body: title, description, category_id, priority, due_date</small>
            </div>
            
            <div class="endpoint">
                <span class="method put">PUT</span>
                <strong>/tasks/{task_id}</strong> - Обновить задачу
            </div>
            
            <div class="endpoint">
                <span class="method post">POST</span>
                <strong>/tasks/{task_id}/complete</strong> - Отметить как выполненную
            </div>
            
            <div class="endpoint">
                <span class="method delete">DELETE</span>
                <strong>/tasks/{task_id}</strong> - Удалить задачу
            </div>
            
            <div class="endpoint">
                <span class="method get">GET</span>
                <strong>/categories</strong> - Получить все категории
            </div>
            
            <div class="endpoint">
                <span class="method get">GET</span>
                <strong>/stats</strong> - Получить статистику
            </div>
            
            <div class="endpoint">
                <span class="method get">GET</span>
                <strong>/docs</strong> - Swagger документация<br>
                <small><a href="/docs">Открыть</a></small>
            </div>
        </div>
    </body>
    </html>
    """


# ===== API ENDPOINTS =====

@app.get("/tasks", response_model=List[TaskResponse])
async def get_tasks(
    status: Optional[str] = Query(None),
    category_id: Optional[int] = Query(None),
    priority: Optional[int] = Query(None)
):
    """Получить список задач с фильтрацией"""
    tasks = db.get_tasks(status=status, category_id=category_id, priority=priority)
    
    result = []
    for task in tasks:
        result.append(TaskResponse(
            id=task[0],
            title=task[1],
            description=task[2],
            category=task[3],
            priority=task[4],
            status=task[5],
            created_at=task[6],
            due_date=task[7]
        ))
    
    return result


@app.get("/tasks/{task_id}", response_model=TaskResponse)
async def get_task(task_id: int):
    """Получить задачу по ID"""
    tasks = db.get_tasks()
    for task in tasks:
        if task[0] == task_id:
            return TaskResponse(
                id=task[0],
                title=task[1],
                description=task[2],
                category=task[3],
                priority=task[4],
                status=task[5],
                created_at=task[6],
                due_date=task[7]
            )
    
    raise HTTPException(status_code=404, detail="Задача не найдена")


@app.post("/tasks", response_model=TaskResponse)
async def create_task(task: TaskCreate):
    """Создать новую задачу"""
    task_id = db.add_task(
        title=task.title,
        description=task.description,
        category_id=task.category_id,
        priority=task.priority,
        due_date=task.due_date
    )
    
    return await get_task(task_id)


@app.put("/tasks/{task_id}", response_model=TaskResponse)
async def update_task(task_id: int, task_update: TaskUpdate):
    """Обновить задачу"""
    update_data = task_update.dict(exclude_unset=True)
    if not update_data:
        raise HTTPException(status_code=400, detail="Нет данных для обновления")
    
    db.update_task(task_id, **update_data)
    return await get_task(task_id)


@app.post("/tasks/{task_id}/complete")
async def complete_task(task_id: int):
    """Отметить задачу как выполненную"""
    db.complete_task(task_id)
    return {"message": "Задача выполнена", "task_id": task_id}


@app.delete("/tasks/{task_id}")
async def delete_task(task_id: int):
    """Удалить задачу"""
    db.delete_task(task_id)
    return {"message": "Задача удалена", "task_id": task_id}


@app.get("/categories")
async def get_categories():
    """Получить все категории"""
    categories = db.get_categories()
    return [{"id": c[0], "name": c[1], "color": c[2]} for c in categories]


@app.get("/stats")
async def get_statistics():
    """Получить статистику"""
    return db.get_statistics()


@app.get("/health")
async def health_check():
    """Проверка работоспособности"""
    return {"status": "ok", "timestamp": datetime.now().isoformat()}


# ===== ЗАПУСК =====

def main():
    uvicorn.run(app, host="127.0.0.1", port=8001)


if __name__ == "__main__":
    main()