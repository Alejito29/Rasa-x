import os
from numbers import Number

import sqlalchemy as sa
from sqlalchemy import Column, Integer, String, DateTime, REAL, ForeignKey, Boolean
from sqlalchemy.orm import Session, sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.engine.base import Engine
from typing import Dict, Text, List, Union, Optional
import pytz

utc = pytz.UTC

GENERAL_ACCOUNTS = {
    "recipient": [
        "katy parrow"
    ],
    "vendor": ["target", "starbucks", "amazon"],
    "depositor": ["interest", "employer"],
}

ACCOUNT_NUMBER_LENGTH = 12
CREDIT_CARD_NUMBER_LENGTH = 14

Base = declarative_base()


class RESERVATION(Base):
    """Accounts table.
    `session_id` is only meaningful for accounts generated by conversation sessions,
    when it is equal to `tracker.sender_id`.
    Since `id` autoincrements, it is used to generate unique account numbers by
    adding leading zeros to it.
    """

    __tablename__ = "reservation"
    id = Column(Integer, primary_key=True, autoincrement=True)
    ID_USER = Column(
        Integer
    )
    PHONES = Column(String(255))
    ID_NIIF = Column(
        Integer
    )
    ROOMS = Column(Integer)
    TICKET = Column(Integer)


class USER(Base):
    """Credit cards table. `account_id` is an `Account.id`"""

    __tablename__ = "user"
    id = Column(Integer, primary_key=True, autoincrement=True)
    NAME = Column(String(255))
    LAST_NAME = Column(String(255))


class ROOM(Base):
    """Credit cards table. `account_id` is an `Account.id`"""

    __tablename__ = "room"
    id = Column(Integer, primary_key=True, autoincrement=True)
    ROOM_NUMBER = Column(String(255))
    KIND_OF_ROOM = Column(String(255))
    ROOM_STATE = Column(String(255))
    TICKET_RESERVATION = Column(Integer)


class GASTO(Base):
    """Credit cards table. `account_id` is an `Account.id`"""

    __tablename__ = "gasto"
    id = Column(Integer, primary_key=True, autoincrement=True)
    DESCRIPTION = Column(String(255))
    VALOR = Column(Integer)
    TICKET = Column(Integer)


class NIIF(Base):
    """Transactions table. `to/from_acount_number` are `Account.id`s with leading zeros"""

    __tablename__ = "niif"
    id = Column(Integer, primary_key=True, autoincrement=True)
    DESCRIPTION = Column(String(255))
    NIIF = Column(String(255))


def create_database(database_engine: Engine, database_name: Text):
    """Try to connect to the database. Create it if it does not exist"""
    try:
        database_engine.connect()
    except sa.exc.OperationalError:
        default_db_url = f"sqlite:///{database_name}.db"
        default_engine = sa.create_engine(default_db_url)
        conn = default_engine.connect()
        conn.execute("commit")
        conn.execute(f"CREATE DATABASE {database_name}")
        conn.close()


def getInitDatabase():
    return []


class ProfileDB:
    def __init__(self, db_engine: Engine):
        self.engine = db_engine
        self.create_tables()
        self.session = self.get_session()

    def get_session(self) -> Session:
        return sessionmaker(bind=self.engine)()

    def create_tables(self):
        RESERVATION.__table__.create(self.engine, checkfirst=True)
        USER.__table__.create(self.engine, checkfirst=True)
        NIIF.__table__.create(self.engine, checkfirst=True)
        ROOM.__table__.create(self.engine, checkfirst=True)
        GASTO.__table__.create(self.engine, checkfirst=True)

    def get_user(self, name: str, last_name: str):
        user_search = self.session.query(USER).filter(USER.NAME is name).first()
        return user_search if user_search is not None else None

    def get_all_user(self):
        all_user = self.session.query(USER).all()
        return all_user if all_user is not None else None

    def get_all_niif(self):
        all_user = self.session.query(NIIF).all()
        return all_user if all_user is not None else None

    def get_all_delivery(self):
        delivery = self.session.query(GASTO).all()
        return delivery if delivery is not None else None

    def getNIIF(self, niif: str):
        niif = self.session.query(NIIF).filter(NIIF.NIIF == niif).first()
        return niif if niif is not None else None

    def getReservation(self):
        reservation = self.session.query(RESERVATION).all()
        return reservation if reservation is not None else None

    def get_all_rooms(self):
        rooms = self.session.query(ROOM).all()
        return rooms if rooms is not None else None

    def updateRoom(self, ticket, state_room):
        rooms = self.session.query(ROOM).filter(ROOM.TICKET_RESERVATION == ticket). \
            update({"ROOM_STATE": state_room})
        self.session.commit()
        return rooms if rooms is not None else None

    def get_all_reservation(self):
        reservation = self.session.query(RESERVATION).all()
        return reservation if reservation is not None else None

    def get_all_expense(self):
        gasto = self.session.query(GASTO).all()
        return gasto if gasto is not None else None

    def add_reservation(self, id_user: Integer, phones: str, id_niif: Integer, rooms: Integer, tickets: Integer):
        """Add a new account for a new session_id. Assumes no such account exists yet."""
        self.session.add(RESERVATION(ID_USER=id_user, PHONES=phones, ID_NIIF=id_niif, ROOMS=rooms, TICKET=tickets))
        self.session.commit()

    def add_rooms(self, room_number: str, kind_room: Integer, state: Boolean, ticket: Integer):
        """Add a new account for a new session_id. Assumes no such account exists yet."""
        self.session.add(
            ROOM(ROOM_NUMBER=room_number, KIND_OF_ROOM=kind_room, ROOM_STATE=state, TICKET_RESERVATION=ticket))
        self.session.commit()

    def add_niif(self, description: str, niif: str):
        """Add a new account for a new session_id. Assumes no such account exists yet."""
        self.session.add(NIIF(DESCRIPTION=description, NIIF=niif))
        self.session.commit()

    def add_user(self, name: str, last_name: str):
        """Add a new account for a new session_id. Assumes no such account exists yet."""
        self.session.add(USER(NAME=name, LAST_NAME=last_name))
        self.session.commit()

    def get_init_database(sel):
        print("pruena")
