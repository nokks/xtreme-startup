import bottle
from bottle import request
import wolframalpha

client = wolframalpha.Client("5UL6XH-64G6L9Y5R4")
app = bottle.Bottle()

bottle.debug = True

@app.get("/")
def home():
	query = request.query["q"]
	terms = query.split(":")
	strq = "".join(terms[1:])
	print("QUERY: %s"%strq)
	
	res = client.query(strq)
	try:
		return next(res.results).text
	except:
		return ""
	
def main():
  app.run(host="0.0.0.0", port=8080)

if __name__ == "__main__":
  main()
