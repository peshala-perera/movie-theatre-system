import random

class Theatre:
    def __init__(self):
        self.layout = [
            [0,1,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,1,1],
            [1]*28,
            [1]*28,
            [1]*28,
            [1]*26,
            [0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0],
            [0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0],
            [0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0],
            [0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0],
            [0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,1,1,0],
            [0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0],
            [0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0],
            [0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,0,0,0],
            [0,0,0,1,1,1,1,1,1,1,1,1,1,1,0,0,0],
            [0,0,0,1,1,1,1,1,1,1,1,1,1,1,0,0,0]
        ]
        
        self.seats = []

        for row in self.layout:
            new_row = []
            for value in row:
                if value == 1:
                    new_row.append("O")
                else:
                    new_row.append(" ")

            self.seats.append(new_row)

        self.generate_disability_seats()
        self.generate_vip_seats()
        self.generate_broken_seats()


    def generate_broken_seats(self):
        broken_count = random.randint(6, 10)
        selected_broken = []
        row_broken_count = {}
        attempts = 0
        while len(selected_broken) < broken_count:
            attempts += 1
            if attempts > 1000:
                break
            row_index = random.randint(0, len(self.seats) - 1)
            row = self.seats[row_index]
            col_index = random.randint(0, len(row) - 1)
            seat = row[col_index]
            if seat != "O":
                continue
            current_row_count = row_broken_count.get(row_index, 0)
            if current_row_count >= 2:
                continue
            left_blocked = False
            right_blocked = False
            if col_index > 0:
                left_blocked = (row[col_index - 1] == "B")
            if col_index < len(row) - 1:
                right_blocked = (row[col_index + 1] == "B")
            if left_blocked or right_blocked:
                continue
            self.seats[row_index][col_index] = "B"
            selected_broken.append((row_index, col_index))
            row_broken_count[row_index] = (current_row_count + 1)


    def generate_disability_seats(self):
        disability_pairs_needed = 3
        generated_pairs = 0
        attempts = 0
        front_rows = [13, 14]
        while generated_pairs < disability_pairs_needed:
            attempts += 1
            if attempts > 1000:
                break
            row_index = random.choice(front_rows)
            row = self.seats[row_index]
            col_index = random.randint(0, len(row) - 2)
            first_seat = row[col_index]
            second_seat = row[col_index + 1]
            if first_seat != "O":
                continue
            if second_seat != "O":
                continue
            row[col_index] = "D"
            row[col_index + 1] = "D"
            generated_pairs += 1

    def generate_vip_seats(self):
        vip_rows = [4, 5, 6, 7, 8]
        selected_rows = random.sample(vip_rows, 4)
        for row_index in selected_rows:
            row = self.seats[row_index]
            vip_size = random.randint(12, 15)
            available_positions = []
            for col_index, seat in enumerate(row):
                if seat == "O":
                    available_positions.append(col_index)
            if len(available_positions) < vip_size:
                continue
            center_start = (len(available_positions) - vip_size) // 2
            vip_positions = available_positions[center_start:center_start + vip_size]
            for col_index in vip_positions:
                row[col_index] = "V"