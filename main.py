import psycopg2

# Параметри підключення до бази даних PostgreSQL
dbname = 'lab_3'
user = 'Ignatiev'
password = '5432'
host = 'localhost'
port = '5432'

total_res=[]
# Підключення до бази даних
try:
    conn = psycopg2.connect(dbname=dbname, user=user, password=password, host=host, port=port)
    cursor = conn.cursor()

    # SQL-запити
    queries = [
        """
        SELECT m.name AS manufacturer_name, MAX(c.price) AS max_car_price
        FROM manufacturer m
        JOIN car c ON m.manufacturer_id = c.manufacturer_id
        GROUP BY m.name;
        """,
        """
        SELECT m.name AS manufacturer_name, SUM(c.price) AS total_income
        FROM manufacturer m
        JOIN car c ON m.manufacturer_id = c.manufacturer_id
        GROUP BY m.name;
        """,
        """
        SELECT color, COUNT(*) AS car_count
        FROM car
        GROUP BY color;
        """
    ]

    # Виконання запитів та виведення результатів у консоль
    for i, query in enumerate(queries, start=1):
        cursor.execute(query)
        result = cursor.fetchall()
        total_res.append(result)
        print(f"Результат запиту {i}:")
        for row in result:
            print(row)

    # Закриваємо з'єднання
    cursor.close()
    conn.close()

except psycopg2.Error as e:
    print("Помилка підключення до бази даних:", e)


