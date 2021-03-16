living_miles_apart = 4
drives_velocity = 25
time_taken = ((living_miles_apart/drives_velocity) * 60)
# 2 minutes in each stop
time_spends = 20
total_time = time_taken + time_spends
print(f"Total time taken by bus is {total_time} ")
jog_one = ((1/7) * 60)
jog_two = ((2/15) * 60)
jog_three = ((1/7) * 60)
total_walk_time = jog_one + jog_two + jog_three
print(f"Time taken by running is {total_walk_time} ")

if (total_time > total_walk_time):
    print("Taking bus is slower than running !!")
else:
    print("Taking bus is quicker than running !!")