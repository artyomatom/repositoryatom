"""
Лабораторная работа №7
Веб-приложение (Well-done уровень)
Используем FastAPI
"""

from fastapi import FastAPI, HTTPException, Query
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
from typing import List, Optional, Union
import uvicorn

from .lab4_rare.solution import count_recursive, count_iterative, calculate_x_recursive, calculate_x_iterative
from .lab5_rare.solution import make_calc, repeat
from .lab6_rare.solution import random_number_generator


app = FastAPI(
    title="Лабораторная работа №7",
    description="API для пакета с лабораторными работами №4-6",
    version="1.0.0"
)


# ===== МОДЕЛИ ДАННЫХ =====

class CountRequest(BaseModel):
    elements: List[Union[int, float, str, list]]
    method: str = "recursive"


class SequenceRequest(BaseModel):
    n: int
    method: str = "iterative"


class CalculatorRequest(BaseModel):
    operation: str
    values: List[float]
    initial: float = 0.0


class RandomRequest(BaseModel):
    count: int = 10
    min_val: int = 0
    max_val: int = 100


class CountResponse(BaseModel):
    result: int
    method: str
    elements_count: int


class SequenceResponse(BaseModel):
    n: int
    value: float
    method: str


class CalculatorResponse(BaseModel):
    result: float
    operation: str
    steps: int


class RandomResponse(BaseModel):
    numbers: List[int]
    count: int
    range: dict


# ===== HTML СТРАНИЦА =====

@app.get("/", response_class=HTMLResponse)
async def root():
    """Главная страница с документацией"""
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Лабораторная работа №7</title>
        <style>
            body { font-family: Arial, sans-serif; margin: 40px; background: #f5f5f5; }
            .container { max-width: 800px; margin: 0 auto; background: white; 
                        padding: 30px; border-radius: 10px; box-shadow: 0 2px 10px rgba(0,0,0,0.1); }
            h1 { color: #333; border-bottom: 3px solid #4CAF50; padding-bottom: 10px; }
            h2 { color: #4CAF50; margin-top: 30px; }
            .endpoint { background: #f9f9f9; padding: 15px; margin: 10px 0; 
                       border-left: 4px solid #4CAF50; }
            .method { display: inline-block; padding: 3px 10px; border-radius: 3px; 
                     font-weight: bold; margin-right: 10px; }
            .get { background: #61affe; color: white; }
            .post { background: #49cc90; color: white; }
            a { color: #4CAF50; text-decoration: none; }
            a:hover { text-decoration: underline; }
            .footer { margin-top: 40px; padding-top: 20px; border-top: 1px solid #ddd; 
                     color: #666; font-size: 12px; }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>🚀 Лабораторная работа №7</h1>
            <h2>Пакеты и модули</h2>
            <p>API для работы с лабораторными работами №4-6</p>
            
            <h2>📚 Доступные эндпоинты:</h2>
            
            <div class="endpoint">
                <span class="method get">GET</span>
                <strong>/api/count</strong> - Подсчёт элементов в списке<br>
                <small>Параметры: elements (JSON), method (recursive/iterative)</small>
            </div>
            
            <div class="endpoint">
                <span class="method get">GET</span>
                <strong>/api/sequence</strong> - Расчёт последовательности x_n<br>
                <small>Параметры: n, method (recursive/iterative)</small>
            </div>
            
            <div class="endpoint">
                <span class="method post">POST</span>
                <strong>/api/calculate</strong> - Калькулятор с замыканием<br>
                <small>Body: operation, values, initial</small>
            </div>
            
            <div class="endpoint">
                <span class="method get">GET</span>
                <strong>/api/random</strong> - Генератор случайных чисел<br>
                <small>Параметры: count, min_val, max_val</small>
            </div>
            
            <div class="endpoint">
                <span class="method get">GET</span>
                <strong>/docs</strong> - Интерактивная документация (Swagger)<br>
                <small><a href="/docs">Открыть Swagger UI</a></small>
            </div>
            
            <div class="footer">
                <p>Лабораторная работа №7 | Пакеты и модули | 2024</p>
            </div>
        </div>
    </body>
    </html>
    """


# ===== API ENDPOINTS =====

@app.get("/api/count", response_model=CountResponse)
async def api_count_elements(
    elements: str = Query(..., description="Список элементов в JSON формате"),
    method: str = Query("recursive", description="Метод: recursive или iterative")
):
    """
    Подсчёт элементов в списке (включая вложенные)
    """
    import json
    try:
        lst = json.loads(elements)
    except json.JSONDecodeError:
        raise HTTPException(status_code=400, detail="Некорректный JSON формат")
    
    if method == "recursive":
        result = count_recursive(lst)
    elif method == "iterative":
        result = count_iterative(lst)
    else:
        raise HTTPException(status_code=400, detail="Метод должен быть 'recursive' или 'iterative'")
    
    return CountResponse(result=result, method=method, elements_count=len(lst))


@app.get("/api/sequence", response_model=SequenceResponse)
async def api_calculate_sequence(
    n: int = Query(..., description="Номер элемента", ge=1),
    method: str = Query("iterative", description="Метод: recursive или iterative")
):
    """
    Расчёт последовательности x_n
    """
    if method == "recursive":
        if n > 20:
            raise HTTPException(status_code=400, detail="n слишком большое для рекурсивного метода")
        result = calculate_x_recursive(n)
    elif method == "iterative":
        result = calculate_x_iterative(n)
    else:
        raise HTTPException(status_code=400, detail="Метод должен быть 'recursive' или 'iterative'")
    
    return SequenceResponse(n=n, value=result, method=method)


@app.post("/api/calculate", response_model=CalculatorResponse)
async def api_calculator(request: CalculatorRequest):
    """
    Калькулятор с замыканием
    """
    if request.operation not in ['+', '-', '*', '/']:
        raise HTTPException(status_code=400, detail="Неподдерживаемая операция")
    
    calc = make_calc(request.operation, request.initial)
    
    for val in request.values:
        result = calc(val)
    
    return CalculatorResponse(
        result=result,
        operation=request.operation,
        steps=len(request.values)
    )


@app.get("/api/random", response_model=RandomResponse)
async def api_random_numbers(
    count: int = Query(10, ge=1, le=1000, description="Количество чисел"),
    min_val: int = Query(0, description="Минимальное значение"),
    max_val: int = Query(100, description="Максимальное значение")
):
    """
    Генератор случайных чисел
    """
    if min_val > max_val:
        raise HTTPException(status_code=400, detail="min_val не может быть больше max_val")
    
    gen = random_number_generator(min_val, max_val)
    numbers = [next(gen) for _ in range(count)]
    
    return RandomResponse(
        numbers=numbers,
        count=count,
        range={"min": min_val, "max": max_val}
    )


@app.get("/api/health")
async def health_check():
    """Проверка работоспособности API"""
    return {"status": "ok", "version": "1.0.0"}


# ===== ЗАПУСК =====

def main():
    uvicorn.run(app, host="127.0.0.1", port=8000)


if __name__ == "__main__":
    main()