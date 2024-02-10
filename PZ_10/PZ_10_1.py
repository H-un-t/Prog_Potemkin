 # Вариант 20.

"""
Известны марки машин, выпускаемые в данной стране и экспортируемых в N заданных стран. 
Определить какие марки машин были доставлены во все указанные страны, 
какие в некоторые из стран и какие не доставлены ни в одну страну.
"""

cars = {'Toyota', 'Honda', 'Nissan', 'Suzuki', 'Mazda', 'Infinity'}
country_1 = {'Toyota', 'Honda', 'Nissan'}
country_2 = {'Toyota', 'Honda', 'Infinity'}
country_3 = {'Toyota', 'Nissan', 'Suzuki'}
anticar = set()
for i in cars:
    if i not in (country_1 | country_2 | country_3):
        anticar.add(i)
print(f'марки машин которые доставлены во все страны: {country_1&country_2&country_3}')
print(f'марки машин которые доставлены в некоторые страны: {country_1|country_2|country_3}')
print(f"марки машин которые не были доставлены ни в одну страну: {anticar}")











"""
cars = [
    ['Toyota', 'Honda', 'Nissan'],
    ['Toyota', 'Honda'],
    ['Toyota', 'Nissan']
]

countries = 3

result = (cars, countries)
print("Марки машин, которые были доставлены во все страны:", result[0])
print("Марки машин, которые были доставлены хотя бы в одну страну:", result[1])
print("Марки машин, которые не были доставлены ни в одну страну:", result[2])
"""