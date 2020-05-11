import flask
import json

from flask_cors import CORS

app = flask.Flask(__name__)
app.config["DEBUG"] = True
CORS(app)



@app.route('/', methods=['GET'])
def home():

    with open('./spiders/eatigo.json','r') as json_file:
        data = json.loads(json_file.read())
    data = {item["url"]: item for item in data}
    return data

app.run()