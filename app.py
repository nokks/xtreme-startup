import bottle

app = bottle.Bottle()

@app.get("/")
def home():
  return "Hello World"

def main():
  app.run(host="0.0.0.0", port=8080)

if __name__ == "__main__":
  main()
