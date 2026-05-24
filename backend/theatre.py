class Theatre:

    def __init__(self):

        # =================================
        # Default cinema seating layout
        #
        # O = Available
        # X = Booked
        # V = VIP
        # B = Broken
        # D = Disability
        # N = No-children zone
        # " " = Aisle / walkway
        # =================================

        self.seats = [

            # Row A
            ["O", "O", "O", "O", "O", " ", "O", "O", "O", "O", " "],

            # Row B
            ["O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O"],

            # Row C
            ["O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O"],

            # Row D
            ["O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O"],

            # Row E
            ["O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O"],

            # Row F
            ["O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O"],

            # Row G
            ["O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O"]

        ]

        # =================================
        # Sample booked seats
        # =================================

        self.seats[0][2] = "X"   # A3
        self.seats[1][4] = "X"   # B5
        self.seats[2][5] = "X"   # C6

        # =================================
        # VIP seating section
        # =================================

        self.seats[0][6] = "V"   # A7
        self.seats[0][7] = "V"   # A8

        self.seats[3][4] = "V"   # D5
        self.seats[3][5] = "V"   # D6
        self.seats[3][6] = "V"   # D7

        self.seats[4][4] = "V"   # E5
        self.seats[4][5] = "V"   # E6
        self.seats[4][6] = "V"   # E7

        # =================================
        # Broken / unusable seat
        # =================================

        self.seats[3][3] = "B"   # D4

        # =================================
        # Accessibility seating
        # =================================

        self.seats[6][0] = "D"   # G1
        self.seats[6][10] = "D"  # G11

        # =================================
        # No-children restricted area
        # =================================

        self.seats[0][0] = "N"   # A1
        self.seats[0][1] = "N"   # A2