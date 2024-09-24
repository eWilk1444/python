"""
    Recites the "99 bottles of beer" song
"""
# in-scope variable in while loop
bottles_of_beer = int(99)

# Main logic
while bottles_of_beer >= 2:
    print(f"{bottles_of_beer} bottles of beer on the wall,")
    print(f"{bottles_of_beer} bottles of beer!")
    print("Take one down, pass it around;")
    bottles_of_beer -= 1
    print(f"We got {bottles_of_beer} more bottles of beer on the wall!\n")
    if bottles_of_beer == 1:  # For proper grammer when singular and non-existent quantities of bottles is mentioned
        print(f"{bottles_of_beer} bottle of beer on the wall,")
        print(f"{bottles_of_beer} bottle of beer!")
        print("Take the last one down, pass it around;")
        print(f"We got no more bottles of beer on the wall!\n")
