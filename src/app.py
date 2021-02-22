from flask import Flask, jsonify
from parsers import get_all_menu
from os import popen


app = Flask(__name__)
MNEU_FILE_NAME = 'menu_files/menu_all_1.html'


@app.route('/menu', methods=['GET'])
def get_menu():
    menu = popen(
        'wget https://menu-droom.pallada.int.sibsau.ru/menu_all \
            --ciphers=DEFAULT:@SECLEVEL=1 \
            --no-check-certificate \
            -qO-'
    ).read()

    return jsonify(list(get_all_menu(menu))), 200


if __name__ == '__main__':
    app.run(debug=False)
