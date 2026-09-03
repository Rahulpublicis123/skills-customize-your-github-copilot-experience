# 📘 Assignment: Testing FastAPI Applications with pytest

## 🎯 Objective

Learn how to test a FastAPI application with pytest and FastAPI's `TestClient`. You will write automated tests for the school clubs API, including successful requests, missing resources, and invalid input.

Run the tests from the assignment folder with `pytest test_starter.py`.

## 📝 Tasks

### 🛠️ Test Read Routes

#### Description
Complete the starter test file to verify the API's read-only routes. Use `TestClient` to send requests to the application without starting a web server.

#### Requirements
Completed test suite should:

- Verify that `GET /clubs` returns a `200` status code
- Verify that the clubs list includes the expected club data
- Verify that `GET /clubs/1` returns the correct club
- Verify that requesting a missing club returns a `404` status code
- Use pytest test functions and clear assertions


### 🛠️ Test Create, Update, and Validation Behavior

#### Description
Add tests for creating and updating clubs. Also test that FastAPI rejects a request with a missing required field. Tests should be independent and should not rely on the order in which pytest runs them.

#### Requirements
Completed test suite should:

- Verify that `POST /clubs` returns a `201` status code and the created club
- Verify that `PUT /clubs/{club_id}` updates an existing club
- Verify that updating a missing club returns a `404` status code
- Verify that invalid request data returns a `422` status code
- Run successfully with `pytest test_starter.py`