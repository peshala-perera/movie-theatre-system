import unittest

from allocate_seats import allocate_seats


class TestSeatAllocation(unittest.TestCase):

    # =================================
    # Normal allocation test
    # =================================

    def test_successful_allocation(self):

        seats = [
            ["O", "O", "O", "O"],
            ["X", "X", "O", "O"]
        ]

        result = allocate_seats(
            seats,
            2
        )

        self.assertEqual(
            result,
            ["A1", "A2"]
        )

    # =================================
    # No adjacent seats available
    # =================================

    def test_no_adjacent_seats(self):

        seats = [
            ["X", "O", "X", "O"],
            ["X", "O", "X", "O"]
        ]

        result = allocate_seats(
            seats,
            2
        )

        self.assertIsNone(result)

    # =================================
    # Prevent double booking
    # =================================

    def test_prevent_double_booking(self):

        seats = [
            ["X", "X", "O", "O"]
        ]

        result = allocate_seats(
            seats,
            2
        )

        self.assertEqual(
            result,
            ["A3", "A4"]
        )

    # =================================
    # Broken seats should not allocate
    # =================================

    def test_broken_seat_not_allocated(self):

        seats = [
            ["O", "B", "O", "O"]
        ]

        result = allocate_seats(
            seats,
            2
        )

        self.assertIsNone(result)

    # =================================
    # Prevent isolated single seats
    # =================================

    def test_scattered_seat_prevention(self):

        seats = [
            ["X", "O", "O", "X"]
        ]

        result = allocate_seats(
            seats,
            2
        )

        self.assertIsNone(result)

    # =================================
    # Large group booking
    # =================================

    def test_large_group_booking(self):

        seats = [
            ["O", "O", "O", "O", "O", "O", "O"]
        ]

        result = allocate_seats(
            seats,
            7
        )

        self.assertEqual(
            result,
            [
                "A1",
                "A2",
                "A3",
                "A4",
                "A5",
                "A6",
                "A7"
            ]
        )

    # =================================
    # Split groups if necessary
    # =================================

    def test_split_large_group_when_needed(self):

        seats = [
            ["X", "X", "X", "O"],
            ["O", "O", "O", "O"]
        ]

        result = allocate_seats(
            seats,
            5
        )

        self.assertEqual(
            len(result),
            5
        )

    # =================================
    # Solo users not between groups
    # =================================

    def test_solo_booking_not_between_groups(self):

        seats = [
            ["X", "O", "X", "O"]
        ]

        result = allocate_seats(
            seats,
            1
        )

        self.assertEqual(
            result,
            ["A4"]
        )

    # =================================
    # Admin override test
    # =================================

    def test_admin_override_allows_scattered_seats(self):

        seats = [
            ["X", "O", "O", "X"]
        ]

        result = allocate_seats(
            seats,
            2,
            admin_override=True
        )

        self.assertEqual(
            result,
            ["A2", "A3"]
        )

    # =================================
    # VIP seat allocation
    # =================================

    def test_vip_seat_allocation(self):

        seats = [
            ["V", "V", "O"]
        ]

        result = allocate_seats(
            seats,
            2
        )

        self.assertEqual(
            result,
            ["A1", "A2"]
        )

    # =================================
    # Disability seat allocation
    # =================================

    def test_accessibility_seat_allocation(self):

        seats = [
            ["D", "O", "O"]
        ]

        result = allocate_seats(
            seats,
            1
        )

        self.assertEqual(
            result,
            ["A1"]
        )

    # =================================
    # Senior priority logic
    # =================================

    def test_senior_priority_logic(self):

        seats = [
            ["O", "O", "O"],
            ["O", "O", "O"],
            ["O", "O", "O"]
        ]

        result = allocate_seats(
            seats,
            1
        )

        self.assertIsNotNone(result)

    # =================================
    # Nearly full cinema test
    # =================================

    def test_nearly_full_cinema(self):

        seats = [

            ["X", "X", "X", "X", "X"],

            ["X", "O", "O", "X", "X"],

            ["X", "X", "X", "X", "X"]

        ]

        result = allocate_seats(
            seats,
            2
        )

        self.assertEqual(
            result,
            ["B2", "B3"]
        )

    # =================================
    # Random broken seat stress test
    # =================================

    def test_random_broken_seats(self):

        seats = [
            ["O", "B", "O", "B", "O"],
            ["O", "O", "B", "O", "O"]
        ]

        result = allocate_seats(
            seats,
            2
        )

        self.assertIsNotNone(result)

    # =================================
    # Row overflow test
    # =================================

    def test_row_overflow_scenario(self):

        seats = [
            ["O", "O"],
            ["O", "O"]
        ]

        result = allocate_seats(
            seats,
            5
        )

        self.assertIsNone(result)

    # =================================
    # Single-gap prevention stress test
    # =================================

    def test_single_gap_prevention(self):

        seats = [
            ["X", "O", "O", "X", "O"]
        ]

        result = allocate_seats(
            seats,
            2
        )

        self.assertIsNone(result)

    # =================================
    # Half-full cinema test
    # =================================

    def test_half_full_cinema(self):

        seats = [

            ["X", "X", "O", "O", "O"],

            ["O", "O", "X", "X", "O"],

            ["O", "O", "O", "X", "X"]

        ]

        result = allocate_seats(
            seats,
            3
        )

        self.assertIsNotNone(result)


if __name__ == "__main__":

    unittest.main()