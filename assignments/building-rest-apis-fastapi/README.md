# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Build a small REST API with FastAPI to practice defining routes, returning JSON data, and validating request bodies with Pydantic. You will create an API for managing a collection of school clubs.

## 📝 Tasks

### 🛠️ Create a Read-Only Clubs API

#### Description
Complete the starter code to create a FastAPI application that exposes the school club data. Add an endpoint that returns all clubs and an endpoint that returns one club by its ID.

#### Requirements
Completed program should:

- Create a `FastAPI` application
- Define a `GET /clubs` route that returns all clubs as JSON
- Define a `GET /clubs/{club_id}` route that returns one club
- Return a `404` response when the requested club does not exist
- Start successfully with `uvicorn starter-code:app --reload`


### 🛠️ Add and Update Clubs

#### Description
Extend the API so users can create a club and update an existing club. Use a Pydantic model to validate incoming JSON and return clear status codes for successful and unsuccessful requests.

#### Requirements
Completed program should:

- Define a Pydantic model with required `name`, `teacher`, and `meeting_day` fields
- Define a `POST /clubs` route that accepts a validated request body and creates a club
- Return the created club, including its assigned ID, with a `201` status code
- Define a `PUT /clubs/{club_id}` route that updates an existing club
- Return a `404` response when updating a club that does not exist
- Test the API using the automatically generated documentation at `http://127.0.0.1:8000/docs`

Example request body:

```json
{
  "name": "Robotics Club",
  "teacher": "Ms. Chen",
  "meeting_day": "Thursday"
}
```