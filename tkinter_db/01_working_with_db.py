import sqlite3

conn = sqlite3.connect('customer.db')

c = conn.cursor()

# c.execute("""CREATE TABLE customers (
#     first_name text,
#     last_name text,
#     email text
#     )
# """)

# customers_list = [
#     ('Clark', 'Kent', 'clark@gmail.com'),
#     ('Don', 'Kline', 'don@gmail.com'),
#     ('Some', 'One', 'someone@gmail.com'),
# ]
#
# c.executemany("INSERT INTO customers VALUES (?,?,?)", customers_list)

c.execute("SELECT * FROM customers")

# print(c.fetchone())
# print(c.fetchmany(3))
items = c.fetchall()

for i in items:
    print(i[2])

print("Executed...")

# commit command
conn.commit()

# closing connection
conn.close()
