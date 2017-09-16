alien_0 = {'color': 'green', 'points':5}
print(alien_0['color'])
print(alien_0['points'])

alien_0['color'] = 'yellow'
print("The alien is now " + alien_0['color'] + ".")

alien_1 = {'x_position':0, 'y_position': 25, 'speed': 'medium'}
print("Original x-position" + str(alien_1['x_position']))

# 向右移动外星人
# 据外星人当前速度决定将其移动多远

if alien_1['speed'] == 'slow':
    x_increment = 1
elif alien_1['speed'] == 'medium':
    x_increment = 2
else:
    x_increment = 3
    
alien_1['x_position'] = alien_1['x_position'] + x_increment

print("New x-position: " + str(alien_1['x_position']))

del alien_0['points']
print(alien_0)
