from flask import Flask,request,make_response,jsonify

app = Flask(__name__,
            static_folder ="resources/",
            static_url_path="/contents")

print(f"app.static_folder: {app.static_folder}")
print(f"app.static_url_path:{app.static_url_path}")


@app.route ("/", methods=["GET"])
def home():
    # body = " hello flask"

    # resp = make_response(body, 200)
    # resp.headers["TEST 1"] = 1
    # resp.headers["TEST 2"] = 2
    # resp.headers["TEST 3"] = 3
    
    # # return "hello flask", 200, {"Test-code": "GSC" }
    # # return "hello flask",404
    # return resp
    return {"name": "kmj", "age": 29}


# @app.after_request
# def post_process(respone):
#     ### 여기에 가공된 
#     #reutrn  response
#     return ...

if __name__ == "__main__":
    app.run(debug=True)