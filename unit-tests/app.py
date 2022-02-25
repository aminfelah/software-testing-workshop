from crypt import methods
from datetime import datetime
from unittest import result
from flask import Flask, jsonify, request
from elasticsearch import Elasticsearch

es = Elasticsearch(hosts="http://localhost:9200")

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    result = es.search(index="employees", body={"query":{"match_all":{}}})

    return jsonify(result['_source'])

app.route('/add', methods=['POST'])
def insert_data():
    id = request.form['id']
    name = request.form['name']
    salary = request.form['salary']

    body = {
        'id': id,
        'name': name,
        'salary': salary,
        'timestamp': datetime.now()
    }

    result = es.index(index='employees', id=id, body=body)

    return jsonify(result)