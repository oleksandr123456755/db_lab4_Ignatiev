CREATE TABLE location
(
  region_name varchar(30) NOT NULL,
  location_id INT NOT NULL,
  PRIMARY KEY (region_name)
);

CREATE TABLE manufacturer
(
  name varchar(30) NOT NULL,
  manufacturer_id INT NOT NULL,
  region_name varchar(30) NOT NULL,
  PRIMARY KEY (manufacturer_id),
  FOREIGN KEY (region_name) REFERENCES location(region_name)
);

CREATE TABLE car
(
  body_type varchar(30) NOT NULL,
  model varchar(30) NOT NULL,
  color varchar(30) NOT NULL,
  price INT NOT NULL,
  car_id INT NOT NULL,
  manufacturer_id INT NOT NULL,
  
  
  PRIMARY KEY (car_id),
  FOREIGN KEY (manufacturer_id) REFERENCES manufacturer(manufacturer_id)
);