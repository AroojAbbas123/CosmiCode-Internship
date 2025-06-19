#In this Task I am going to convert the given time in seconds to hours,minutes,seconds

second=int(input("Enter sseconds which you want to convert: "))
if(second<0):
    print("Time can never be negative!")
else:
    
   hours = second // 3600
   remaining_seconds = second % 3600
   minutes = remaining_seconds // 60
   seconds = remaining_seconds % 60

print(f"{hours} hours, {minutes} minutes, {seconds} seconds")
   