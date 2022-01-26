alien_0 = {'color': 'green', 'points': 5}
print(alien_0)

#adding new key-value pairs:
alien_0['x_position'] = 0
alien_0['y_position'] = 25

print(alien_0)

#starting with an empty dictionary:
alien_0 = {}

alien_0['color'] = 'green'
alien_0['points'] = 5

print(alien_0)

#modifying values in a dictionary:

alien_0 = {'color': 'green'}
print(f"The alien is {alien_0['color']}.")

alien_0['color'] = 'yellow'
print(f"The alien is now {alien_0['color']}.")

#tracking the position of an alien:
alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
print(f"Original position: {alien_0['x_position']}")

#Move the alien to the right.
#Determine how far to move the alien based on its current speed.
if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    #This must be a fast alien.
    x_increment = 3

#The new position is the old position plus the increment
alien_0['x_position'] = alien_0['x_position'] + x_increment

print(f"New position: {alien_0['x_position']}")
 
 #removing key-value pairs:
alien_0 = {'color': 'green', 'points': 5}
print(alien_0)

del alien_0['points']
print(alien_0)

#nesting
alien_0 = {'color': 'green', 'points': '5'}
alien_1 = {'color': 'yellow', 'points': '10'}
alien_2 = {'color': 'red', 'points': 15}

aliens = [alien_0, alien_1, alien_2]

for alien in aliens:
    print(alien)

#Make an empty list for storing aliens.
aliens = []

#Make 30 green aliens.
for alien_number in range(30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)

for alien in aliens[:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10
    elif alien['color'] == 'yellow':
        alien['color'] = 'red'
        alien['speed'] = 'fast'
        alien['points'] = 15
#Show the first five aliens.
for alien in aliens[:5]:
    print(alien)
print("...")

#Show how many aliens have been created.
print(f"Total numbers of aliens: {len(aliens)}")
