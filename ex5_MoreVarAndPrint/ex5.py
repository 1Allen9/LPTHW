name = 'Zed A. Shaw'
age = 35 # not a lie
height = 74 # inches
meter_height = height * 0.0254 # inches
weight = 180 #lbs
kilogram = weight * 0.4535
eyes = 'Blues'
teeth = 'White'
hair = 'Brown'

print(f"Let's talk about {name}.")
print(f"He's {height} inches tall, that is {meter_height} meter.")
print(f"He's {weight} pounds heavy (aka {kilogram} kg.")
print("Actually that's not too heavy.")
print(f"He's got {eyes} eyes and {hair} hair.")
print(f"His teeth are usually {teeth} depending on the coffee.")

# this line is tricky, try to got it exactly right
total = age + height + weight
total_2 = age + meter_height + kilogram

print(f"If I add {age}, {height}, and {weight} I get {total}.")
print(f"total_2 is {total_2}")
print(f"round(total_2) is {round(total_2)}")
