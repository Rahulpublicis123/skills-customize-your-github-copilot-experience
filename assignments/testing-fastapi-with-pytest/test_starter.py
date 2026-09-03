"""Starter tests for the Testing FastAPI Applications with pytest assignment."""

from fastapi.testclient import TestClient

from app import app


client = TestClient(app)


def test_list_clubs():
    """Task 1: Test the response from GET /clubs."""
    # Check the status code and response data.
    pass


def test_get_existing_club():
    """Task 1: Test the response from GET /clubs/1."""
    # Check that the expected club is returned.
    pass


def test_get_missing_club():
    """Task 1: Test the 404 response for a missing club."""
    # Request a club ID that does not exist.
    pass


def test_create_club():
    """Task 2: Test creating a club with POST /clubs."""
    new_club = {
        "name": "Robotics Club",
        "teacher": "Ms. Chen",
        "meeting_day": "Thursday",
    }
    # Send new_club to the API and check the response.
    pass


def test_update_club():
    """Task 2: Test updating a club with PUT /clubs/1."""
    updated_club = {
        "name": "Advanced Art Club",
        "teacher": "Ms. Rivera",
        "meeting_day": "Tuesday",
    }
    # Send updated_club to the API and check the response.
    pass


def test_update_missing_club():
    """Task 2: Test the 404 response for updating a missing club."""
    # Try to update a club ID that does not exist.
    pass


def test_invalid_club_data():
    """Task 2: Test validation when a required field is missing."""
    invalid_club = {
        "name": "Science Club",
        "teacher": "Mr. Green",
    }
    # Send invalid_club and check that validation fails.
    pass