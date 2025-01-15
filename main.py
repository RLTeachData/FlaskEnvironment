from flask import Flask

app = Flask(__name__)

html = '''
<html>
    <head>
        <title>Flask App</title>
    </head>
    <body>
        <h1>Hello, World!</h1>
    </body>
</html>
'''
# 指定路由
@app.route("/")
def hello_world():
    return html

if __name__ == "__main__":
    while True:
        app.run(port=8100, host="0.0.0.0", debug=True)