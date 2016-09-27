from flask import Flask, request
from flask import make_response
import requests
import os
import json

app = Flask(__name__)

@app.route('/chat')
def cf_connect():
    api_url = 'https://api.api.ai/v1/query?v=20150910&query='
    head = {'Authorization': 'Bearer fa64f569fcb544a38ec30ea3d7f4ab39'}
    s = requests.Session()
    result = s.get(api_url + 'trending today' + '&lang=en', headers=head)
    result = result.json()
    # print(result)
    res = json.dumps(result, indent=4)

    fulfil = result.get('fulfillment')
    data= fulfil.get("data")
    fb = data.get("facebook")
    element=[]
    element.append(fb)

    print('res' + '--->' + element)
    r = make_response(element)
    return r


if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))
    app.run(debug=False, port=port, host='0.0.0.0')
    # app.run(debug=False, port=port, host='127.0.0.1')
