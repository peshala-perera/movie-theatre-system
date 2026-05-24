from helpers import (
    is_available,
    is_vip,
    is_disabled,
    create_seat_label
)

#find adjacent seats for small groups
def find_adjacent_seats(theatre, no_of_seats, allowed_types):
    allocated = []
    for row_index, row in enumerate(theatre.seats):
        current_block = []
        for col_index, seat in enumerate(row):
            if seat in allowed_types:
                current_block.append(
                    (row_index, col_index)
                )
            else:
                current_block = []
            if len(current_block) == no_of_seats:
                return current_block
    return allocated

#find edge seats for single customers
def find_edge_seat(theatre, no_of_seats, allowed_types):
    for row_index, row in enumerate(theatre.seats):
        if row[0] in allowed_types:
            return [(row_index, 0)]
        if row[-1] in allowed_types:
            return [(row_index, len(row)-1)]
    return []

#split large groups across rows if adjacent seats not available
def split_large_group(theatre, no_of_seats, allowed_types):
    allocated = []
    remaining = no_of_seats
    for row_index, row in enumerate(theatre.seats):
        current_block = []
        for col_index, seat in enumerate(row):
            if seat in allowed_types:
                current_block.append((row_index, col_index))
            else:
                current_block = []
            max_block = min(7, remaining)
            if len(current_block) == max_block:
                allocated.extend(current_block)
                remaining -= max_block
                current_block = []
                if remaining == 0:
                    return allocated
    return []

def find_adjacent_seats_in_rows(rows, group_size, allowed_types):
    for row_index, row in rows:
        current_block = []
        for col_index, seat in enumerate(row):
            if seat in allowed_types:
                current_block.append((row_index, col_index))
            else:
                current_block = []
            if len(current_block) == group_size:
                return current_block
    return []