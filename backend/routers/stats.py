from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session, joinedload
from sqlalchemy import func
from database import get_db
from models import Goal, Team, Match
from schemas import ScorerOut, TeamOut

router = APIRouter(prefix="/stats", tags=["stats"])


@router.get("/top-scorers", response_model=list[ScorerOut])
def top_scorers(limit: int = Query(20, ge=1, le=50), db: Session = Depends(get_db)):
    rows = (
        db.query(
            Goal.scorer,
            Goal.team_id,
            func.count(Goal.id).label("total"),
        )
        .filter(Goal.own_goal == False)
        .group_by(Goal.scorer, Goal.team_id)
        .order_by(func.count(Goal.id).desc())
        .limit(limit)
        .all()
    )
    result = []
    for scorer, team_id, total in rows:
        team = db.query(Team).filter(Team.id == team_id).first()
        result.append(ScorerOut(team=team, player=scorer, goals=total))
    return result


@router.get("/standings-summary")
def standings_summary(db: Session = Depends(get_db)):
    letters = [chr(ord("A") + i) for i in range(12)]
    summary = {}
    for letter in letters:
        teams = db.query(Team).filter(Team.group_letter == letter).all()
        total_goals = 0
        total_matches = 0
        for team in teams:
            matches = (
                db.query(Match)
                .filter(
                    ((Match.team1_id == team.id) | (Match.team2_id == team.id)),
                    Match.group_name == f"Group {letter}",
                    Match.played == True,
                )
                .all()
            )
            for m in matches:
                total_matches += 1
                if m.team1_id == team.id:
                    total_goals += m.score_ft_home or 0
                else:
                    total_goals += m.score_ft_away or 0

        summary[letter] = {
            "teams": len(teams),
            "matches_played": total_matches,
            "total_goals": total_goals,
        }
    return summary
