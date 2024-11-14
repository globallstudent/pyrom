import pytest


def test_basic_route_adding(app):
    @app.route("/home")
    def home(req, resp):
        resp.text = "Hello from home"

def test_dublicate_routes_throws_excepton(app):
    @app.route("/home")
    def home(req, resp):
        resp.text = "Hello from home"

    with pytest.raises(AssertionError):
        @app.route("/home")
        def home2(req, resp):
            resp.text = "Hello from home2"

def test_requests_can_be_sent_by_test_client(app, test_client):
    @app.route("/home")
    def home(req, resp):
        resp.text = "Hello from home"

    response = test_client.get("http://testserver/home")

    assert response.text == "Hello from home"

def test_parameterized_routing(app, test_client):
    @app.route("/hello/{name}")
    def greeting(request, response, name):
        response.text = f"Hello {name}"
    
    assert test_client.get("http://testserver/hello/Asliddin").text == "Hello Asliddin"
    assert test_client.get("http://testserver/hello/Matthew").text == "Hello Matthew"

def test_default_response(test_client):
    response = test_client.get("http://testserver/nonexistent/")

    assert response.text == "Not Found"
    assert response.status_code == 404

def test_class_based_get(app, test_client):
    @app.route("/books")
    class Books:
        def get(self, req, resp):
            resp.text = "Books page"
            
    assert test_client.get("http://testserver/books").text == "Books page"