import string
import random


class URLShortener:
    def __init__(self):
        self._urls = {}
        self._code_length = 4

    def _generate_code(self):
        #Сгенерировать уникальный короткий код
        chars = string.ascii_lowercase + string.digits  # буквы a-z и цифры 0-9

        while True:
            code = ''.join(random.choice(chars) for _ in range(self._code_length))
            if code not in self._urls:
                return code

    def add_url(self, long_url):
        #Добавить ссылку
        for code, url in self._urls.items():
            if url == long_url:
                print(f"Такая ссылка уже существует с кодом: {code}")
                return code

        code = self._generate_code()
        self._urls[code] = long_url
        print(f"Ссылка сокращена! Короткий код: {code}")
        return code

    def get_url(self, code):
        #Получить длинную ссылку по коду
        if code in self._urls:
            return self._urls[code]
        else:
            print(f"Короткий код '{code}' не найден!")
            return None

    def check_code(self, code):
        #есть ли такой код
        return code in self._urls

    def get_all_urls(self):
        #отсортировать по коду
        if not self._urls:
            return {}
        # Сортируем по короткому коду
        sorted_items = sorted(self._urls.items())
        return dict(sorted_items)

    def show_all_urls(self):
        #Вывести все пары по сортировке
        if not self._urls:
            print("Список ссылок пуст!")
            return

        print("\n=== ВСЕ СОКРАЩЁННЫЕ ССЫЛКИ (отсортировано по коду) ===")
        sorted_urls = self.get_all_urls()
        for i, (code, url) in enumerate(sorted_urls.items(), 1):
            print(f"{i}. {code} -> {url}")
        print(f"Всего ссылок: {len(self._urls)}\n")



shortener = URLShortener()

while True:
    print("\n" + "=" * 50)
    print("СЕРВИС СОКРАЩЕНИЯ ССЫЛОК")
    print("=" * 50)
    print("1. Добавить новую ссылку")
    print("2. Получить длинную ссылку по короткому коду")
    print("3. Проверить существование короткого кода")
    print("4. Вывести все сокращённые ссылки")
    print("0. Выход")
    print("=" * 50)

    choice = input("Выберите действие: ")

    if choice == "1":
        print("\n--- Добавление новой ссылки ---")
        long_url = input("Введите длинную ссылку: ")

        if long_url.strip() == "":
            print("Ссылка не может быть пустой!")
        else:
            code = shortener.add_url(long_url)
            print(f"Готово! Короткий код: {code}")

    elif choice == "2":
        print("\n--- Получение оригинальной ссылки ---")
        code = input("Введите короткий код: ")

        if code.strip() == "":
            print("Короткий код не может быть пустым!")
        else:
            long_url = shortener.get_url(code)
            if long_url:
                print(f"Оригинальная ссылка: {long_url}")

    elif choice == "3":
        print("\n--- Проверка существования кода ---")
        code = input("Введите короткий код: ")

        if code.strip() == "":
            print("Короткий код не может быть пустым!")
        else:
            if shortener.check_code(code):
                print(f"Короткий код '{code}' существует!")
                print(f"Соответствует ссылке: {shortener.get_url(code)}")
            else:
                print(f"Короткий код '{code}' НЕ существует!")

    elif choice == "4":
        shortener.show_all_urls()

    elif choice == "0":
        print("До свидания!")
        break

    else:
        print("Неверный ввод! Пожалуйста, выберите пункт от 0 до 4")