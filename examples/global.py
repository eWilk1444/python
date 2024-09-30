"""
        Global variables should not change while the program is running
        They are constants
        Ex. Sales tax, 
        Gloabls should be in all caps 
    """

BAG_CHARGE = .10


def bag_cost(num_bags):
    cost = num_bags * BAG_CHARGE
    print(f"Cost for bags is: ${cost:.2f}")


bag_cost(10)
