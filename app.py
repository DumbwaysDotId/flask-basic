from flask import Flask, request, json

app = Flask(__name__)

rooms = [
    {'id': 1, 'name': 'RN ID'},
    {'id': 2, 'name': 'JS ID'},
]

@app.route('/api/rooms')
def rooms_get():
    return json.dumps(rooms)

@app.route('/api/rooms', methods=['POST'])
def rooms_post():
    rooms.append({
        'id': request.json.get('id'),
        'name': request.json.get('name')
    })
    return "success"

# GET
@app.route('/api/news')
def all_news():
    return "GET all_news"

# POST
@app.route('/api/news', methods=['POST'])
def post_news():
    return "POST single_news"

# GET SINGLE
@app.route('/api/news/<:id>')
def get_news():
    return "GET single_news where id = id"

# DELETE SINGLE
@app.route('/api/news/<:id>')
def delete_news():
    return "DELETE single_news where id = id"

# PATCH SINGLE
@app.route('/api/news/<:id>', methods=['PATCH'])
def patch_news():
    return "PATCH single_news where id = id, data = form"


if __name__ == '__main__':
    app.run(debug=True)
