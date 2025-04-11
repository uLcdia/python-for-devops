from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

if __name__ == '__main__':
  app.run(debug=True, host='0.0.0.0', port=8000)
"""
Traceback (most recent call last):
  File "/home/nenya/source/python-for-devops/./simple-python-app/app.py", line 1, in <module>
    from flask import Flask
ModuleNotFoundError: No module named 'flask'
"""
