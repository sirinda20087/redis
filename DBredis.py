import os
import json
import redis
from flask import Flask,request,jsonify

app = Flask(__name__)
db = redis.StrictRedis(
        host='node9156-advweb-18.app.ruk-com.cloud',
        port=11166,
        password='RBLoox93611'
        ,decode_responses=True)


@app.route('/',methods=['GET'])
def show():
    name=db.keys()
    name.sort()
    req = []
    for r in name :
        req.append(db.hgetall(r))
    return jsonify(req)
    #return 'Hello %s!' % name

@app.route('/setname/<name>')
def setname(name):
    db.set('name',name)
    return 'Name updated.'

if __name__ == '__main__':
    app.run()