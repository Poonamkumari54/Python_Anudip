# Get the distance from the user
distance = float(input("Enter the distance in kilometers: "))

# Calculate the fare based on the distance
if distance >= 1 and distance <= 50:
    fare = distance * 8
elif distance >= 51 and distance <= 100:
    fare = distance * 10
else:
    fare = distance * 12

# Display the calculated fare
print("The fare for traveling", distance, "kilometers is", fare, "Rs.")