from address import Address
from Mailing import Mailing

to_address = Address("693506", "Москва", "Ленина", "593", "25")

from_address = Address("596364", "Ижевск", "Пушкинская", "125", "15")

shipment = Mailing (to_address = to_address,
from_address = from_address,
cost = 550,
track = "RA987654321RU")

print(
    f"Отправление {shipment.track} из {shipment.from_address.index}, {shipment.from_address.city}, {shipment.from_address.street}, {shipment.from_address.house} - {shipment.from_address.apartment} "
    f"в {shipment.to_address.index}, {shipment.to_address.city}, {shipment.to_address.street}, {shipment.to_address.house} - {shipment.to_address.apartment}. "
    f"Стоимость {shipment.cost} рублей."
)