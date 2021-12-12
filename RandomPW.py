import random


def randomPassword(n):
    
    low = 'abcdefgihjklmnoqrstuvwxyz'
    upper = low.upper()
    nums = '0123456789'
    special = '!@#$%^&*'
    password = ''

    for i in range(n):
        eachItr = [random.choice(low), random.choice(upper), random.choice(nums), random.choice(special)]
        password += random.choice(eachItr)

    return password

if __name__ == '__main__':
    n = int(input("Length of password\n"))
    print(randomPassword(n))