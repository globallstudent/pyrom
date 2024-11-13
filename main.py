from app import PyRomApp

app = PyRomApp()

@app.route("/home")
def home(request, response):
    response.text = "Hello from Home Page"

@app.route("/about")
def about(request, response):
    response.text = "Hello from About Page"

