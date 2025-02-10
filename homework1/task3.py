#Check if number is postive or negative with if statement

def check_pos_neg(number):
    positive = "Number is positive"
    negative = "Number is negative"
    if(number > 0):                    #Check if number positive
        print("Number is positive")
        return positive
    else:
        print("Number is negative")   #Check if number is negative
        return negative

#Print the first 10 prime numbers using a for loop
def get_first_10_primes():
    num = 2
    primeNums = []

    while(len(primeNums) < 10):
        is_prime = True

        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                is_prime = False
            
        if is_prime:
            primeNums.append(num)
        num += 1
    print(primeNums)
    return primeNums

#Find the sum of all numbers from 1 to 100 using a while loop
def sum_numbers():
    count = 0
    sum = 0

    while(count <= 100):
        sum += count
        count += 1
    print(sum)

    return sum

check_pos_neg(3)
get_first_10_primes()
sum_numbers()