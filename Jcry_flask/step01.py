from flask import Flask, redirect, url_for

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello! I'm <h1>Jcry</h1>"

# url에 /하고 name 값입력하면 화면에 Hello {name}! 이 출력 됨.
@app.route("/<name>")
def user(name):
    return f"Hello {name}!"

# user함수에서 사용하는 name이라는 변수에 값을 Admin!으로 넣음.
@app.route("/admin")
def admin():
    return redirect(url_for("user", name="Admin!"))

if __name__=="__main__":
    app.run()