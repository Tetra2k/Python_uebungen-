customer_basket_cost = 34
customer_basket_weight = 44

# Write if statement here to calculate the total cost

if customer_basket_cost < 100:
   ship = customer_basket_weight *1.2
   price = customer_basket_cost + ship
   print(price)