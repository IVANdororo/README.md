def get_model():
    """Спрашиваем модель телефона"""
    print("\nВыберите модель:")
    print("1. iPhone")
    print("2. Samsung")
    print("3. Xiaomi")
    print("4. Google Pixel")
    print("5. Другое")

    choice = input("Введите номер (1-5): ")

    if choice == "1":
        return "iPhone"
    elif choice == "2":
        return "Samsung"
    elif choice == "3":
        return "Xiaomi"
    elif choice == "4":
        return "Google Pixel"
    else:
        return "Other"

def get_repair():
    """Спрашиваем тип ремонта"""
    print("\nВыберите тип ремонта:")
    print("1. Замена экрана")
    print("2. Замена аккумулятора")
    print("3. Ремонт материнской платы")

    choice = input("Введите номер (1-3): ")

    if choice == "1":
        return "screen"
    elif choice == "2":
        return "battery"
    else:
        return "motherboard"

def get_urgency():
    """Спрашиваем срочность"""
    print("\nСрочность:")
    print("1. Обычный (3-5 дней)")
    print("2. Срочный (1 день, +30%)")
    print("3. Экстренный (2-4 часа, +50%)")

    choice = input("Введите номер (1-3): ")

    if choice == "1":
        return "normal"
    elif choice == "2":
        return "urgent"
    else:
        return "emergency"

def get_services():
    """Спрашиваем доп услуги"""
    print("\nДополнительные услуги:")

    visit = input("Выезд мастера? (+500 руб) (y/n): ")
    glass = input("Защитное стекло? (+300 руб) (y/n): ")

    total = 0
    if visit == "y":
        total = total + 500
    if glass == "y":
        total = total + 300

    return total

def get_promocode():
    """Спрашиваем промокод"""
    code = input("Введите промокод (или Enter): ")
    return code

def get_parts_price(model, repair):
    """Автоматически берём цену запчасти из базы"""

    PARTS_PRICES = {
        "iPhone": {"screen": 5000, "battery": 2500, "motherboard": 8000},
        "Samsung": {"screen": 4000, "battery": 2000, "motherboard": 7000},
        "Xiaomi": {"screen": 3000, "battery": 1500, "motherboard": 6000},
        "Google Pixel": {"screen": 4500, "battery": 2200, "motherboard": 7500},
        "Other": {"screen": 2500, "battery": 1200, "motherboard": 5000}
    }

    price = PARTS_PRICES.get(model, {}).get(repair, 3000)
    print(f"\nСтоимость запчасти: {price} руб")

    return price

def get_all_data():
    """Собираем все данные в один словарь"""
    print("=" * 40)
    print("КАЛЬКУЛЯТОР РЕМОНТА ТЕЛЕФОНА")
    print("=" * 40)

    model = get_model()
    repair = get_repair()

    data = {
        "model": model,
        "repair": repair,
        "parts": get_parts_price(model, repair),
        "urgency": get_urgency(),
        "services": get_services(),
        "promocode": get_promocode()
    }

    return data
