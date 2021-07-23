# Project 1: Block letters
print('DDDDDDD                 AAAAAAA             DDDDDDD        ??????')
print('D      D               A       A            D      D             ?')
print('D       D             A         A           D       D            ?')
print('D        D           A           A          D        D         ?')
print('D        D          AAAAAAAAAAAAAAA         D        D       ?')
print('D       D          A               A        D       D       ? ')
print('D      D          A                 A       D      D       ?')
print('DDDDDDD          A                   A      DDDDDDD        .')

# Project 2: Receipts for lovely loveseats
lovely_loveseat_description = 'Lovely Loveseat. Tufted polyester blend on wood. 32 inches high x 40 inches wide x 30 inches deep. Red or white.'
lovely_loveseat_price = 254.00

stylish_settee_description = 'Stylish Settee. Faux leather on birch. 29.50 inches high x 54.75 inches wide x 28 inches deep. Black.'
stylish_settee_price = 180.50

luxurious_lamp_description = 'Luxurious Lamp. Glass and iron. 36 inches tall. Brown with cream shade.'
luxurious_lamp_price = 52.15

sales_tax = .088  # 8.8%

customer_one_total = 0 # first customer
customer_one_itemization = ''
customer_one_total += lovely_loveseat_price
customer_one_itemization += lovely_loveseat_description
customer_one_total += luxurious_lamp_price
customer_one_itemization += luxurious_lamp_description

customer_one_tax = customer_one_total ** sales_tax
customer_one_total += customer_one_tax
print('Customer One Items:')
print(customer_one_itemization)
print('Customer One Total:')
print(customer_one_total)

# Project 3: Sal's shipping
weight = 41.5

#ground shipping
if weight <= 2:
    cost_ground = weight * 1.50 + 20.00
if weight <= 6:
    cost_ground = weight * 3.00 + 20.00
if weight <= 10:
    cost_ground = weight * 4.00 + 20.00
else:
    cost_ground = weight * 4.75 + 20.00
print(cost_ground)

premium_ground_shipping = 125.00
print(premium_ground_shipping)

#drone shipping
if weight <= 2:
    cost_drone = weight * 4.50 
if weight <= 6:
    cost_drone = weight * 9.00
if weight <= 10:
    cost_drone = weight * 12.00
else:
    cost_drone = weight * 14.25
print(cost_drone)

# Project 4: Gradebook
last_semester_gradebook = [["politics", 80], ["latin", 96], ["dance", 97], ["architecture", 65]]
subjects = ['physics', 'calculus', 'poetry', 'history']
grades = [98, 97, 85, 88]

gradebook = [['physics', 98], ['calculus', 97], ['poetry', 85], ['history', 88]]
print(gradebook)

gradebook.append(['computer science', 100])
print(gradebook)
gradebook.append(['visual arts', 93])
print(gradebook)

gradebook[-1][-1] = 98
print(gradebook)

gradebook[2].remove(85)
print(gradebook)
gradebook[2].append('Pass')
print(gradebook)

full_gradebook = last_semester_gradebook + gradebook
print(full_gradebook)

# Project 5: Len's slice

# checkpoint 1
toppings = ['pepperoni', 'pineapple', 'cheese', 'sausage', 'olives', 'anchovies', 'mushrooms']
# print(toppings)

# checkpoint 2
prices = [2, 6, 1, 3, 2, 7, 2]
# print(prices)

#checkpoint 3
num_two_dollar_slices = prices.count(2)
# print(num_two_dollar_slices)

#checkpoint 4
num_pizzas = len(toppings)
# print(num_pizzas)

#checkpoint 5
pizza_sent = 'We sell ' + str(num_pizzas)
pizza_sent += ' different kinds of pizza.'
# print(pizza_sent)

#checkpoint 6
pizza_and_prices = [[2, 'pepperoni'], [6, 'pineapple'], [1, 'cheese'], [3, 'sausage'], [2, 'olives'], [7, 'anchovies'], [2, 'mushrooms']]
# print(pizza_and_prices)

#checkpoint 7
pizza_and_prices.sort()
# print(pizza_and_prices)

#checkpoint 8
cheapest_pizza = pizza_and_prices[0][1]
# print(cheapest_pizza)

#checkpoint 9
priciest_pizza = pizza_and_prices[-1]
# print(priciest_pizza)

#checkpoint 10
pizza_and_prices.pop()
print([pizza_and_prices])


#checkpoint 11
pizza_and_prices.insert(4, [2.5, 'peppers'])
print(pizza_and_prices)

#checkpoint 12
three_cheapest = pizza_and_prices[:3]
print(three_cheapest)
