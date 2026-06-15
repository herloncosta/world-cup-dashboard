import re
import httpx
from sqlalchemy.orm import Session
from database import SessionLocal, engine, Base
from models import Team, Stadium, Match, Goal

DATA_URL = "https://raw.githubusercontent.com/openfootball/worldcup.json/master/2026/worldcup.json"

STADIUM_MAP = {
    "Mexico City": ("Estadio Azteca", "Mexico City", "Mexico"),
    "Guadalajara (Zapopan)": ("Estadio Akron", "Guadalajara", "Mexico"),
    "Monterrey (Guadalupe)": ("Estadio BBVA", "Monterrey", "Mexico"),
    "Atlanta": ("Mercedes-Benz Stadium", "Atlanta", "USA"),
    "Boston (Foxborough)": ("Gillette Stadium", "Boston", "USA"),
    "Dallas (Arlington)": ("AT&T Stadium", "Dallas", "USA"),
    "Houston": ("NRG Stadium", "Houston", "USA"),
    "Kansas City": ("Arrowhead Stadium", "Kansas City", "USA"),
    "Los Angeles (Inglewood)": ("SoFi Stadium", "Los Angeles", "USA"),
    "Miami (Miami Gardens)": ("Hard Rock Stadium", "Miami", "USA"),
    "New York/New Jersey (East Rutherford)": ("MetLife Stadium", "New York", "USA"),
    "Philadelphia": ("Lincoln Financial Field", "Philadelphia", "USA"),
    "San Francisco Bay Area (Santa Clara)": ("Levi's Stadium", "San Francisco", "USA"),
    "Seattle": ("Lumen Field", "Seattle", "USA"),
    "Toronto": ("BMO Field", "Toronto", "Canada"),
    "Vancouver": ("BC Place", "Vancouver", "Canada"),
}


def seed():
    Base.metadata.create_all(bind=engine)
    db = SessionLocal()

    if db.query(Team).count() > 0:
        print("Database already seeded. Skipping.")
        db.close()
        return

    resp = httpx.get(DATA_URL, timeout=30)
    resp.raise_for_status()
    data = resp.json()

    team_names: set[str] = set()
    group_map: dict[str, str] = {}
    stadium_keys: set[str] = set()

    for m in data["matches"]:
        team_names.add(m["team1"])
        team_names.add(m["team2"])
        if m.get("group"):
            group_map[m["team1"]] = m["group"]
            group_map[m["team2"]] = m["group"]
        if m.get("ground"):
            stadium_keys.add(m["ground"])

    stadium_objs: dict[str, Stadium] = {}
    for key in sorted(stadium_keys):
        info = STADIUM_MAP.get(key, (key, "", ""))
        obj = Stadium(name=info[0], city=info[1], country=info[2])
        db.add(obj)
        db.flush()
        stadium_objs[key] = obj

    def is_placeholder(name: str) -> bool:
        return bool(re.match(r'^[0-9A-Z/]+$', name)) and name != "USA"

    team_objs: dict[str, Team] = {}
    for name in sorted(team_names):
        group_letter = ""
        if name in group_map:
            group_letter = group_map[name].replace("Group ", "")
        obj = Team(name=name, group_letter=group_letter, placeholder=is_placeholder(name))
        db.add(obj)
        db.flush()
        team_objs[name] = obj

    for m in data["matches"]:
        t1 = team_objs[m["team1"]]
        t2 = team_objs[m["team2"]]

        ft = m.get("score", {}).get("ft") if m.get("score") else None
        ht = m.get("score", {}).get("ht") if m.get("score") else None

        stadium = stadium_objs.get(m.get("ground", ""))

        match_obj = Match(
            round_name=m.get("round", ""),
            date=m.get("date", ""),
            time=m.get("time", ""),
            team1_id=t1.id,
            team2_id=t2.id,
            score_ft_home=ft[0] if ft else None,
            score_ft_away=ft[1] if ft else None,
            score_ht_home=ht[0] if ht else None,
            score_ht_away=ht[1] if ht else None,
            group_name=m.get("group"),
            stadium_id=stadium.id if stadium else None,
            knockout=m.get("round", "").lower() not in ("matchday 1", "matchday 2", "matchday 3", "matchday 4", "matchday 5", "matchday 6", "matchday 7", "matchday 8", "matchday 9", "matchday 10", "matchday 11", "matchday 12", "matchday 13", "matchday 14", "matchday 15"),
            played=ft is not None,
        )
        db.add(match_obj)
        db.flush()

        if ft is not None:
            match_obj.winner_id = t1.id if ft[0] > ft[1] else t2.id if ft[1] > ft[0] else None

        goals1 = m.get("goals1", [])
        goals2 = m.get("goals2", [])
        for g in goals1:
            db.add(Goal(match_id=match_obj.id, team_id=t1.id, scorer=g["name"], minute=g.get("minute", ""), penalty=g.get("penalty", False), own_goal=g.get("owngoal", False)))
        for g in goals2:
            db.add(Goal(match_id=match_obj.id, team_id=t2.id, scorer=g["name"], minute=g.get("minute", ""), penalty=g.get("penalty", False), own_goal=g.get("owngoal", False)))

    real_count = sum(1 for t in team_objs.values() if not t.placeholder)
    db.commit()
    db.close()
    print(f"Seeded {real_count} real teams (+{len(team_names) - real_count} placeholders), {len(stadium_keys)} stadiums, {len(data['matches'])} matches")


if __name__ == "__main__":
    seed()
