# Convert the time entered in hh,min and sec into seconds.

# step-1: Take a input hour, min, sec
hour = int(input('Enter a Hour: '))
minute = int(input('Enter a Minutes: '))
second = int(input('Enter a Second: '))

# step-2: convert hour into second
hour_in_second = hour * 3600

# step-3: convert minutes into second
minute_in_second = minute * 60

# step-4: total second
total_second = hour_in_second + minute_in_second + second

print('Total Second is ', total_second)