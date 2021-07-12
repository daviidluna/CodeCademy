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



