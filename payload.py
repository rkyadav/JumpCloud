from flask import Flask, jsonify, request, abort
import requests

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
        return jsonify({"Jump":"Cloud"})

@app.route('/manage_file', methods=['GET', 'POST'])
def manage_file():
    url = 'https://www.learningcontainer.com/wp-content/uploads/2020/04/sample-text-file.txt'
    filename = 'sample-text-file.txt'
    if (request.method == 'POST'):
        json_payload = request.get_json()
        if (json_payload['action'] == "download"):
            req = requests.get(url)
            with open(filename, 'wb') as f:
                for chunk in req.iter_content(chunk_size=8192):
                    if chunk:
                        f.write(chunk)
            return filename, 201
        elif (json_payload['action'] == "read"):
            with open(filename,"r") as file:
                content = file.read()
            return jsonify(content), 200
        else: 
            return jsonify({'you sent': json_payload}), 201
    else:
        abort(400)

if __name__ == '__main__':
    app.run(debug=True)
