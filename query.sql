--Запит 1 вивести назву фірми та її ціну найдорожчого автомобіля
SELECT m.name AS manufacturer_name, MAX(c.price) AS max_car_price
FROM manufacturer m
JOIN car c ON m.manufacturer_id = c.manufacturer_id
GROUP BY m.name;

-- Запит 2 загальна кількість грошей, отриманих кожним виробником
SELECT m.name AS manufacturer_name, SUM(c.price) AS total_income
FROM manufacturer m
JOIN car c ON m.manufacturer_id = c.manufacturer_id
GROUP BY m.name;

-- Запит 3 залежність кількості проданих автомобілей від кольору
SELECT color, COUNT(*) AS car_count
FROM car
GROUP BY color;

