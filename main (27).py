def lunar_weight_after_years(earth_weight, years, weight_gain_per_year=1):
    lunar_gravity = 1/6
    total_weight_gain = weight_gain_per_year * years
    final_earth_weight = earth_weight + total_weight_gain
    lunar_weight = final_earth_weight * lunar_gravity
    return lunar_weight

earth_weight = float(input("Введите вашу массу на Земле (в килограммах): "))

years = int(input("Введите количество лет: "))

lunar_weight = lunar_weight_after_years(earth_weight, years)
print(f"Ваш лунный вес через {years} лет составит примерно {lunar_weight:.2f} килограмма.")
