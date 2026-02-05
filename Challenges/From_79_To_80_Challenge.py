import datetime 

requireData = datetime.datetime(2021, 6, 25)
todayDate = datetime.datetime(2025, 11, 29)

print(f"Days From {requireData} To {todayDate} Is => {(todayDate - requireData).days}")

# Message Will Be
"Days From 2021-06-25 To 2025-11-29 Is => 1618"

# [2]

dateNow = datetime.datetime.now().date()
monthNow = datetime.datetime.now().date().month

print(dateNow)
print(f'{dateNow.strftime('%b')}  {dateNow.day}, {dateNow.year}')
print(f'{dateNow.day} - {dateNow.strftime('%b')} - {dateNow.year}')
print(f'{dateNow.day} / {dateNow.strftime('%b')} / {dateNow.year}')
print(f'{dateNow.day}  {dateNow.strftime('%b')}, {dateNow.year}')
print(f'{dateNow.day} / {dateNow.strftime('%B')} / {dateNow.year}')
print(f'{dateNow.strftime('%a')}, {dateNow.month} {dateNow.strftime('%B')} {dateNow.year}')



# Today Is "2021, 8, 10"

"2021-08-10"
"Aug 10, 2021"
"10 - Aug - 2021"
"10 / Aug / 21"
"10 / August / 2021"
"Tue, 10 August 2021"