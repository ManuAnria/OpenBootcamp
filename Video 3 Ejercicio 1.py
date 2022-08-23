import pprint

contacto1 = {'nombre': 'Ernesto',
             'apellido': 'Garcia',
             'edad': '25',
             'email': 'egarcia@gmail.com',
             'telefono': '12345678',
             'casado': 'False',
             'con_hijos': 'False',
             'amigos': ['Juan', 'Pedro', 'Maria'],
             'peliculas_vistas': {1: 'El padrino', 2: 'Harry Potter', 3: 'Avengers'}}
pprint.pprint(contacto1, sort_dicts=False)
