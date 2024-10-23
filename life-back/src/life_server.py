
from flask import Flask, jsonify, request
import argparse
import logging
import game_management
import json

logging.basicConfig(level=logging.DEBUG)

major_version = 0
minor_version = 1
modification_version = 0
semantic_version = f"{major_version}.{minor_version}.{modification_version}"

default_port=5001
db_uri = None
app = Flask(__name__)

game_engine = None

@app.route('/start_game', methods=['POST'])
def start_game():
    json_config=request.form['config']
    config=json.loads(json_config)
    players=config['players']
    game_status = game_engine.start(players)
    return jsonify({"response": "success", "game" : game_status}), 200

@app.route('/pause_game', methods=['GET'])
def pause_game():
    game_status = game_engine.pause()
    return jsonify({"response": "success", "game" : game_status}), 200

@app.route('/stop_game', methods=['POST'])
def stop_game():
    game_status = game_engine.stop()
    return jsonify({"response": "success", "game" : game_status}), 200

@app.route('/query_game', methods=['GET'])
def query_game():
    game_status = game_engine.status()
    return jsonify({"response": "success","status" : game_status}), 200
   
def parse_args(parser):
    parser.add_argument('-P', '--port', type=int,
                        default=default_port, help='App listening port')
    parser.add_argument('-L', '--host', default='0.0.0.0',
                        help='App listening host')
    parser.add_argument(
        '-D', '--debug', action='store_true', help='Debug mode')
    return parser.parse_args()

if __name__ == '__main__':
    arg = parse_args(argparse.ArgumentParser())
    logging.info("host:", arg.host, " port:", arg.port)
    
    game_engine = game_management.Game()
    
    app.run(host='0.0.0.0', port=arg.port, debug=arg.debug)
