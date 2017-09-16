motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

motorcycles[0] = 'ducati'
print(motorcycles)

motorcycles.append('ducati')
print(motorcycles)

motorcycles.insert(0, 'ducati')
print(motorcycles)

del motorcycles[0]
print(motorcycles)

popped_motorcycle = motorcycles.pop()
print(motorcycles)
print(popped_motorcycle)

too_expensive = 'yamaha'
motorcycles.remove(too_expensive)
print(motorcycles)
print('\nA ' + too_expensive.title() + " is too expensive for me.")

supper_person = ['father', 'mather', 'sister']
print(supper_person)

print(supper_person[0] + ' is busy.')
supper_person[0] = 'uncle'
print(supper_person)

supper_person.insert(0, 'nephew')

supper_person.insert(2, 'cousin')

supper_person.append('grandfather')
print(supper_person)

can_not_invite = supper_person.pop()
print('sorry for '+ can_not_invite)
print(supper_person)

can_not_invite = supper_person.pop()
print('sorry for '+ can_not_invite)
print(supper_person)

can_not_invite = supper_person.pop()
print('sorry for '+ can_not_invite)
print(supper_person)

can_not_invite = supper_person.pop()
print('sorry for '+ can_not_invite)
print(supper_person)

del supper_person[0]

del supper_person[0]

print(supper_person)



