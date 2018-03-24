from flask import Flask, request
import random

app = Flask(__name__)

def genStr (n):
	string = ''
	i = 0
	while i < n:
		c = str(random.randint(0,9))
		string += c
		i += 1
	return string

@app.route("/")
def main_get():
	return genStr(2048)

@app.route("/",methods=['POST'])
def main_post():
	try:
		n = int(request.form['n'])
		return genStr(n)
	except Exception:
		return "ERROR"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)
