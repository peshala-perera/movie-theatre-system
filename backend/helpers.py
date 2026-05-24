#is seat available
def is_available(seat):

    return seat in ["O", "V", "D"]

#is vip seat
def is_vip(seat):
    return seat == "V"

#is disabled seat
def is_disabled(seat):
    return seat == "D"

#get row letter
def get_row_letter(index):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    return alphabet[index]

#create seat label
def create_seat_label(row, col): 
    row_letter = get_row_letter(row)
    return f"{row_letter}{col + 1}"