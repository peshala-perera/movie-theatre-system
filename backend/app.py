from flask import Flask, jsonify, request
from flask_cors import CORS

from theatre import Theatre
from allocate_seats import allocate_seats


app = Flask(__name__)
CORS(app)


# =================================
# Create separate theatre halls
# for each movie
# =================================

theatres = {
    "Moana 2": Theatre(),
    "Zootopia 2": Theatre(),
    "UP": Theatre(),
    "Lio & Stitch": Theatre(),
    "Tangled": Theatre()
}


# =================================
# Simple admin override
# =================================

admin_override = False


# =================================
# Temporary in-memory users
# =================================

users = []


# =================================
# Get all seats for selected movie
# =================================

@app.route('/seats', methods=['GET'])
def get_seats():

    movie = request.args.get('movie')

    if movie not in theatres:

        return jsonify({
            'success': False,
            'message': 'Movie not found.'
        }), 404

    return jsonify(
        theatres[movie].seats
    )


# =================================
# Register user
# =================================

@app.route('/register', methods=['POST'])
def register():

    data = request.json

    username = data['username']
    password = data['password']

    # Check existing user
    for user in users:

        if user['username'] == username:

            return jsonify({
                'success': False,
                'message': 'Username already exists.'
            })

    users.append({
        'username': username,
        'password': password
    })

    return jsonify({
        'success': True,
        'message': 'Registration successful.'
    })


# =================================
# Login user
# =================================

@app.route('/login', methods=['POST'])
def login():

    data = request.json

    username = data['username']
    password = data['password']

    for user in users:

        if (
            user['username'] == username
            and
            user['password'] == password
        ):

            return jsonify({
                'success': True,
                'username': username
            })

    return jsonify({
        'success': False,
        'message': 'Invalid username or password.'
    })


# =================================
# Allocate seats automatically
# =================================

@app.route('/allocate', methods=['POST'])
def allocate():

    data = request.json

    group_size = int(data['group_size'])
    movie = data['movie']

    if movie not in theatres:

        return jsonify({
            'success': False,
            'message': 'Movie not found.'
        }), 404

    # Validate group size
    if group_size < 1 or group_size > 7:

        return jsonify({
            'success': False,
            'message': 'Group size must be between 1 and 7.',
            'seats': theatres[movie].seats
        })

    allocated = allocate_seats(
        theatres[movie].seats,
        group_size,
        admin_override
    )

    if allocated:

        return jsonify({
            'success': True,
            'allocated': allocated,
            'message': 'Seats allocated successfully.',
            'seats': theatres[movie].seats
        })

    return jsonify({
        'success': False,
        'message': 'No suitable adjacent seats available.',
        'seats': theatres[movie].seats
    })


# =================================
# Admin allocate seat manually
# =================================

@app.route('/admin_allocate', methods=['POST'])
def admin_allocate():

    data = request.json

    movie = data['movie']
    row = data['row']
    col = data['col']

    if movie not in theatres:

        return jsonify({
            'success': False,
            'message': 'Movie not found.'
        }), 404

    theatres[movie].seats[row][col] = "X"

    return jsonify({
        'success': True,
        'message': 'Admin override applied.',
        'seats': theatres[movie].seats
    })


# =================================
# Toggle admin override
# =================================

@app.route('/admin-override', methods=['POST'])
def toggle_admin_override():

    global admin_override

    admin_override = not admin_override

    return jsonify({
        'admin_override': admin_override
    })


# =================================
# Cancel booking
# =================================

@app.route('/cancel', methods=['POST'])
def cancel_booking():

    data = request.json

    movie = data['movie']
    seats_to_cancel = data['seats']

    if movie not in theatres:

        return jsonify({
            'success': False,
            'message': 'Movie not found.'
        }), 404

    theatre = theatres[movie]

    for seat in seats_to_cancel:

        row = ord(seat[0]) - 65
        col = int(seat[1:]) - 1

        if theatre.seats[row][col] == "X":

            theatre.seats[row][col] = "O"

    return jsonify({
        'success': True,
        'message': 'Booking cancelled successfully.',
        'seats': theatre.seats
    })


# =================================
# Reschedule booking
# =================================

@app.route('/reschedule', methods=['POST'])
def reschedule():

    data = request.json

    old_seats = data['old_seats']
    new_group_size = data['group_size']
    movie = data['movie']

    if movie not in theatres:

        return jsonify({
            'success': False,
            'message': 'Movie not found.'
        }), 404

    theatre = theatres[movie]

    # Release old seats
    for seat in old_seats:

        row = ord(seat[0]) - 65
        col = int(seat[1:]) - 1

        if theatre.seats[row][col] == "X":

            theatre.seats[row][col] = "O"

    # Allocate new seats
    allocated = allocate_seats(
        theatre.seats,
        new_group_size,
        admin_override
    )

    if allocated:

        return jsonify({
            'success': True,
            'allocated': allocated,
            'message': 'Rescheduling successful.',
            'seats': theatre.seats
        })

    return jsonify({
        'success': False,
        'message': 'Rescheduling failed.',
        'seats': theatre.seats
    })


# =================================
# Run Flask app
# =================================

if __name__ == '__main__':
    app.run(debug=True)