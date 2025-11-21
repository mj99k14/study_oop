from flask import Flask, request

app = Flask(__name__)

# Path : /, Method : Get
@app.route("/", methods=["GET"])
def home():
#   print(f"Path: {request.path}")
#   print(f"Method: {request.method}")

#   return "hello flask", 200, { "GSC" : "gsc"}

  uploaded_file_name = None

  # upload 파일 검사
  file_obj = request.files.get("file_key")
  if file_obj:
    uploaded_file_name = file_obj.filename

  # 현 http request 정보 출력
  return {
    "method": request.method,
    "url": request.url,
    "path": request.path,
    "query": request.args,
    "form": request.form,
    "headers": dict(request.headers),
    "cookies": request.cookies,
    "files": uploaded_file_name,
    "json": request.get_json(silent=True),
    "remote_addr": request.remote_addr
  }

if __name__ == "__main__":
  app.run(debug=True)