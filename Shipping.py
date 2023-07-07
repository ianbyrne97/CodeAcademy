weight = 41.5

# Ground Shipping
if weight <= 2:
  price_ground = weight * 1.50 + 20.00
elif weight > 2 and weight <= 6:
  price_ground = weight * 3.00 + 20.00
elif weight > 6 and weight <= 10:
  price_ground = weight * 4.00 + 20.00
elif weight > 10:
  price_ground = weight * 4.75 + 20.00

print("Ground Shipping: $", price_ground)

# Premium Ground Shipping
price_premium_ground = 125.00

print("Premium Ground Shipping: $", price_premium_ground)

# Drone Shipping
if weight <= 2:
  price_drone = weight * 4.50
elif weight > 2 and weight <= 6:
  price_drone = weight * 9.00
elif weight > 6 and weight <= 10:
  price_drone = weight * 12.00
elif weight > 10:
  price_drone = weight * 14.25

print("Drone Shipping: $", price_drone)
