from flask import Flask, Response,request

# Flask 애플리케이션 객체 생성
# 이 객체에 라우트, 훅(before/after), 설정 등이 모두 등록됨
app = Flask(__name__)


# -----------------------------
# 1. 모든 요청(Request) 전에 실행되는 전역 Hook
# -----------------------------
@app.before_request   # 모든 라우트 실행 전에 먼저 실행되는 데코레이터
def prt_log():
    # 공통 전처리 작업 (로깅, 인증 체크 등)
    print("Log")


# -----------------------------
# 2. "/" 경로(GET) 요청 처리
# -----------------------------
@app.route("/", methods=["GET"])  # "/" URL에 GET 요청이 오면 이 함수를 실행
def home():
    # Response 구조: (본문, 상태코드, 헤더)
    # 여기서는 custom header "GSC"를 추가한 예시
    print(f"path:{request.path}")
    print(f"Method:{request.method}")
    return "hello flask", 200, {"GSC": "gsc"}


# -----------------------------
# 3. "/students/<int:id>" 경로(GET) 요청 처리
# -----------------------------
@app.route("/students/<int:id>", methods=["GET"])  
# <int:id>는 URL에서 정수 타입 파라미터를 추출하는 Flask의 동적 라우트 문법
def student(id):
    # URL에서 받아온 id를 그대로 응답
    return f"Student ID : {id}"


# -----------------------------
# 4. 모든 응답(Response)을 클라이언트에 보내기 직전에 실행되는 후처리 Hook
# -----------------------------
@app.after_request   # View 함수가 끝나고, 응답을 보내기 직전에 실행
def prt_after(rsp: Response):
    # 응답 헤더 중 "GSC" 값을 출력
    # "/" 경로에서는 "gsc", 다른 경로는 None
    print(rsp.headers.get('GSC'))
    
    # after_request는 반드시 Response 객체를 return 해야함
    return rsp

@app.teardown_request
def teardown(e):
  print(e)

# -----------------------------
# Flask 앱 실행
# -----------------------------
if __name__ == "__main__":
    # debug=True → 코드 변경 시 자동 재시작, 에러 화면 자세히 표시
    app.run(debug=True)
