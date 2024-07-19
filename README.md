## Описание
# Lib_calculating_area_shapes

 "библиотека для поставки внешним клиентам, которая умеет вычислять площадь круга по радиусу и треугольника по трем сторонам."

## Стек технологий

- Python
- setuptools

## Локальная установка проекта

1. #### Склонируйте репозиторий:
```
git clone git@github.com:aleksei-astapoff/lib_calculating_area_shapes.git
```

2. #### Создайте и активируйте виртуальное окружение если его нет:
Команда для установки виртуального окружения на Mac или Linux:
```
python3 -m venv env

source venv/bin/activate
```

Команда для установки виртуального окружения на Windows:
```
python -m venv venv

source venv/Scripts/activate
```

3. #### Установите зависимости:
В папке где находится файл requirements.txt выполните команду:
```
pip install -r requirements.txt
```

4. #### Через пакетный менеджер установите библиотеку:
В терминале выполните команду:
```
pip install -e .
```

5. #### Запустите тесты, чтобы убедиться, что все работает корректно:
В терминале выполните команду:
```
python -m unittest discover lib_calculating_area_shapes
```
6. #### Теперь можно импортировать функцию для расчета площади круга по радиусу и треугольника по трем сторонам.
Пример кода создайте файл example.py и вставьте в него код:
```
from lib_calculating_area_shapes import calculate_area

def main():
    print(calculate_area(5))           # Круг
    print(calculate_area(3, 4, 5))     # Прямоугольный треугольник
    print(calculate_area(3, 4, 6))     # Треугольник

if __name__ == "__main__":
    main()
```