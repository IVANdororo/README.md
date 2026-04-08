from input_handler import get_all_data
from calculator import calc_total
from logger import log_start, log_input, log_result, log_error
from receipt import print_receipt


def main():
    try:
        # 1. Начинаем лог
        log_start()
        
        # 2. Получаем данные от пользователя
        data = get_all_data()
        log_input(data)
        
        # 3. Считаем стоимость
        result = calc_total(data)
        log_result(result)
        
        # 4. Печатаем чек
        print_receipt(data, result)
        
    except Exception as e:
        log_error(str(e))
        print(f"Ошибка: {e}")


# Запускаем программу
if __name__ == "__main__":
    main()
