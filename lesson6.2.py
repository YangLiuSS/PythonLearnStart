favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }
    
print("Sarah's favorite language is " + 
    favorite_languages['sarah'].title() +
    ".")


friend = {'first_name': 'yang',
    'last_name': 'liu',
    'age': '26',
    'city': 'xian',
    }
print("my friend name is: " + 
    friend['first_name'] + " " +
    friend['last_name'] +
    " his age is: "+
    friend['age']+
    " he live in: "+
    friend['city']+
    ".")
    
friends = ['phil', 'sarah']
for name in favorite_languages.keys():
    print(name.title())

    if name in friends:
        print(" Hi " + name.title() +
            ", I see your favorite language is " +
            favorite_languages[name].title() + "!")
if 'erin' not in favorite_languages.keys():
    print("Erin,please take our poll!")
    
accepts_person = ['edward', 'phil', 'berite']

for name in favorite_languages.keys():
    if name in accepts_person:
        print("Thank you " + name.title() +
         "your favorite_languages is " + 
         favorite_languages[name].title() + 
         "!")
    else:
        print("hi," + name.title() +
        " we are invite you to accept the investigation")
