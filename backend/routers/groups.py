from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db
from models import Team, Match, Goal
from schemas import GroupOut, GroupStandingOut, TeamOut

router = APIRouter(prefix="/groups", tags=["groups"])

GROUP_LETTERS = [chr(ord("A") + i) for i in range(12)]


def compute_standings(db: Session, letter: str) -> list[GroupStandingOut]:
    teams = db.query(Team).filter(Team.group_letter == letter).order_by(Team.name).all()
    standings: list[dict] = []

    for team in teams:
        matches = (
            db.query(Match)
            .filter(
                ((Match.team1_id == team.id) | (Match.team2_id == team.id)),
                Match.group_name == f"Group {letter}",
            )
            .all()
        )
        played = won = drawn = lost = goals_for = goals_against = 0
        for m in matches:
            if not m.played:
                continue
            played += 1
            is_home = m.team1_id == team.id
            gf = m.score_ft_home if is_home else m.score_ft_away
            ga = m.score_ft_away if is_home else m.score_ft_home
            goals_for += gf or 0
            goals_against += ga or 0
            if (gf or 0) > (ga or 0):
                won += 1
            elif (gf or 0) < (ga or 0):
                lost += 1
            else:
                drawn += 1

        standings.append({
            "team": team,
            "played": played,
            "won": won,
            "drawn": drawn,
            "lost": lost,
            "goals_for": goals_for,
            "goals_against": goals_against,
            "goal_diff": goals_for - goals_against,
            "points": won * 3 + drawn,
        })

    standings.sort(key=lambda s: (-s["points"], -s["goal_diff"], -s["goals_for"]))
    return [
        GroupStandingOut(position=i + 1, **s)
        for i, s in enumerate(standings)
    ]


@router.get("", response_model=list[GroupOut])
def list_groups(db: Session = Depends(get_db)):
    return [
        GroupOut(letter=letter, standings=compute_standings(db, letter))
        for letter in GROUP_LETTERS
    ]


@router.get("/{letter}", response_model=GroupOut)
def get_group(letter: str, db: Session = Depends(get_db)):
    return GroupOut(letter=letter.upper(), standings=compute_standings(db, letter.upper()))
