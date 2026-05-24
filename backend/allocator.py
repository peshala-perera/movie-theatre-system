from theatre import Theatre
from strategies import determine_strategy
from rules import (
    find_adjacent_seats,
    find_edge_seat,
    split_large_group,
    find_adjacent_seats_in_rows
)
from helpers import create_seat_label


#main auto allocation function
def allocate_seats(theatre, data):
    movie = data.get("movie")
    no_of_seats = data.get("no_of_seats")
    customer_type = data.get("customer_type")
    is_admin = data.get("is_admin")

    #define strategy based on customer type
    strategy = determine_strategy(
        customer_type
    )

    allocated = []


    #vip customers get VIP seats, disabled customers get disabled seats, regular customers get regular seats
    if strategy == "VIP":
        allowed_types = ["V"]
    elif strategy == "DISABLED":
        allowed_types = ["D"]
    else:
        allowed_types = ["O"]


    #single customers get edge seats, small groups get adjacent seats, large groups get split across rows
    if strategy == "REGULAR":
        if no_of_seats == 1:
            allocated = find_edge_seat(theatre, no_of_seats, allowed_types)
        if no_of_seats <= 7:
            allocated = find_adjacent_seats(theatre, no_of_seats, allowed_types)
        else:
            allocated = split_large_group(theatre, no_of_seats, allowed_types)

    elif strategy == "VIP":
        if no_of_seats <= 7:
            allocated = find_adjacent_seats(theatre, no_of_seats, allowed_types)
        else:
            allocated = split_large_group(theatre, no_of_seats, allowed_types)


    #disabled customers get priority for front rows, then adjacent seats, then split across rows
    elif strategy == "DISABLED":
        allocated = find_adjacent_seats(theatre, no_of_seats, ["D"])
        if len(allocated) == 0:
            front_rows = [(13, theatre.seats[13]), (14, theatre.seats[14])]
            allocated = find_adjacent_seats_in_rows(front_rows, no_of_seats, ["O"])
            if len(allocated) == 0:
                allocated = find_adjacent_seats(theatre, no_of_seats, ["O"])


    #admin override can bypass all rules and allocate any available seats
    if is_admin and len(allocated) == 0:
        allocated = split_large_group(
            theatre,
            no_of_seats,
            ["O", "V", "D"]
        )


    # finally, if no seats allocated, return failure
    if len(allocated) == 0:

        return {
            "success": False,
            "message": "No seats available",
            "seats": theatre.seats
        }


    #mark allocated seats in theatre and create seat labels for response
    seat_labels = []
    for row, col in allocated:
        theatre.seats[row][col] = "X"
        seat_labels.append(
            create_seat_label(row, col)
        )


    return {
        "success": True,
        "movie": movie,
        "strategy": strategy,
        "allocated_seats": seat_labels,
        "seats": theatre.seats,
    }