from application import app
from os.path import dirname, join
from jinja2 import Template, FileSystemLoader, Environment

def test_application():
    # this errors out the second time through
    response = app.test_client().get('/')
    assert response.status_code == 200

def test_standalone():
    # this works
    templateLoader = FileSystemLoader(searchpath=join(dirname(__file__), '..', 'templates'))
    templateEnv = Environment(loader=templateLoader)
    t = templateEnv.get_template('t.html')
    rendered = t.render(c="baz")
    assert 'script' in rendered
