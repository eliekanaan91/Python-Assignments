username = 'admin'
password = '1234'
tries_left = 3

while tries_left > 0:
    entered_username = input("Enter your username: ")
    entered_password = input("Enter your password: ")

    if entered_username==username and entered_password==password:
        print ('you are logged in')
        break
    else:
        tries_left-=1
        print("Your username or password are wrong, try again")

if tries_left==0:
    print("Your account is blocked")
else:
    n=int(input("Please enter a number: "))
    print(f"Prime numbers between 2 and {n} are:")
    
    
    for num in range(2, n + 1):
        is_prime = True
    
        for i in range(2, num):
            if num % i == 0:
                is_prime = False
                break
    
        if is_prime:
            print(num, end=" ")