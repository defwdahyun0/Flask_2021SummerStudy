from flask import Flask
# !pip install flask

app = Flask(__name__) # 객체
#__name__은 모듈의 이름이 저장됨. 실행하는 코드에서는 __main__이 들어간다.
# 파이썬은 스크립트 언어. 시작점 없이 스크립트 코드를 바로 실행한다.

@app.route('/hello')
def hello():
    return "<h1>Hello World!<h1>"

if __name__ == "main":
    app.run(host="0.0.0.0", port="8080", debug=True) # 웹서버 돌리기