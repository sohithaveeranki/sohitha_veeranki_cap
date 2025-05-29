inventory = [
    # name,       category,   unit_price, units_sold, units_left
    ["Strawberry", "Fruit",      3.50,        40,          10],
    ["Broccoli",   "Vegetable",  2.20,        25,           8],
    ["Cheddar",    "Dairy",      5.00,        18,           4],
    ["Baguette",   "Bakery",     2.80,        35,           2],
    ["Blueberry",  "Fruit",      4.00,        22,           6],
    ["Spinach",    "Vegetable",  1.80,        30,          12],
    ["Yogurt",     "Dairy",      1.20,        50,          15],
    ["Croissant",  "Bakery",     3.00,        28,           3],
]

total_revenue = 0

for name, category, unit_price, units_sold, units_left in inventory:
    total_revenue += unit_price * units_sold

print("Total Revenue: ", total_revenue)

for item in inventory:
    name = item[0]
    units_left = item[4]

    if units_left < 5:
        print(name, "is low on stock with", units_left, "units left")


category_revenue = {}

for item in inventory:
    category = item[1]
    unit_price = item[2]
    units_sold = item[3]
    revenue = unit_price * units_sold

    if category in category_revenue:
        category_revenue[category] += revenue
    else:
        category_revenue[category] = revenue

for cat in category_revenue:
    print(cat, "revenue: $", category_revenue[cat])



