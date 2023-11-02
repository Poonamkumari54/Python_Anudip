# Input the distance from the user
distance = float(input("Enter the distance in kilometers: "))

# Calculate the fare based on the distance
if distance >= 1 and distance <= 50:
    fare = distance * 8
elif distance >= 51 and distance <= 100:
    fare = distance * 10
else:
    fare = distance * 12

# Print the calculated fare
print("The fare for traveling", distance, "kilometers is", fare, "Rs.")

#Output
#Enter the distance in kilometers: 60
#The fare for traveling 60.0 kilometers is 600.0 Rs.
