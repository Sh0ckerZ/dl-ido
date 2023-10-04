salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
months = 10  # Количество месяцев, которое планируется протянуть без долгов
increase = 0.03  # Ежемесячный рост цен

# TODO Рассчитайте подушку безопасности, чтобы протянуть 10 месяцев без долгов
# Инициализация финансовой подушки безопасности
money_capital = 0

# Цикл для моделирования ситуации на протяжении 10 месяцев
for month in range(1, months+1):
    if month != 1:
    # Вычисляем текущие расходы на проживание
        spend = (spend * (1 + increase))
    # Покрываем расходы сначала зарплатой, а затем из подушки безопасности
    if salary < spend:
        money_capital += spend - salary
print("Подушка безопасности, чтобы протянуть 10 месяцев без долгов:",int(money_capital))