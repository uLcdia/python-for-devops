from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

if __name__ == '__main__':
    app.run("0.0.0.0")

"""
Traceback (most recent call last):
  File "/home/nenya/source/python-for-devops/./Day-15/examples/hello-world.py", line 1, in <module>
    from flask import Flask
ModuleNotFoundError: No module named 'flask'
"""
