CREATE TABLE dishes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    price INTEGER
);

CREATE TABLE orders (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    date TEXT
);

CREATE TABLE ordered (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    order_id INTEGER,
    dish_id INTEGER,
    FOREIGN KEY (order_id) REFERENCES orders(id),
    FOREIGN KEY (dish_id) REFERENCES dishes(id)
);

-- Вставка данных в таблицу "Блюда"
INSERT INTO dishes (name, price) VALUES
('Пицца Маргарита', 500),
('Бургер', 250),
('Суши Филадельфия', 650),
('Паста Карбонара', 450),
('Стейк', 1200);

-- Вставка данных в таблицу "Заказы"
INSERT INTO orders (date) VALUES
('2025-02-20'),
('2025-02-21'),
('2025-02-22');

-- Вставка данных в таблицу "Заказано" (связь заказов и блюд)
INSERT INTO ordered (order_id, dish_id) VALUES
(1, 1), (1, 3), (1, 5),  -- Заказ 1 (Пицца, Суши, Стейк)
(2, 2), (2, 4),          -- Заказ 2 (Бургер, Паста)
(3, 1), (3, 2), (3, 5);  -- Заказ 3 (Пицца, Бургер, Стейк)