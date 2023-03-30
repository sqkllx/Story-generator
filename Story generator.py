import random 
when = ['Once upon a time', 'A few days ago', 'Yesterday', 'A long time ago', 'Last night', 'On 25th Febuary']
who = [' a magician', ' a turtle', ' a monster', ' a horse',' a fish', ' a cat']
name = ['haley', 'leah', 'olivia', 'draco', 'burhan', "adam" ]
residence = ['Canada', 'England', 'Australia', 'Dubai', 'Brazil', 'Argentina']
went = ['park', 'school', 'party', 'theatre', 'gas station', 'bakery']
happend = ['read a book', ' alot of new friends', 'drank juice', 'solved a mystery', 'found a key', 'wrote a book']
print(random.choice(when) + ', ' +random.choice(who) + ' that lived in '+random.choice(residence) + ', ' +random.choice(name) + ' went to the ' +random.choice(went) + ' and ' +random.choice(happend))