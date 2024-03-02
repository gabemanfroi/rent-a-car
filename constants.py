POPULAR = 'popular'
SEDDAN = 'seddan'
PICK_UP = 'pick_up'
SUV = 'suv'

# carros populares = celta palio gol clio  90 diária
# carros seddan = prisma sienna voyage logan 100 diaria
# pick up = montana strada saveiro pampa 120 diaria 
# Suv = blazer pulse tiguan duster 150 diaria
# seg = 20 popular e sedan
# seg = 30 pick up e suv

#3 dias = desconto de 3%
#7 dias = desconto de 5%
#10 dias = desconto de 7%
base_de_dados = {
    SEDDAN: { 
        "preco": 100,
        "modelos": [ "prisma", "sienna", "voyage", "logan"], 
        "seguro": 20
    },
    PICK_UP: {
        'preco': 120,
        'modelos': ['montana', 'strada', 'saveiro', 'pampa'],
        "seguro": 30
    },
    POPULAR: {
        'preco': 90,
        'modelos': ['celta', 'palio', 'gol', 'clio'],
        'seguro': 20
    }, 
    SUV: {
        'preco': 150,
        'modelos': ['blazer', 'pulse', 'tiguan', 'duster'],
        'seguro': 30
    }
}