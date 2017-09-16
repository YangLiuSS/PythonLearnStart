user_0 = {
    'username': 'efermi',
    'first': 'enrico',
    'last': 'fermi',
    'last1': 'fermi1',
    'last2': 'fermi1',
    'last3': 'fermi1',
    'last4': 'fermi1',
    'last5': 'fermi1',
    'last6': 'fermi1',
    }
    
for key, value in user_0.items():
    print("\nKey: " + key)
    print("Value: " + value)

for key in user_0.keys():
    print(key)

#默认会遍历所有的key
for key in user_0:
    print(key)

#~ d = {'a': 1,
    #~ 'b': 0,
    #~ 'c': 1,
    #~ 'd': 0
    #~ }
#~ for k in d.keys():
    #~ if d[k] == 0:
        #~ del(d[k])
#~ print(d)

for user in set(user_0.values()):
    print(user.title())


rivers = {'changjiang': 'china',
    'nile': 'egypt',
    'Mississippi': 'america',
    }
for river,country in rivers.items():
    print("The " + river.title() + " runs through " + country.title())

for river in rivers.keys():
    print("The river\'s name is " + river.title())

for river in rivers:
    print("The river\'s name is " + river.title())
    
for river in rivers.values():
    print("The country\'s name is " + river.title())

