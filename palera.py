import random

# =====================================================
# ШАБЛОН 1: РАБОТА С МАССИВАМИ (задачи 1-30, вариант 1)
# =====================================================

def generate_array(size, min_val=-100, max_val=100, is_float=False):
    """Генерация массива с рандомными элементами"""
    if is_float:
        return [round(random.uniform(min_val, max_val), 2) for _ in range(size)]
    else:
        return [random.randint(min_val, max_val) for _ in range(size)]


def read_array_from_file(filename):
    """Чтение массива из файла"""
    with open(filename, 'r', encoding='utf-8') as f:
        data = f.read().strip()
        # Массив может быть записан через пробел или запятую
        if ',' in data:
            return [float(x) if '.' in x else int(x) for x in data.split(',')]
        else:
            return [float(x) if '.' in x else int(x) for x in data.split()]


def write_result_to_file(filename, result):
    """Запись результата в файл"""
    with open(filename, 'w', encoding='utf-8') as f:
        if isinstance(result, list):
            f.write(' '.join(map(str, result)))
        else:
            f.write(str(result))


# Пример задачи 1: Найти количество четных элементов
def task_1(input_file='input.txt', output_file='output.txt'):
    """Найти количество элементов четных по значению"""
    arr = read_array_from_file(input_file)
    count = sum(1 for x in arr if x % 2 == 0)
    write_result_to_file(output_file, count)
    return count


# Пример задачи 4: Поменять местами максимальный и первый элементы
def task_4(input_file='input.txt', output_file='output.txt'):
    """Поменять местами максимальный и первый элементы"""
    arr = read_array_from_file(input_file)
    max_idx = arr.index(max(arr))
    arr[0], arr[max_idx] = arr[max_idx], arr[0]
    write_result_to_file(output_file, arr)
    return arr


# Пример задачи 12: Сортировка по убыванию и сумма мин/макс
def task_12(input_file='input.txt', output_file='output.txt'):
    """Расположить элементы по убыванию. Сумма мин и макс"""
    arr = read_array_from_file(input_file)
    sorted_arr = sorted(arr, reverse=True)
    result_sum = max(arr) + min(arr)
    
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(' '.join(map(str, sorted_arr)) + '\n')
        f.write(f'Сумма: {result_sum}')
    
    return sorted_arr, result_sum


# =====================================================
# ШАБЛОН 2: РАБОТА С ДВУМЯ МАССИВАМИ (задачи 1-30, вариант 2)
# =====================================================

def task_two_arrays_example(input_file='input.txt', output_file='output.txt'):
    """Пример работы с двумя массивами"""
    with open(input_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        arr1 = list(map(int, lines[0].strip().split()))
        arr2 = list(map(int, lines[1].strip().split()))
    
    # Обработка двух массивов
    result = []  # Здесь ваша логика
    
    write_result_to_file(output_file, result)
    return result


# =====================================================
# ШАБЛОН 3: РАБОТА СО СТРОКАМИ
# =====================================================

def task_string_analysis(input_file='input.txt', output_file='output.txt'):
    """Подсчет букв в строке (задача 1 из раздела строк)"""
    with open(input_file, 'r', encoding='utf-8') as f:
        text = f.read().strip()
    
    # Подсчет букв
    letter_count = {}
    for char in text.lower():
        if char.isalpha():
            letter_count[char] = letter_count.get(char, 0) + 1
    
    # Вывод в алфавитном порядке
    with open(output_file, 'w', encoding='utf-8') as f:
        for letter in sorted(letter_count.keys()):
            f.write(f'{letter} – {letter_count[letter]}\n')
    
    return letter_count


# =====================================================
# ШАБЛОН 4: РАБОТА С КЛАССАМИ
# =====================================================

class Mfu:
    """Класс МФУ (многофункциональное устройство)"""
    
    def __init__(self, model):
        self.model = model
        self.scanned_total = 0
        self.printed_total = 0
    
    def to_scan(self, sheets):
        """Сканирование листов"""
        self.scanned_total += sheets
        print(f'Сканирование завершено. Сканер "{self.model}" отсканировал {sheets} листов.')
    
    def to_print(self, sheets):
        """Печать листов"""
        self.printed_total += sheets
        print(f'Печать завершена. Принтер "{self.model}" распечатал {sheets} листов.')
    
    def scan_info(self):
        """Информация о сканировании"""
        print(f'Общее количество отсканированных листов - {self.scanned_total}.')
    
    def print_info(self):
        """Информация о печати"""
        print(f'Общее количество распечатанных листов - {self.printed_total}.')
    
    def scan_reset(self):
        """Сброс счетчика сканирования"""
        self.scanned_total = 0
        print(f'Сканер "{self.model}" обнулил счетчик сканированных листов.')
    
    def print_reset(self):
        """Сброс счетчика печати"""
        self.printed_total = 0
        print(f'Принтер "{self.model}" обнулил счетчик распечатанных листов.')


# =====================================================
# ШАБЛОН 5: РАБОТА С ФАЙЛАМИ (задача 4 из раздела файлов)
# =====================================================

def task_file_processing(input_file='in.txt', output_file='out.txt'):
    """Максимальная сумма в строке и среднее арифметическое"""
    with open(input_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    all_numbers = []
    max_sum = 0
    
    for line in lines:
        # Парсинг чисел из строки (через ; или пробел)
        numbers = [int(x.strip()) for x in line.replace(';', ' ').split() if x.strip().isdigit()]
        line_sum = sum(numbers)
        max_sum = max(max_sum, line_sum)
        all_numbers.extend(numbers)
    
    avg = sum(all_numbers) / len(all_numbers) if all_numbers else 0
    
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(f'{max_sum}\n')
        f.write(f'{avg:.1f}')
    
    return max_sum, avg


# =====================================================
# ОСНОВНАЯ ПРОГРАММА ДЛЯ ТЕСТИРОВАНИЯ
# =====================================================

if __name__ == '__main__':
    # Пример 1: Генерация массива и запись в файл
    arr = generate_array(14, -50, 50, is_float=False)
    write_result_to_file('input.txt', arr)
    print(f'Сгенерирован массив: {arr}')
    
    # Пример 2: Решение задачи
    result = task_1('input.txt', 'output.txt')
    print(f'Результат задачи 1: {result}')
    
    # Пример 3: Работа с классом
    print('\nПример работы с классом МФУ:')
    mfu = Mfu('HP')
    mfu.to_scan(15)
    mfu.to_print(44)
    mfu.scan_info()
    mfu.print_info()
