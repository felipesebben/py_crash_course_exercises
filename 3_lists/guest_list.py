guests = ['beethoven','paco de lucia','guimaraes rosa']
print(f"\nDear {guests[0].title()}, would you like to come over for dinner?")

guests = ['beethoven','paco de lucia','guimaraes rosa', 'hemingway']
invited_guest = guests.pop()
print(guests)
print(f"\nDear {invited_guest.title()}, would you like to come over for dinner?")

guests = ['beethoven','paco de lucia','guimaraes rosa', 'hemingway']
cancelled_guest = 'beethoven'
alternative_guest = 'mozart'
guests.remove(cancelled_guest)
guests.insert(0, alternative_guest)
print(guests)
print(f"\nSince {cancelled_guest.title()} won't make it, I'll invite {alternative_guest.title()} instead.")

print(f"\nDear Mozart, Paco de Lucia, Guimaraes Rosa and Hemingway, I'm glad to inform you that we are getting a bigger table, so I'll invite three more guests!")
guests.insert(0, 'Lula')
guests.insert(3, 'Bolsonaro')
guests.append('Bismarck')

print(guests)
guest1 = guests[0]
guest2 =guests[1]
all_guests = guests
print(f"\nDear {guest1.title()}, you are invited to this tremendous party!")
print(f"\nDear {guest2.title()}, you are invited to this tremendous party!")
print(f"\nDear {all_guests}, sorry but I can only invite two of you as there is only room for two guests!")

guests.pop()
print(guests)
guests.pop(-1)
guests.pop(-1)
guests.pop(1)
guests.pop(1)
guest1 = guests[0]
guest2 =guests[1]
print(guests)
print(f"\nDear {guest1.title()} and {guest2.title()}, you are invited to my party!")
del guests[0]
del guests[0]
print(guests)

guests = ['beethoven','paco de lucia','guimaraes rosa', 'hemingway']
len(guests)
print(len(guests))