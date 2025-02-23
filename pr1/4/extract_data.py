import sqlite3
import pandas as pd

con = sqlite3.connect("sqllite.db")

# 1
df = pd.read_sql("""SELECT ordered.id AS ordered_id, dishes.name, dishes.price 
                 FROM ordered 
                 LEFT JOIN dishes ON ordered.dish_id = dishes.id""", con, index_col="ordered_id")
# print(df.head())

# 2
df = pd.read_sql("""SELECT ordered.order_id, sum(dishes.price) AS total 
                 FROM ordered 
                 LEFT JOIN dishes ON ordered.dish_id = dishes.id
                 GROUP BY order_id""", con, index_col="order_id")
# print(df.head())

# 3
df = pd.read_sql("""SELECT name 
                 FROM dishes 
                 WHERE price < 300""", con)
# print(df.head())

# 4
df = pd.read_sql("""SELECT dishes.name, dishes.price 
                 FROM ordered 
                 LEFT JOIN dishes ON ordered.dish_id = dishes.id
                 WHERE order_id = 1""", con)
# print(df.head())

# 5
df = pd.read_sql("""SELECT * 
                 FROM dishes 
                 ORDER BY price DESC""", con, index_col='id')
# print(df.head())

# 6
def calculate_order_price(order_id: int) -> int:
    sql = f"""SELECT order_id, dishes.price AS price
                FROM ordered 
                LEFT JOIN dishes ON ordered.dish_id = dishes.id 
                WHERE order_id = {order_id}"""
    df = pd.read_sql(sql, con)

    price = df['price'].sum()
    if df.shape[0] >= 3:
        price *= 0.95

    return price

# print(calculate_order_price(1))

# 7
new_dishes = pd.DataFrame({
    "name": ["Том Ям", "Цезарь", "Ролл Калифорния"],
    "price": [700, 400, 600]
})
new_dishes.to_sql("dishes", con, if_exists='append', index=False)

new_orders = pd.DataFrame({
    "date": ["2025-02-23", "2025-02-24", "2025-02-25"]
})
new_orders.to_sql("orders", con, if_exists='append', index=False)

orders_id = pd.read_sql(f"""SELECT id FROM orders ORDER BY id DESC LIMIT {new_orders.shape[0]}""", con)
dishes_id = pd.read_sql(f"""SELECT id FROM dishes ORDER BY id DESC LIMIT {new_dishes.shape[0]}""", con)

new_ordered = pd.DataFrame({
    "order_id": orders_id['id'],
    "dish_id": dishes_id['id']
})
new_ordered.to_sql("ordered", con, if_exists='append', index=False)

con.close()