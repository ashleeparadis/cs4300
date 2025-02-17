
#Function that takes price and discounts as arguements and applies
#the discount to give the final price.
def calculate_discount(price, discount):

    #Calculate discounted price
    dis_price = price * (1 - (discount / 100))
    return dis_price

print(calculate_discount(20, 10))