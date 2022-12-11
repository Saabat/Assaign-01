mobile_data = {
    'status': True,
    'data': [
        {'name': 'Xiaomi Note 5', 'price': '300 USD', 'made': 'China'},
        {'name': 'Samsung Note 6', 'price': '200 USD', 'made': 'USA'},
        {'name': 'Iphone 5', 'price': '180.5 USD', 'made': 'Japan'},
        {'name': 'Pixel 5', 'price': '89.60 USD', 'made': 'Rusia'},
        {'name': 'Techno 5', 'price': '110 USD', 'made': 'Uk'},
        {'name': 'Huawei 5', 'price': '350 USD', 'made': 'Malaysia'},
    ],
    'exchnage_rate': 103.25
}

#  Your Code Starts from here

i = 0
while i < len(mobile_data['data']):
    name = mobile_data.get('data')[i].get('name')
    price = mobile_data.get('data')[i].get('price')
    price_split = price.split()
    price_float = float(price_split[0])
    exchange_rate = mobile_data.get('exchnage_rate')
    made = mobile_data.get('data')[i].get('made')
    sentence = f"{name} is made in {made}. The price is {price} which is equal to {exchange_rate * price_float} BDT "
    i = i + 1
    print(sentence)