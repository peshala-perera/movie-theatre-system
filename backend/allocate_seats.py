def creates_isolated_seat(
    row,
    start,
    group_size
):

    temp_row = row[:]

    # Temporarily mark seats as booked
    for i in range(start, start + group_size):

        temp_row[i] = "X"

    # Check for isolated single seats
    for i in range(1, len(temp_row) - 1):

        if temp_row[i] == "O":

            if (
                temp_row[i - 1] == "X"
                and
                temp_row[i + 1] == "X"
            ):

                return True

    return False


def allocate_seats(
    seats,
    group_size,
    admin_override=False
):

    total_rows = len(seats)

    middle_row = total_rows // 2

    # =================================
    # Seating preference logic
    # =================================

    customer_type = "regular"

    if customer_type == "senior":

        # Senior citizens:
        # prioritize front rows

        row_priority = sorted(
            range(total_rows),
            key=lambda r: r
        )

    else:

        # Regular users:
        # prioritize center rows

        row_priority = sorted(
            range(total_rows),
            key=lambda r: abs(r - middle_row)
        )

    # =================================
    # SOLO BOOKING LOGIC
    # =================================

    if group_size == 1:

        for row_index in row_priority:

            row = seats[row_index]

            for col_index in range(len(row)):

                # Allow:
                # O = Available
                # V = VIP
                # D = Disability

                if row[col_index] in ["O", "V", "D"]:

                    left_booked = (
                        col_index > 0
                        and
                        row[col_index - 1] == "X"
                    )

                    right_booked = (
                        col_index < len(row) - 1
                        and
                        row[col_index + 1] == "X"
                    )

                    # Avoid isolated seating

                    if left_booked and right_booked:

                        continue

                    row[col_index] = "X"

                    return [
                        f"{chr(65 + row_index)}{col_index + 1}"
                    ]

    # =================================
    # FIRST:
    # Try allocating adjacent seats
    # =================================

    for row_index in row_priority:

        row = seats[row_index]

        count = 0
        start_index = 0

        for col_index in range(len(row)):

            # Allow:
            # O = Available
            # V = VIP
            # D = Disability

            if row[col_index] in ["O", "V", "D"]:

                if count == 0:

                    start_index = col_index

                count += 1

                if count == group_size:

                    # Prevent isolated seat gaps

                    if (
                        not admin_override
                        and
                        creates_isolated_seat(
                            row,
                            start_index,
                            group_size
                        )
                    ):

                        count = 0
                        continue

                    allocated = []

                    for i in range(
                        start_index,
                        start_index + group_size
                    ):

                        row[i] = "X"

                        allocated.append(
                            f"{chr(65 + row_index)}{i + 1}"
                        )

                    return allocated

            else:

                # Reset counter if blocked

                count = 0

    # =================================
    # SECOND:
    # Split group if no adjacent seats
    # available
    # =================================

    allocated = []

    remaining = group_size

    for row_index in row_priority:

        row = seats[row_index]

        for col_index in range(len(row)):

            if row[col_index] in ["O", "V", "D"]:

                row[col_index] = "X"

                allocated.append(
                    f"{chr(65 + row_index)}{col_index + 1}"
                )

                remaining -= 1

                if remaining == 0:

                    return allocated

    # =================================
    # No seats available
    # =================================

    return None