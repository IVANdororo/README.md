from input_handler import get_all_data
from calculator import calc_total, compare_options
from logger import log_start, log_input, log_result, log_error
from receipt import print_receipt

def main():
    try:
        log_start()
        
        data = get_all_data()
        log_input(data)
        
        result = calc_total(data)
        log_result(result)
        
        # Сравниваем варианты (оригинал vs аналог)
        comparison = compare_options(data['model'], data['repair'], data['urgency'])
        
        # Печатаем чек
        print_receipt(data, result)
        
        # Печатаем рекомендацию
        print("\n" + "=" * 40)
        print("       РЕКОМЕНДАЦИЯ")
        print("=" * 40)
        print(f"Оригинал: {comparison['original']:.2f} руб")
        print(f"Аналог:   {comparison['analog']:.2f} руб")
        print(f"Лучше взять: {comparison['best']}")
        print(f"Экономия: {comparison['savings']:.2f} руб")
        print("=" * 40)
        
    except Exception as e:
        log_error(str(e))
        print(f"Ошибка: {e}")

if __name__ == "__main__":
    main()
