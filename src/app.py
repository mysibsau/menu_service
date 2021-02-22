from flask import Flask, jsonify
from parsers.menu_parser import get_all_menu
from os import system


app = Flask(__name__)
MNEU_FILE_NAME = 'menu_files/menu_all_1.html'


@app.route('/menu', methods=['GET'])
def get_menu():

    system(
        f'wget https://menu-droom.pallada.int.sibsau.ru/menu_all \
            --ciphers=DEFAULT:@SECLEVEL=1 \
            --no-check-certificate \
            -O {MNEU_FILE_NAME}'
    )

    try:
        return jsonify(list(get_all_menu(MNEU_FILE_NAME))), 200
    except FileNotFoundError:
        return jsonify({'error': 'file menu not found'}), 404


if __name__ == '__main__':
    app.run(debug=False)
