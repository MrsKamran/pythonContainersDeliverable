students = ["Yiren","Yufei","Nick","Seb"]

print(f'Second students\' name is {students[1]}')
print(f'Last students\' name is {students[-1]}')

foods = ("cookies","apples","PB&J","grapes")
for item in range(len(foods)):
  print(f'{foods[item]} goes {item} in a good food')

for item in range(len(foods)-2,len(foods)):
  print(f'{foods[item]} has index {item} in foods tuple')

home_town = {
  "city": "Lahore", 
  "state": "Pakistan",
  "population": 220892340
  }

print(f'I was born in {home_town["city"]}, {home_town["state"]} - of {home_town["population"]} population')

# for k in home_town:
#   print(f'{k} = {home_town[k]}')

for k,v in home_town.items():
  print(f'{k} = {v}')

cohort = []
for s in range(len(students)):
  new_c ={
    'student' : students[s],
    'fav_food' : foods[s]
  }
  cohort.append(new_c)
print(cohort)

awesome_students = [student+" is awesome!" for student in students]

for s in awesome_students:
  print(s)

for f in foods:
  if 'a' in f:
    print(f'{f}')
