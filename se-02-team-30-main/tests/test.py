from pathlib import Path
import pytest
from app import app


def test_visitorresponse(client):
    response = client.get("/visitor_name")
    assert b"<h2>Shubham</h2>" in response.data


# get the resources folder in the tests folder
resources = Path(__file__).parent / "resources"


def test_edit_user(client):
    response = client.post("/user/2/edit", data={
        "name": "Flask",
        "theme": "dark",
        "picture": (resources / "picture.png").open("rb"),
    })
    assert response.status_code == 200
