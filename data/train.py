TRAIN_ROUTES = [
    ('Minstowe', 'Cowstone', 3),
    ('Oldcastle', 'New North', 5),
    ('Oldcastle', 'Freeham', 2),
    ('Cowstone', 'Freeham', 5),
    ('Cowstone', 'New North', 4),
    ('Cowstone', 'Bingborough', 6),
    ('Cowstone', 'Donningpool', 7),
    ('Cowstone', 'Highbrook', 5),
    ('New North', 'Bingborough', 3),
    ('New North', 'Donningpool', 6),
    ('New North', 'Wington', 4),
    ('New North', 'Highbrook', 2),
    ('Freeham', 'Cowstone', 2),
    ('Freeham', 'Donningpool', 3),
    ('Freeham', 'Wington', 5),
    ('Bingborough', 'Donningpool', 2),
    ('Bingborough', 'Highbrook', 1),
    ('Donningpool', 'Wington', 4),
    ('Donningpool', 'Highbrook', 5),
    ('Donningpool', 'Old Mere', 2),
]


TRAIN_ROUTES_GRAPH = {
    'Minstowe': {'Cowstone': 3},
    'Cowstone': {'Minstowe': 3, 'Freeham': 2, 'New North': 4, 'Bingborough': 6, 'Donningpool': 7, 'Highbrook': 5},
    'Oldcastle': {'New North': 5, 'Freeham': 2},
    'New North': {'Oldcastle': 5, 'Cowstone': 4, 'Bingborough': 3, 'Donningpool': 6, 'Wington': 4, 'Highbrook': 2},
    'Freeham': {'Oldcastle': 2, 'Cowstone': 2, 'Donningpool': 3, 'Wington': 5},
    'Bingborough': {'Cowstone': 6, 'New North': 3, 'Donningpool': 2, 'Highbrook': 1},
    'Donningpool': {'Cowstone': 7, 'New North': 6, 'Freeham': 3, 'Bingborough': 2, 'Wington': 4, 'Highbrook': 5, 'Old Mere': 2},
    'Highbrook': {'Cowstone': 5, 'New North': 2, 'Bingborough': 1, 'Donningpool': 5},
    'Wington': {'New North': 4, 'Freeham': 5, 'Donningpool': 4},
    'Old Mere': {'Donningpool': 2}
}


TRAINT_COST_HOUR: int = 15


TRAINT_CLASESS = {
    'economy': {'capacity': 25, 'cost': 20},
    'business': {'capacity': 30, 'cost': 30},
    'exclusive': {'capacity': 35, 'cost': 40}
}
