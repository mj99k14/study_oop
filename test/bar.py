from flask import Flask

#flask 클래스의 객체 생성(현재 실행 프로그램의 경로를 인자 값으로 전달)
app = Flask(__name__)

#routing -> view function

@app.route("/")
def home():
    print("fff")
    return "hello flask" 
print(app.url_map)
#flask실행 
if __name__ == "__main__":
    #디버그:콘솔
    app.run(debug =True)