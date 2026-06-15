from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, JSON
from sqlalchemy.orm import relationship
from database import Base


class Team(Base):
    __tablename__ = "teams"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    group_letter = Column(String)
    flag = Column(String, default="")
    placeholder = Column(Boolean, default=False)

    home_matches = relationship("Match", foreign_keys="Match.team1_id", back_populates="home_team")
    away_matches = relationship("Match", foreign_keys="Match.team2_id", back_populates="away_team")


class Stadium(Base):
    __tablename__ = "stadiums"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True)
    city = Column(String, default="")
    country = Column(String, default="")


class Match(Base):
    __tablename__ = "matches"

    id = Column(Integer, primary_key=True, index=True)
    round_name = Column(String)
    date = Column(String)
    time = Column(String)
    team1_id = Column(Integer, ForeignKey("teams.id"))
    team2_id = Column(Integer, ForeignKey("teams.id"))
    score_ft_home = Column(Integer, nullable=True)
    score_ft_away = Column(Integer, nullable=True)
    score_ht_home = Column(Integer, nullable=True)
    score_ht_away = Column(Integer, nullable=True)
    group_name = Column(String, nullable=True)
    stadium_id = Column(Integer, ForeignKey("stadiums.id"), nullable=True)
    knockout = Column(Boolean, default=False)
    winner_id = Column(Integer, ForeignKey("teams.id"), nullable=True)
    played = Column(Boolean, default=False)

    home_team = relationship("Team", foreign_keys=[team1_id], back_populates="home_matches")
    away_team = relationship("Team", foreign_keys=[team2_id], back_populates="away_matches")
    stadium_rel = relationship("Stadium")
    goals = relationship("Goal", back_populates="match", cascade="all, delete-orphan")


class Goal(Base):
    __tablename__ = "goals"

    id = Column(Integer, primary_key=True, index=True)
    match_id = Column(Integer, ForeignKey("matches.id"))
    team_id = Column(Integer, ForeignKey("teams.id"))
    scorer = Column(String)
    minute = Column(String)
    penalty = Column(Boolean, default=False)
    own_goal = Column(Boolean, default=False)

    match = relationship("Match", back_populates="goals")
