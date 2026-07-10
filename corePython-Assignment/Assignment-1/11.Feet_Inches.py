# Convert distance from feet and inches to meter and centimeter

feet = int(input("Enter distance in feet: "))
inches = float(input("Enter distance in inches: "))

# Step 1: Convert feet to inches
feet_in_inches = feet * 12

# Step 2: Find total inches
total_inches = feet_in_inches + inches

# Step 3: Convert inches to centimeters
total_centimeters = total_inches * 2.54

# Step 4: Convert centimeters to meters and remaining centimeters
meters = int(total_centimeters // 100)
centimeters = total_centimeters % 100

# Output
print("Distance in meters and centimeters:")
print("Meters =", meters)
print("Centimeters =", centimeters)



""" FLOW OF THE PROGRAM

    Feet + Inches
      ↓
    Feet → Inches
      ↓
    Total Inches
      ↓
    Inches → Centimeters
      ↓
    Centimeters → Meters + Remaining Centimeters
      ↓
    Output
    
"""