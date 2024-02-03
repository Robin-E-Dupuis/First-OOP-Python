from user import User
userN = input("Enter your username:")
userP = input("Enter your Password:")
userB = int(input("Enter your birth date as is (MDY = 100104):"))
user1 = User(userN, userP, userB)

print("hello "+userN + " your password is "+userP + " and your birthday is " + str(userB))
