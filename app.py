from flask import Flask, jsonify, request
from flask_cors import CORS
from game_recommendation import obtain_recommendation

app = Flask(__name__)
CORS(app)


@app.route('/recommendations')
def recommendation():
    game_list = request.args.get('games')
    game_exceptions = request.args.get('exceptions')
    number = request.args.get('number')
    print(game_list, game_exceptions, number)
    return jsonify(obtain_recommendation(game_list, number, game_exceptions))


if __name__ == "__main__":
    app.run(debug=True)