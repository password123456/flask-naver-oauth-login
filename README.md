# flask-naver-oauth-login
![made-with-python][made-with-python]
![Python Versions][pyversion-button]
![Hits]

[pyversion-button]: https://img.shields.io/pypi/pyversions/Markdown.svg
[made-with-python]: https://img.shields.io/badge/Made%20with-Python-1f425f.svg
[Hits]: https://hits.seeyoufarm.com/api/count/incr/badge.svg?url=https%3A%2F%2Fgithub.com%2Fpassword123456%2Fflask-naver-oauth-login&count_bg=%2379C83D&title_bg=%23555555&icon=&icon_color=%23E7E7E7&title=hits&edge_flat=false

a simple example app for implementing login functionality via Naver OAuth in a Flask application. Users can log in with their Naver accounts and obtain an access token through this app.

네이버 OAuth를 통해 로그인 기능을 구현하는 간단한 예제 앱입니다. 
이 앱을 통해 사용자는 네이버 계정으로 로그인하여 엑세스 토큰을 받아올 수 있습니다.

## Configuration
1) Register your application and obtain OAuth client ID and secret key from Naver Developer Center.
2) Open the app.py file and input the obtained values into the 'client_id' and 'client_secret' variables.

- 네이버 개발자 센터에서 애플리케이션을 등록하고 OAuth 클라이언트 ID 및 시크릿 키를 발급받습니다.
- app.py 파일의 'client_id' 와 'client_secret' 변수에 발급받은 값을 입력합니다.

## Step 1: Clone this repository:
```bash
# git clone https://github.com/password123456/flask-naver-oauth-login
```

## Step 2: Create and activate a virtual environment:
```bash
# virtualenv venv
# source venv/bin/activate
```

## Step 3: Install required packages:
```bash
# pip install -r requirements.txt
```

## Step 4: Run the app:
```bash
# python3 app.py
```

## Usage
- After running the app, navigate to http://127.0.0.1:8080/naver in your web browser.
- Click on the Naver login button to log in.
- Once logged in, the access token will be displayed.

# References
- [Flask Official Documentation](https://flask.palletsprojects.com/en)
- [Naver OAuth Official Documentation](https://developers.naver.com/docs/login/api/api.md)
