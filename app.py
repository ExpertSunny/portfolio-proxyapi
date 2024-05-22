from flask import Flask, jsonify, make_response
import requests
from flask_cors import CORS, cross_origin

app = Flask(__name__)
CORS(app, origins="*")
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route('/proxyapi/thm-rank/', methods=['GET'])
def thm_api():
    try:
        response = requests.get('https://tryhackme.com/api/user/rank/ExpertSunny')
        proxy_response = make_response(response.text, response.status_code)
        proxy_response.headers['Content-Type'] = 'application/json'
        return proxy_response
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/proxyapi/htb-rank/', methods=['GET'])
def htb_api():
    try:
        headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
            'Accept-Encoding': 'gzip, deflate, br, zstd',
            'Accept-Language': 'en-US,en;q=0.5',
            'Connection': 'keep-alive',
            'Host': 'www.hackthebox.com',
            'Sec-Fetch-Dest': 'document',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-Site': 'cross-site',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:126.0) Gecko/20100101 Firefox/126.0'
        }

        response = requests.get(
            'https://www.hackthebox.com/api/v4/profile/391497',
            headers=headers
        )

        proxy_response = make_response(response.text, response.status_code)
        proxy_response.headers['Content-Type'] = 'application/json'
        return proxy_response
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000)
