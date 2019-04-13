from sqlalchemy import Column, ForeignKey, Integer, String, Boolean, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from configr import Configr

Base = declarative_base()


class Schedule(Base):
    """
    Table that hold the schedule/assignments

    .. WARNING:: Needs testing.
    """
    __tablename__ = 'schedule'

    id = Column(Integer, primary_key=True)
    speaker = Column(Integer, ForeignKey('speaker.id'), nullable=False)
    outline = Column(Integer, ForeignKey('outline.id'), nullable=False)
    congregation = Column(Integer, ForeignKey('congregation.id'), nullable=False)
    chairman = Column(Integer, ForeignKey('speaker.id'), nullable=False)
    hospitality = Column(Integer, ForeignKey('hospitality.id'), nullable=False)
    date = Column(Date, nullable=False)


class Speaker(Base):
    """
    Table that holds the information for the speakers.
    """
    __tablename__ = 'speaker'

    id = Column(Integer, primary_key=True)
    first_name = Column(String(250), nullable=False)
    middle_name = Column(String(250), nullable=True)
    last_name = Column(String(250), nullable=False)
    email = Column(String(250), nullable=True)
    phone1 = Column(String(20), nullable=False)
    phone2 = Column(String(20), nullable=True)
    congregation = Column(Integer, ForeignKey('congregation.id'), nullable=False)
    responsibility = Column(String(20), nullable=False)
    speaker = Column(Boolean, nullable=False, default=False)
    chairman = Column(Boolean, nullable=False, default=False)
    coordinator = Column(Boolean, nullable=False, default=False)
    note = Column(String(250), nullable=True)
    visibility = Column(Boolean, nullable=False, default=True)


class Congregation(Base):

    __tablename__ = 'congregation'

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    phone = Column(String(20), nullable=False)
    email = Column(String(250), nullable=True)
    street = Column(String(250), nullable=False)
    city = Column(String(20), nullable=False)
    state = Column(String(20), nullable=False)
    zipcode = Column(Integer, nullable=False)
    week = Column(String(20), nullable=False)
    time = Column(String(20), nullable=False)
    note = Column(String(250), nullable=True)
    visibility = Column(Boolean, nullable=False, default=True)


class Hospitality(Base):
    """Hospitality class"""
    __tablename__ = 'hospitality'

    id = Column(Integer, primary_key=True)
    group = Column(String(250), nullable=False)
    note = Column(String(250), nullable=True)


class Outline(Base):
    """Table holding all of the outlines."""
    __tablename__ = 'outline'
    id = Column(Integer, primary_key=True)
    number = Column(String(16), nullable=False)
    title = Column(String(250), nullable=False)
    visibility = Column(Boolean, nullable=False, default=True)


class SpeakOut(Base):
    """Association between speaker and outline"""
    __tablename__ = 'speakout'

    id = Column(Integer, primary_key=True)
    outline = Column(Integer, ForeignKey('outline.id'))
    speaker = Column(Integer, ForeignKey('speaker.id'))


if __name__ == '__main__':
    print(f'{__name__} is not a script.')
