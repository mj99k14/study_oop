from flask import Flask, make_response, request, jsonify

# app = Flask(__name__)
app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    print(request.headers['content-type'])
    return "hello flask"

if __name__ == "__main__":
  app.run(debug=True)