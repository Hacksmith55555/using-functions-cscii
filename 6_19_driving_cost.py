
# Starter Code :
def driving_cost(miles_per_gallon, dollars_per_gallon, miles_driven):
       driving_cost = (miles_driven/miles_per_gallon) * dollars_per_gallon
       return driving_cost
# Define your function here.

if __name__ == '__main__':
    # Type your code here.
    miles_per_gallon = 20.0
    dollars_per_gallon = 3.1599

    # Output gas cost for the 10 miles
    print(f"{driving_cost(miles_per_gallon, dollars_per_gallon, 10):.2f}")

    #Output gas cost for the 50 miles
    print(f"{driving_cost(miles_per_gallon, dollars_per_gallon, 50):.2f}")

    #Output gas cost for the 400 miles
    print(f"{driving_cost(miles_per_gallon, dollars_per_gallon, 400):.2f}")
    