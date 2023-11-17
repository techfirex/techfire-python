age = int(input("Enter your age: "))

if age==0 or age<0:
    print("you cannot watch movie")
elif 0<age<=3:
    print("Ticket price: Free")
elif 3<age<=10:
    print("Ticket price: 150")
elif 10<age<=60:
    print("Ticket price: 250")
else:
    print("Ticket price: 200")