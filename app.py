import requests
from flask import Flask, redirect, request, render_template

app = Flask(__name__)

client_id = 'YOUR_CLIENT_ID'
client_secret = 'YOUR_CLIENT_SECRET'


@app.route('/naver')
def naver_login():
    redirect_uri = 'http://127.0.0.1:8080/callback'
    url = f'https://nid.naver.com/oauth2.0/authorize?client_id={client_id}&redirect_uri={redirect_uri}&response_type=code'
    return redirect(url)


@app.route('/callback')
def authorization_callback():
    params = request.args.to_dict()
    code = params.get('code')

    token_request_url = (f'https://nid.naver.com/oauth2.0/token?grant_type=authorization_code'
                         f'&client_id={client_id}&client_secret={client_secret}&code={code}')
    token_response = requests.get(token_request_url)
    token_data = token_response.json()

    access_token = token_data.get('access_token')
    profile_request = requests.get("https://openapi.naver.com/v1/nid/me", headers={'Authorization': f'Bearer {access_token}'})
    profile_data = profile_request.json()

    return render_template('callback.html', token_info=token_data, profile_info=profile_data)


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)
