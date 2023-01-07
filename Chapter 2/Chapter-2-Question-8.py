# Question 8

initial_time = int(input("What is the current time (in hours)? "))
alarm_time = int(input("What is the time duration of alarm (in hours)? "))

end_time = (initial_time + alarm_time) % 24
print("The alarm goes off at " + str(end_time) + "00 hours.")