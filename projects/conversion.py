# This file converts kilograms (kg) to pounds (lbs) and rounds the answer to 2 decimal places

# Kg amounts are stored and imputed here
kg_amount_1 = 34
kg_amount_2 = 42
kg_amount_3 = 76
kg_amount_4 = 99

# What the kgs are multiplied by
conversion_factor = 2.20462

# Converts kgs to lbs
lbs_1 = kg_amount_1 * conversion_factor
lbs_2 = kg_amount_2 * conversion_factor
lbs_3 = kg_amount_3 * conversion_factor
lbs_4 = kg_amount_4 * conversion_factor

# Prints results to console for kg_amount_1 through kg_amount_4
# Rounds to the second decimal place
print("\nPlease note that these calculations are rounded to the second decimal place.\n")
print(f"{kg_amount_1} kilogram(s) is about {lbs_1:.2f} pounds", "\n"
      f"{kg_amount_2} kilogram(s) is about {lbs_2:.2f} pounds", "\n"
      f"{kg_amount_3} kilogram(s) is about {lbs_3:.2f} pounds", "\n"
      f"{kg_amount_4} kilogram(s) is about {lbs_4:.2f} pounds", "\n"
      )
