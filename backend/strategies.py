def determine_strategy(customer_type):
    if customer_type == "vip":
        return "VIP"
    elif customer_type == "disabled":
        return "DISABLED"
    else:
        return "REGULAR"