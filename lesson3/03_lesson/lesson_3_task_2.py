from smartphone import Smartphone
catalog = [
    Smartphone("Apple", "iPhone 16 Pro Max", "+7 (999) 111-22-33"),
    Smartphone("Samsung", "Galaxy S26 Ultra", "+7 (999) 444-55-66"),
    Smartphone("Xiaomi", "15 Pro", "+7 (999) 777-88-99"),
    Smartphone("Google", "Pixel 10 Pro", "+7 (900) 123-45-67"),
    Smartphone("OnePlus", "13", "+7 (950) 987-65-43")
    ]


for Smartphone in catalog:
    print(f"{Smartphone.brand} - {Smartphone.model} . {Smartphone.nomer}")