import os
import sys
from sqlalchemy.orm import declarative_base, Mapped, mapped_column, relationship
from sqlalchemy import create_engine, String, ForeignKey
from eralchemy2 import render_er

Base = declarative_base()

class Users(Base):
    __tablename__ = 'users'
    id: Mapped[int] = mapped_column(primary_key=True)
    nameuser: Mapped[str] = mapped_column(nullable=False)
    email: Mapped[str] = mapped_column(nullable=False)
    password: Mapped[str] = mapped_column(nullable=False)
    favorites: Mapped[list["Favorites"]] = relationship(back_populates="users")

class People(Base):
    __tablename__ = 'people'
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(nullable=False)
    birth_year: Mapped[int] = mapped_column(nullable=False)
    mass: Mapped[float] = mapped_column(nullable=False)
    favorites: Mapped[list["Favorites"]] = relationship(back_populates="people")

class Planets(Base):
    __tablename__ = 'planets'
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(nullable=False)
    diameter: Mapped[int] = mapped_column(nullable=False)
    population: Mapped[int] = mapped_column(nullable=False)
    favorites: Mapped[list["Favorites"]] = relationship(back_populates="planets")

class Starships(Base):
    __tablename__ = 'starships'
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(nullable=False)
    model: Mapped[str] = mapped_column(nullable=False)
    passengers: Mapped[int] = mapped_column(nullable=False)
    favorites: Mapped[list["Favorites"]] = relationship(back_populates="starships")
    
class Favorites(Base):
    __tablename__ = "favorites"
    people_id: Mapped[int] = mapped_column(ForeignKey("people.id"), primary_key=True)
    planets_id: Mapped[int] = mapped_column(ForeignKey("planets.id"), primary_key=True, nullable=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"), primary_key=True)
    starships_id: Mapped[int] = mapped_column(ForeignKey("starships.id"), primary_key=True)

    # Relaciones con las tablas principales
    people: Mapped["People"] = relationship(back_populates="favorites")
    planets: Mapped["Planets"] = relationship(back_populates="favorites")
    user: Mapped["Users"] = relationship(back_populates="favorites")
    starships: Mapped["Starships"] = relationship(back_populates="favorites")


    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
