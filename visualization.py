


import matplotlib.pyplot as plt

# Результати запитів
result_query_1 = [('Lada', 8200), ('Toyota', 29600), ('Volvo', 3900), ('Subaru', 10900)]
result_query_2 = [('Lada', 15266), ('Toyota', 31050), ('Volvo', 6700), ('Subaru', 10900)]
result_query_3 = [('grey', 1), ('blue', 1), ('silver', 3), ('other', 2)]

# Побудова графіків
# Стовпчикова діаграма для першого запиту
plt.figure(figsize=(8, 6))
manufacturers_1 = [row[0] for row in result_query_1]
prices_1 = [row[1] for row in result_query_1]
plt.bar(manufacturers_1, prices_1, color='skyblue')
plt.xlabel('Виробники')
plt.ylabel('Ціна')
plt.title('Ціна найдорожчого авто від виробника')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Кругова діаграма для другого запиту
plt.figure(figsize=(6, 6))
manufacturers_2 = [row[0] for row in result_query_2]
incomes_2 = [row[1] for row in result_query_2]
plt.pie(incomes_2, labels=manufacturers_2, autopct='%1.1f%%', colors=plt.cm.Set3.colors)
plt.title('Загальний прибуток від виробника')
plt.axis('equal')
plt.tight_layout()
plt.show()

# Графік залежності для третього запиту
plt.figure(figsize=(8, 6))
colors_3 = [row[0] for row in result_query_3]
car_count_3 = [row[1] for row in result_query_3]
plt.plot(colors_3, car_count_3, marker='o', linestyle='-', color='green')
plt.xlabel('Кольори')
plt.ylabel('Кількість проданих авто')
plt.title('Кількість проданих авто від кольору')
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()
plt.show()