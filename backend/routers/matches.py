from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session, joinedload
from database import get_db
from models import Match
from schemas import MatchOut

router = APIRouter(prefix="/matches", tags=["matches"])


def match_to_out(m: Match) -> MatchOut:
    winner = None
    if m.winner_id:
        winner = m.home_team if m.winner_id == m.team1_id else m.away_team

    return MatchOut(
        id=m.id,
        round_name=m.round_name,
        date=m.date,
        time=m.time,
        team1=m.home_team,
        team2=m.away_team,
        score_ft_home=m.score_ft_home,
        score_ft_away=m.score_ft_away,
        score_ht_home=m.score_ht_home,
        score_ht_away=m.score_ht_away,
        group_name=m.group_name,
        stadium=m.stadium_rel,
        knockout=m.knockout,
        winner=winner,
        played=m.played,
        goals=m.goals,
    )


@router.get("", response_model=list[MatchOut])
def list_matches(
    group: str | None = Query(None),
    team: str | None = Query(None),
    round: str | None = Query(None, alias="round_name"),
    db: Session = Depends(get_db),
):
    q = db.query(Match).options(
        joinedload(Match.home_team),
        joinedload(Match.away_team),
        joinedload(Match.stadium_rel),
        joinedload(Match.goals),
    )
    if group:
        q = q.filter(Match.group_name == f"Group {group.upper()}")
    if team:
        q = q.filter(
            (Match.home_team.has(name=team)) | (Match.away_team.has(name=team))
        )
    if round:
        q = q.filter(Match.round_name == round)

    return [match_to_out(m) for m in q.order_by(Match.date, Match.time).all()]


@router.get("/{match_id}", response_model=MatchOut)
def get_match(match_id: int, db: Session = Depends(get_db)):
    m = (
        db.query(Match)
        .options(
            joinedload(Match.home_team),
            joinedload(Match.away_team),
            joinedload(Match.stadium_rel),
            joinedload(Match.goals),
        )
        .filter(Match.id == match_id)
        .first()
    )
    if not m:
        raise HTTPException(status_code=404, detail="Match not found")
    return match_to_out(m)
