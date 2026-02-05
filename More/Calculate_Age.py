#  Calculate Age Advanced Version and Training 

userAge = input("Please Write Your Age").strip()

unitTime = input("Please Choose Time Unit: Months, Weeks, Days ").strip().lower()

months = int(userAge) * 12
weeks = months * 4
days = int(userAge) * 365


if unitTime == 'months' or unitTime == 'm':

  print(f"You Lived For {months:,} Months.")

elif unitTime == 'weeks' or unitTime == 'w':

  print(f"You Lived For {weeks:,} Weeks.")

elif unitTime == 'days' or unitTime == 'd':

  print(f"You Lived For {days:,} Days.")