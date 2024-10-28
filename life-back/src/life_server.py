
from flask import Flask, jsonify, request
import argparse
import logging
import game_management
import json

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
    if game_engine is not None:
        game_status = game_engine.pause()
        return jsonify({"response": "success", "game" : game_status}), 200
    else:
        return jsonify({"response": "failure", "game" : "Not started"}), 400

@app.route('/stop_game', methods=['POST'])
def stop_game():
    game_status = game_engine.stop()
    return jsonify({"response": "success", "game" : game_status}), 200

@app.route('/query_game', methods=['GET'])
def query_game():
    if game_engine is not None:
        game_status = game_engine.status()
        return jsonify({"response": "success","status" : game_status}), 200
    else:
        return jsonify({"response": "failure","status" : "Not started"}), 400
   
def parse_args(parser):
    parser.add_argument('-P', '--port', type=int,
                        default=default_port, help='App listening port')
    parser.add_argument('-L', '--host', default='0.0.0.0',
                        help='App listening host')
    parser.add_argument(
        '-D', '--debug', action='store_true', help='Debug mode')
    return parser.parse_args()

def process():
    #TODO Handle debugging according to the parameter
    arg = parse_args(argparse.ArgumentParser())
    level = logging.DEBUG if arg.debug is True else logging.INFO 
    app.logger.setLevel(level=level)
    logging.basicConfig(level=level)
    logging.debug(f"host:{arg.host} port: {arg.port} debug: {arg.debug}")
    
    
    app.run(host=arg.host, port=arg.port, debug=arg.debug)

if __name__ == '__main__':
    game_engine = game_management.Game()
    process()
