from flask import Flask, jsonify
from parsers.menu_parser import get_all_menu


app = Flask(__name__)

@app.route('/menu', methods=['GET'])
def get_menu():
    # wget запрос
    file_name = './menu_files/menu_all.html'
    try:
        html_menu = open(file_name)
    except FileNotFoundError:
        return jsonify({'error': 'file menu not found'}), 404

    return jsonify(list(get_all_menu(file_name))), 200


if __name__ == '__main__':
    app.run(debug=False)