select * from car
select * from manufacturer
select * from location
--ЗАПИТ 1 вивести місто виробника найдорожчого автомобіля
SELECT loc.region_name AS city_of_manufacturer_of_most_expensive_car
FROM location loc
JOIN manufacturer m ON loc.location_id = m.location_id
JOIN car c ON m.manufacturer_id = c.manufacturer_id
WHERE c.price = (
    SELECT MAX(price) FROM car
)
--ЗАПИТ 2 вивести колір найдешевшого автомобіля
SELECT color AS color_of_cheapest_car
FROM car
WHERE price = (
    SELECT MIN(price) FROM car
)

--ЗАПИТ 3 вивести назву виробника, модель авто та ціну у порядку зростання ціни
SELECT m.name AS manufacturer_name, c.model AS car_model, c.price AS car_price
FROM manufacturer m
JOIN car c ON m.manufacturer_id = c.manufacturer_id
ORDER BY c.price ASC;


