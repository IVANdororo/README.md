from config import PRICES, URGENCY, SERVICES, PROMOCODES


def calc_labor(model, repair):
    """Считаем стоимость работы"""
    # Берем цены для модели, если нет такой - берем Other
    if model in PRICES:
        model_prices = PRICES[model]
    else:
        model_prices = PRICES["Other"]
    
    # Берем цену для типа ремонта
    return model_prices.get(repair, 0)


def calc_total(data):
    """Главная функция расчета"""
    
    # 1. Достаем данные
    model = data["model"]
    repair = data["repair"]
    parts = data["parts"]
    urgency = data["urgency"]
    services = data["services"]
    promocode = data["promocode"]
    
    # 2. Считаем работу
    labor = calc_labor(model, repair)
    
    # 3. Диагностика (500 руб, если ремонт не сложный)
    if repair == "motherboard":
        diagnostics = 0
    else:
        diagnostics = 500
    
    # 4. Промежуточная сумма
    subtotal = labor + parts + diagnostics + services
    
    # 5. Умножаем на срочность
    multiplier = URGENCY[urgency]
    total = subtotal * multiplier
    
    # 6. Применяем промокод
    discount = 0
    if promocode == "SERVICE10":
        discount = total * 0.10  # 10% скидка
        total = total - discount
    elif promocode == "REMONT26":
        discount = labor * 0.15  # 15% скидка на работы
        total = total - discount
    
    # 7. Возвращаем результат с деталями
    result = {
        "labor": labor,
        "parts": parts,
        "diagnostics": diagnostics,
        "services": services,
        "subtotal": subtotal,
        "multiplier": multiplier,
        "discount": discount,
        "total": total
    }
    
    return result
