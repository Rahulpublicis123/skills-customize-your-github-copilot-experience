"""FastAPI application under test for the pytest assignment."""

from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel

app = FastAPI(title="Mergington Clubs API")

clubs = {
    1: {"id": 1, "name": "Art Club", "teacher": "Ms. Rivera", "meeting_day": "Monday"},
    2: {"id": 2, "name": "Chess Club", "teacher": "Mr. Patel", "meeting_day": "Wednesday"},
}


class Club(BaseModel):
    name: str
    teacher: str
    meeting_day: str


@app.get("/clubs")
def list_clubs():
    return list(clubs.values())


@app.get("/clubs/{club_id}")
def get_club(club_id: int):
    if club_id not in clubs:
        raise HTTPException(status_code=404, detail="Club not found")
    return clubs[club_id]


@app.post("/clubs", status_code=status.HTTP_201_CREATED)
def create_club(club: Club):
    club_id = max(clubs, default=0) + 1
    clubs[club_id] = {"id": club_id, **club.model_dump()}
    return clubs[club_id]


@app.put("/clubs/{club_id}")
def update_club(club_id: int, club: Club):
    if club_id not in clubs:
        raise HTTPException(status_code=404, detail="Club not found")
    clubs[club_id] = {"id": club_id, **club.model_dump()}
    return clubs[club_id]