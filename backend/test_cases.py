from theatre import Theatre
from rules import (
    find_adjacent_seats,
    find_edge_seat,
    split_large_group,
    find_adjacent_seats_in_rows
)

from strategies import determine_strategy


print("movie theatre seat allocation - TESTING")


#create fresh theatre
theatre = Theatre()


# 5.1.1 find_adjacent_seats()

print("5.1.1 Testing find_adjacent_seats()\n")

allocated = find_adjacent_seats(
    theatre,
    4,
    ["O"]
)

print("TC-01 -> Request 4 regular seats")
print("Allocated:", allocated)

if len(allocated) == 4:
    print("Result: PASS\n")
else:
    print("Result: FAIL\n")


allocated = find_adjacent_seats(
    theatre,
    3,
    ["V"]
)

print("TC-02 -> Request 3 VIP seats")
print("Allocated:", allocated)

if len(allocated) == 3:
    print("Result: PASS\n")
else:
    print("Result: FAIL\n")


# 5.1.2 find_edge_seat()

print("5.1.2 Testing find_edge_seat()\n")

allocated = find_edge_seat(
    theatre,
    ["O"]
)

print("TC-03 -> Request solo edge seat")
print("Allocated:", allocated)

if len(allocated) == 1:
    print("Result: PASS\n")
else:
    print("Result: FAIL\n")


# 5.1.3 split_large_group()

print("5.1.3 Testing split_large_group()\n")

allocated = split_large_group(
    theatre,
    12,
    ["O"]
)

print("TC-04 -> Request 12 seats")
print("Allocated:", allocated)

if len(allocated) == 12:
    print("Result: PASS\n")
else:
    print("Result: FAIL\n")


allocated = split_large_group(
    theatre,
    20,
    ["O"]
)

print("TC-05 -> Request 20 seats")
print("Allocated:", allocated)

if len(allocated) == 20:
    print("Result: PASS\n")
else:
    print("Result: FAIL\n")


# 5.1.4 find_adjacent_seats_in_rows()

print("5.1.4 Testing find_adjacent_seats_in_rows()\n")

front_rows = [
    (13, theatre.seats[13]),
    (14, theatre.seats[14])
]

allocated = find_adjacent_seats_in_rows(
    front_rows,
    2,
    ["O", "D"]
)

print("TC-06 -> Request adjacent seats in front rows")
print("Allocated:", allocated)

if len(allocated) == 2:
    print("Result: PASS\n")
else:
    print("Result: FAIL\n")


# 5.1.5 determine_strategy()

print("5.1.5 Testing determine_strategy()\n")

strategy = determine_strategy("vip")

print("TC-07 -> VIP strategy")
print("Returned:", strategy)

if strategy == "VIP":
    print("Result: PASS\n")
else:
    print("Result: FAIL\n")


strategy = determine_strategy("disabled")

print("TC-08 -> Disabled strategy")
print("Returned:", strategy)

if strategy == "DISABLED":
    print("Result: PASS\n")
else:
    print("Result: FAIL\n")


strategy = determine_strategy("regular")

print("TC-09 -> Regular strategy")
print("Returned:", strategy)

if strategy == "REGULAR":
    print("Result: PASS\n")
else:
    print("Result: FAIL\n")


print("all test cases completed")