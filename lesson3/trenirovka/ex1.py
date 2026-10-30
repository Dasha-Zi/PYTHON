from product import Product

my_product = Product("Телефон", 12000)

print(my_product.get_name())# Ожидаемый результат: "Laptop"
print(my_product.get_price())# Ожидаемый результат: 1200
print(my_product.get_product_info())# Ожидаемый результат: "Product: Laptop, Price: 1200"