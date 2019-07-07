from collections import defaultdict

coworkers = [('Rolf', 'MIT'), ('Jen', 'Oxford'), ('Rolf', 'Cambridge'), ('Charlie', 'Manchester')]

alma_maters = {}

for coworker, place in coworkers:
    if coworker not in alma_maters:
        alma_maters[coworker] = []
    alma_maters[coworker].append(place)

alma_maters = defaultdict(list)

for coworker, place in coworkers:
    alma_maters[coworker].append(place)

# alma_maters.default_factory = None

print(alma_maters['Rolf'])
print(alma_maters['Anne'])


my_company = 'Teclado'

coworkers = ['Jen', 'Li', 'Charlie', 'Rhys']
other_coworkers =[('Rolf', 'Apple Inc'), ('Anna', 'Google')]

coworker_companies = defaultdict(lambda: my_company)

for person, company in other_coworkers:
    coworker_companies[person] = company

print(coworker_companies[coworkers[0]])
print(coworker_companies['Rolf'])