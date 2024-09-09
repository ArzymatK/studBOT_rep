from datetime import datetime

print("Enter you date of birth:")
result = datetime.now()-datetime.strptime(input(">>>"),'%d-%m-%Y')
print(f"You are {result.days//365}! Have a productive day!")
