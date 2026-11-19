class CustomerProfile:
    def __init__(self, user_id, email, password_hash, city, loyalty_points):
        self.user_id = user_id
        self.email = email
        self.password_hash = password_hash
        self.city = city
        self.loyalty_points = loyalty_points


# 2. Ліквідація Stamp Coupling: приймаємо лише примітиви (city та weight_kg) замість об'єкта CustomerProfile
def calculate_delivery_cost(city: str, weight_kg: float) -> float:
    if city == "Ivano-Frankivsk":
        base_rate = 50.0
    elif city == "Kyiv":
        base_rate = 80.0
    else:
        base_rate = 110.0
    return base_rate + (weight_kg * 15.0)


# 1 та 3. Ліквідація Common та Control Coupling: прибрано GLOBAL_TAX_RATE і mode_flag,
# ставку податку передаємо явно як аргумент зі значенням за замовчуванням 0.20
def process_standard_invoice(amount: float, city: str, weight_kg: float, tax_rate: float = 0.20) -> dict:
    delivery = calculate_delivery_cost(city, weight_kg)
    total = (amount * (1 + tax_rate)) + delivery
    return {"status": "PROCESSED", "total": round(total, 2)}


# 3. Окрема функція для розрахунку без податку (замість гілки mode_flag == 2)
def process_tax_exempt_invoice(amount: float, city: str, weight_kg: float) -> dict:
    delivery = calculate_delivery_cost(city, weight_kg)
    total = amount + delivery
    return {"status": "TAX_EXEMPT", "total": round(total, 2)}
