from pydantic import BaseModel, ConfigDict


class TeamOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    name: str
    group_letter: str
    flag: str


class StadiumOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    name: str
    city: str
    country: str


class GoalOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    match_id: int
    team_id: int
    scorer: str
    minute: str
    penalty: bool
    own_goal: bool


class MatchOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    round_name: str
    date: str
    time: str
    team1: TeamOut | None
    team2: TeamOut | None
    score_ft_home: int | None
    score_ft_away: int | None
    score_ht_home: int | None
    score_ht_away: int | None
    group_name: str | None
    stadium: StadiumOut | None
    knockout: bool
    winner: TeamOut | None
    played: bool
    goals: list[GoalOut]


class GroupStandingOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    position: int
    team: TeamOut
    played: int
    won: int
    drawn: int
    lost: int
    goals_for: int
    goals_against: int
    goal_diff: int
    points: int


class GroupOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    letter: str
    standings: list[GroupStandingOut]


class ScorerOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    team: TeamOut
    player: str
    goals: int
