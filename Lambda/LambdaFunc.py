# # 9.2
# x = lambda value : value * value
# print(x(3))
#
#
# # 9.3
# krokovaci_funkce_po_dvou = lambda x : x + 2
# nasobici_funkce = lambda a, b : a * b
# linearni_funkce = lambda a, b, x : a * x + b
# konstantni_funkce_peti = lambda : 5
#
#
# print(krokovaci_funkce_po_dvou(1))
# print(nasobici_funkce(2, 4))
# print(linearni_funkce(1, 2, 3))
# print(konstantni_funkce_peti())
#
#
#
# # 9.4
# vysledky = [
#     ("Karel", 31),
#     ("Petr", 10),
#     ("Honza", 52),
#     ("Eva", 61),
#     ("Katka", 0),
# ]
#
# sorted_list = sorted(vysledky, key=lambda e: e[1])
# print(sorted_list)


# 9.5
zbozi = [
    {
        "name" : "IPHONE 14",
        "price" : 22169.0,
        "cathegory" : (12, "Mobilní telefony")
    },
    {
        "name" : "Fujifilm XT30",
        "price" : 22269.0,
        "cathegory" : (2, "Fotoaparáty")
    },
    {
        "name" : "Niceboy HIVE Pins Black",
        "price" : 999.0,
        "cathegory" : (4, "Sluchátka")
    }
]


def asceding_price(collection):
    return collection["price"]


def desceding_name(collection):
    return collection["name"]

def asceding_category(collection):
    return collection["cathegory"][0]


sorted_asc_price = sorted(zbozi, key = asceding_price)
print(sorted_asc_price)
sorted_desc_name = sorted(zbozi, key = desceding_name, reverse=True)
print(sorted_desc_name)
sorted_asc_category = sorted(zbozi, key = asceding_category)
print(sorted_asc_category)