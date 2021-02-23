from flask import Flask, jsonify
from parsers import get_all_menu
from os import popen
from json import loads as json_loads
from random import randint, choices


app = Flask(__name__)


@app.route('/menu/', methods=['GET'])
def get_menu():
    menu = popen(
        'wget https://menu-droom.pallada.int.sibsau.ru/menu_all \
            --ciphers=DEFAULT:@SECLEVEL=1 \
            --no-check-certificate \
            -qO-'
    ).read()

    return jsonify(get_all_menu(menu)), 200


@app.route('/menu/test/', methods=['GET'])
def get_test_menu():
    result = []
    dataset = json_loads(open('test_dataset.json').read())

    for room in dataset['rooms']:
        for type in dataset['types']:
            for dish in choices(dataset['types'][type], k=randint(2, 4)):
                dish['type'] = type
                dish['room'] = room
                result.append(dish)

    return jsonify(result)


if __name__ == '__main__':
    app.run(debug=True)
