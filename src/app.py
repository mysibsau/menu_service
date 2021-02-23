from flask import Flask, jsonify
from parsers import get_all_menu
import os
from json import loads as json_loads
from random import randint, choices


app = Flask(__name__)
BASE_DIR = os.path.abspath(os.path.dirname(__file__))


@app.route('/menu/', methods=['GET'])
def get_menu():
    menu = os.popen(
        'wget https://menu-droom.pallada.int.sibsau.ru/menu_all \
            --ciphers=DEFAULT:@SECLEVEL=1 \
            --no-check-certificate \
            -qO-'
    ).read()

    return jsonify(get_all_menu(menu)), 200


@app.route('/menu/test/', methods=['GET'])
def get_test_menu():
    result = []
    dataset = json_loads(open(os.path.join(BASE_DIR, 'test_dataset.json')).read())

    for room in dataset['rooms']:
        for type_dish in dataset['types']:
            for dish in choices(dataset['types'][type_dish], k=randint(2, 4)):
                tmp = dish.copy()
                tmp['type'] = type_dish
                tmp['room'] = room
                result.append(tmp)

    return jsonify(result), 200


if __name__ == '__main__':
    app.run(debug=False)
