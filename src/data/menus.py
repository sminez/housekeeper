'''
Lila's menus, ripped and re-formatted from the PDF provided by the school
'''
from datetime import date

autumn_2018_weeks = {
    date(2018, 9, 3): 1, date(2019, 9, 24): 1,
    date(2018, 10, 15): 1, date(2019, 11, 12): 1,
    date(2018, 12, 3): 1, date(2019, 9, 10): 2,
    date(2018, 10, 1): 2, date(2019, 10, 22): 2,
    date(2018, 11, 19): 2, date(2019, 12, 10): 2,
    date(2018, 9, 17): 3, date(2019, 10, 8): 3,
    date(2018, 11, 5): 3, date(2019, 11, 26): 3,
    date(2018, 12, 17): 3,
}

spring_2019_weeks = {
    date(2019, 1, 7): 1, date(2019, 1, 28): 1,
    date(2019, 1, 28): 1, date(2019, 2, 25): 1,
    date(2019, 3, 18): 1, date(2019, 1, 14): 2,
    date(2019, 2, 4): 2, date(2019, 4, 4): 2,
    date(2019, 3, 25): 2, date(2019, 1, 21): 3,
    date(2019, 2, 11): 3, date(2019, 3, 11): 3,
    date(2019, 4, 1): 3
}

autumn_2018_menus = {
    1: {
        'main': [
            'Sausage in a Hot Dog Bun',
            'Chicken Stir Fry with Noodles',
            'Roast Gammon and Pineapple, with Roast Potatoes and Gravy',
            'Chicken Tikka with Rice',
            'Salmon Fishcake, or Fishfingers with Chips'
        ],
        'vegitarian': [
            'Quorn Sausage in a Hot Dog Bun',
            'Macaroni Cheese with Garlic Slice',
            'Quorn Roast, with Roast Potatoes and Gravy',
            'Margarita Pizza, with Baby New Potatoes',
            'Mexican Style Vegetable Wrap with Chips'
        ],
        'sides': [
            'Jacket Wedges, Sweetcorn, and Green Beans',
            'Garden Peas and Cauliflower',
            'Carrot and Swede ',
            'Sweet corn with Peppers, and Broccoli Florets',
            'Baked Beans or Garden Peas'
        ],
        'pudding': [
            'Chocolate Cookie',
            'Carrot and Courgette Cake with Custard',
            'Mixed Fruit Crumble with Ice Cream',
            'Apple and Berry Cobbler with Custard',
            'Orange Tray bake'
        ]
    },
    2: {
        'main': [
            'Beef Burger in a Bun, with potatoe Wedges',
            'Chicken Neapolitan Pasta Bake',
            'Roast Turkey and Stuffing with Roast Potatoes and Gravy',
            'Spaghetti Bolognese',
            'Fish and Chips '
        ],
        'vegitarian': [
            'Vegetarian Mince Lasagne with potatoe Wedges',
            'Sticky barbecue Quorn with Rice',
            'Mixed Vegetable Loaf with Roast Potatoes and Gravy',
            'Vegetable and Lentil Curry with Rice',
            'Cheese and Tomato Quiche with Chips'
        ],
        'sides': [
            'Green Beans and Sweet corn',
            'Peas and Cauliflower',
            'Broccoli and Carrots',
            'Mixed Vegetables',
            'Baked Beans or Garden Peas'
        ],
        'pudding': [
            'Pineapple Loaf',
            'Eves Pudding with Custard',
            'Rice Pudding with Berries',
            'Oaty Peach Crumble with Custard',
            'Chocolate Rock Cake'
        ]
    },
    3: {
        'main': [
            'Ham Pizza, with Baby New Potatoes',
            'Minced Beef Pie with Mash ',
            'Roast Chicken and Stuffing, with Roast Potatoes and Gravy',
            'barbecue Chicken with Cajun Wedges',
            'Fish and Chips'
        ],
        'vegitarian': [
            'Cheese and Tomato Pizza, with Baby New Potatoes',
            'Shepherdess Pie',
            'Vegetable Pastry Parcel with Roast Potatoes and Gravy',
            'Five Bean Chilli with Rice',
            'Red Pepper Frittata with Vegetable Cous cous'
        ],
        'sides': [
            'Garden Peas and Coleslaw',
            'Green Beans and Sweetcorn',
            'Cabbage, Carrot and Swede',
            'Broccoli and Sweetcorn',
            'Baked Beans or Garden Peas'
        ],
        'pudding': [
            'Mandarin Upside Down Cake',
            'Rice Pudding with Mixed Berries',
            'Cheese, Apple and Biscuits',
            'Chocolate Sponge with Custard',
            'Lemon Drizzle Tray bake'
        ]
    }
}


spring_2019_menus = {
    1: {
        'main': [
            'Beef Burgers in a Bun with New Potatoes',
            'Chicken and Tomato Pasta',
            'Roast Gammon With Roast Potatoes and Gravy',
            'Chicken Curry with Boiled Rice',
            'Breaded Fish with  Chips and Tomato Sauce',
        ],
        'vegitarian': [
            'Quorn Burger in a Bun with New Potatoes',
            'Creamy Broccoli Pasta Bake',
            'Cheese and Pepper Whirl with Roast Potatoes',
            'Soya Mince and Vegetable Stir Fry with Noodles',
            'Veggie Sausage with Chips',
        ],
        'sides': ['vegetables', 'vegetables', 'vegetables', 'vegetables', 'vegetables'],
        'pudding': [
            'Oaty Cookie',
            'Pear Crumble and Custard',
            'Rolled Apple & Strawberry Pie with Custard',
            'Rice Pudding',
            'Lemon Drizzle Traybke',
        ]
    },
    2: {
        'main': [
            'Hot Dog with Tomato Sauce and potatoe Wedges',
            'Chicken and Sweetcorn Puff Pastry Pie with New Potatoes and Gravy',
            'Roast Turkey with Roast Potatoes & Gravy',
            'Spaghetti Bolognaise ',
            'Fish and Chips and Tomato Sauce',
        ],
        'vegitarian': [
            'Veggie Hot Dog with Tomato Sauce and potatoe Wedges',
            'Macaroni Cheese',
            'Quorn Roast With Roast Potatoes and Gravy ',
            'Lentil and Vegetable Curry with Rice',
            'Spinach & Tomato Quiche with Potatoes',
        ],
        'sides': ['vegetables', 'vegetables', 'vegetables', 'vegetables', 'vegetables'],
        'pudding': [
            'Chocolate Shortbread',
            'Banana Sponge and Custard',
            'Apple, Cheese and Biscuits',
            'Fruit Crumble and Custard',
            'Orange Traybake',
        ]
    },
    3: {
        'main': [
            'Ham pizza with potatoe wedges',
            'Beef lasagne',
            'Roast Chicken and Stuffing with Roast Potatoes and Gravy',
            'Beef Tortillas and Rice',
            'Fish Fingers with Chips and Tomato Sauce',
        ],
        'vegitarian': [
            'Cheese pizza with potatoe wedges',
            'Vegetable Lasagne',
            'Vegetable Pastry Puff With Roast Potatoes and Gravy',
            'Quorn Chilli with Rice',
            'Cheese Tomato & Spinach Frittata with Chips',
        ],
        'sides': ['vegetables', 'vegetables', 'vegetables', 'vegetables', 'vegetables'],
        'pudding': [
            'Chocolate and Mandarin brownie',
            'Lemon and Mixed Berry Cake',
            'Mandarins and Ice Cream',
            'Oaty Peach Crumble and Custard',
            'Pear & Ginger Traybake',
        ]
    }
}
