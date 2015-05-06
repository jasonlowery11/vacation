# Simple trip-planner app that gives estimated cost based on number of days/nights
# and destination based on 4 example destinations. Assignment comes from Codecademy
# lesson 8, "Taking a vacation." As of now, the functions take constant values.



# define hotel cost
def hotel_cost(nights):
    return 140 * nights

# define plane ride cost based on destination
def plane_ride_cost(city):
    if city == "Charlotte":
        return 183
    elif city == "Tampa":
        return 220
    elif city == "Pittsburgh":
        return 222
    elif city == "Los Angeles":
        return 475


# define rental car cost        
def rental_car_cost(days):
    cost = days * 40
    if days >= 7:
        return cost - 50
    elif days >= 3:
        return cost - 20
    else:
        return cost

# total all costs associated with vacation including spending money        
def trip_cost(city, days, spending_money):
    return hotel_cost(days) + plane_ride_cost(city) + rental_car_cost(days) + spending_money

# Print totals
print("Hotel Total: $" + str(hotel_cost(5)))
print("Air Travel: $" + str(plane_ride_cost("Los Angeles")))
print("Rental Car: $" + str(rental_car_cost(5)))
print("Estimated Spending Money: $" + str(600))
print(trip_cost("Los Angeles", 5, 600))
