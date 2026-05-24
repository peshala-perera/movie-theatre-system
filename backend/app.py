from flask import Flask, jsonify, request
from flask_cors import CORS
from theatre import Theatre
from allocator import allocate_seats

app = Flask(__name__)
CORS(app)

#separate cinema hall per movie
theatres = {
    "Moana 2": Theatre(),
    "Zootopia 2": Theatre(),
    "UP": Theatre(),
    "Lio & Stitch": Theatre(),
    "Tangled": Theatre()
}

#get cinema seats
@app.route('/seats', methods=['GET'])
def get_seats():
    movie = request.args.get('movie')
    if movie not in theatres:
        return jsonify({
            "success": False,
            "message": "Movie not found."
        }), 404
    return jsonify(
        theatres[movie].seats
    )

#auto seat allocation
@app.route('/allocate', methods=['POST'])
def allocate():
    data = request.json
    movie = data.get("movie")
    if movie not in theatres:
        return jsonify({
            "success": False,
            "message": "Movie not found."
        }), 404
    theatre = theatres[movie]
    result = allocate_seats(
        theatre,
        data
    )
    return jsonify(result)


if __name__ == "__main__":

    app.run(debug=True)