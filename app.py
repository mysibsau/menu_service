from flask import Flask, jsonify
from parsers.menu_parser import get_all_menu


app = Flask(__name__)


@app.route('/menu', methods=['GET'])
def get_menu():
    # wget запрос
    file_name = './menu_files/menu_all_1.html'
    try:
        jsonify(list(get_all_menu(file_name))), 200
    except FileNotFoundError:
        return jsonify({'error': 'file menu not found'}), 404


if __name__ == '__main__':
    app.run(debug=False)
