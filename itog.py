import datetime
import logging
import argparse

logging.basicConfig(level=logging.INFO)  # Настройка базового логгера

class MyStr(str):
    def __new__(cls, value, author):
        logging.info(f"Создается объект MyStr с value='{value}' и author='{author}'")
        obj = super().__new__(cls)
        obj.value = value
        obj.author = author
        obj.time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M')
        return obj

    def __str__(self):
        return f"{self.value} (Автор: {self.author}, Время создания: {self.time})"

    def __repr__(self):
        return f"MyStr('{self.value}', '{self.author}')"

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Создает объект MyStr")
    parser.add_argument("value", help="Значение объекта")
    parser.add_argument("author", help="Автор объекта")
    args = parser.parse_args()

    try:
        my_str = MyStr(args.value, args.author)
        logging.info(f"Создан объект MyStr: {my_str}")
        print(my_str)
    except Exception as e:
        logging.error(f"Ошибка при создании объекта MyStr: {e}")
 
 #вызов из терминала:  python itog.py "Hello, world!" "Яна" 
