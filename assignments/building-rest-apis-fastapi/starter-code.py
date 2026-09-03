"""Starter code for the Building REST APIs with FastAPI assignment."""

from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel

app = FastAPI(title="Mergington Clubs API")

clubs = {
    1: {"id": 1, "name": "Art Club", "teacher": "Ms. Rivera", "meeting_day": "Monday"},
    2: {"id": 2, "name": "Chess Club", "teacher": "Mr. Patel", "meeting_day": "Wednesday"},
}


class Club(BaseModel):
    """Data required to create or update a club."""

    name: str
    teacher: str
    meeting_day: str


@app.get("/clubs")
def list_clubs():
    """Return all school clubs."""
    # Task 1: Return the clubs collection.
    pass


@app.get("/clubs/{club_id}")
def get_club(club_id: int):
    """Return one club by ID."""
    # Task 1: Look up the club and raise HTTPException when it is missing.
    pass


@app.post("/clubs", status_code=status.HTTP_201_CREATED)
def create_club(club: Club):
    """Create a club with the next available ID."""
    # Task 2: Add the validated club to the collection and return it.
    pass


@app.put("/clubs/{club_id}")
def update_club(club_id: int, club: Club):
    """Replace an existing club's details."""
    # Task 2: Check that the ID exists, update the club, and return it.
    pass