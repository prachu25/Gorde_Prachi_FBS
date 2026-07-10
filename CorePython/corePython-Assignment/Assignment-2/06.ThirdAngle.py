# Write a Program to input two angles from user and find third angle of the triangle.

angle1 = float(input('Enter First Angle: '))
angle2 = float(input('Enter Second Angle: '))

sum_2angle = angle1 + angle2

# Third Angle = 180 - (First Angle + Second Angle)

angle3 = 180 - sum_2angle

print('Third Angle: ', angle3)