from sqlalchemy import Column, ForeignKey, Integer, String, Boolean, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from config import Config


db_location = Config()
file_location = db_location.getValue('DB', 'location')

# engine = create_engine(f"sqlite:///{db_location}", echo=True)


engine = create_engine(f'sqlite:///{file_location}', echo=True)
Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()


class Schedule(Base):
    """
    The model for the *schedule* table in the database.
    """
    __tablename__ = 'schedule'

    id = Column(Integer, primary_key=True)
    """Primary key for the *schedule* table. (int)"""

    brother = Column(Integer, ForeignKey('brother.id'), nullable=False)
    """Foreign key of the brother (int)"""

    outline = Column(Integer, ForeignKey('outline.id'), nullable=False)
    """Foreign key of the outline to be given. (int)"""

    congregation = Column(Integer, ForeignKey('congregation.id'), nullable=False)
    """Foreign key of the congregation of the speaker coming or going to give the talk. (int)"""

    chairman = Column(Integer, ForeignKey('brother.id'), nullable=False)
    """Foreign key for the chairman. (int)"""

    hospitality = Column(Integer, ForeignKey('hospitality.id'), nullable=False)
    """Foreign ket for the group that has hospitality. (int)"""

    date = Column(Date, nullable=False)
    """Date of the schedule.
    (`date <https://docs.sqlalchemy.org/en/latest/core/type_basics.html#sqlalchemy.types.Date>`_)"""


class Brother(Base):
    """
    The model for the *brother* table in the database.
    """
    __tablename__ = 'brother'

    id = Column(Integer, primary_key=True)
    """Primary key (int)"""

    first_name = Column(String(250), nullable=False)
    """The first name of the brother. (string)"""

    middle_name = Column(String(250), nullable=True)
    """Optinal field for the brother's middle name if applicable."""

    last_name = Column(String(250), nullable=False)
    """The last name of the brother. (string)"""

    email = Column(String(250), nullable=True)
    """The email address of the brother. (string)"""

    phone1 = Column(String(20), nullable=False)
    """
    The primary phone number associated with the brother. This field is a string because some
    people like to enter phone numbers in variouse formats such as *555-555-5555* so a string
    field would be more flexable. (string)
    """

    phone2 = Column(String(20), nullable=True)
    """Secendary phone number for the brother. Not required. (string)"""

    congregation = Column(Integer, ForeignKey('congregation.id'), nullable=False)
    """Foreign key of the congregation the brother belongs to. (int)"""

    responsibility = Column(String(20), nullable=False)
    """The responsibility the brother currently has. ie: `Elder, Ministerial Servant, Publisher` (string)"""

    speaker = Column(Boolean, nullable=False, default=False)
    """
    If the brother is approved for giving talks, either local and/or outgoing, this field will be
    *True* otherwise it will be *False* if brother is not approved for talks. (boolean)
    """

    chairman = Column(Boolean, nullable=False, default=False)
    """If the brother is approved to be chairman, this field will be *True* otherwise *False*. (boolean)"""

    coordinator = Column(Boolean, nullable=False, default=False)
    """This field will be *True* if the brother is the coordinator of the congregation, otherwise *False*. (boolean)"""

    note = Column(String(250), nullable=True)
    """Notes for the brother. (string)"""

    visibility = Column(Boolean, nullable=False, default=True)
    """*False* if the brother has been deleted, otherwise *True*. (boolean)"""


class Congregation(Base):
    """
    The model for the *congregation* table in the database.
    """

    __tablename__ = 'congregation'

    id = Column(Integer, primary_key=True)
    """Primary key for the congregation table. (int)"""

    name = Column(String(250), nullable=False)
    """The name of the congregation. (string)"""

    phone = Column(String(20), nullable=False)
    """The phone number for the congregation. (string)"""

    email = Column(String(250), nullable=True)
    """
    .. note:: The ability to have an email address for the congregation PTC & an email address for emailing scriptures and/or pictures in the near future.
    The email address for the congregation.

    This might be the email address for the PTC or the email address used to email scriptures or
    images for the talks. (string)
    """

    street = Column(String(250), nullable=False)
    """The street address for the Kingdom hall where the congregation meets. (string)"""

    city = Column(String(20), nullable=False)
    """The city for the Kingdom hall where the congregation meets. (string)"""

    state = Column(String(20), nullable=False)
    """The state for the kingdom hall where the congregation meets. (string)"""

    zipcode = Column(Integer, nullable=False)
    """The zipcode for the kingdom hall where the congregation meets. (string)"""

    week = Column(String(20), nullable=False)
    """
    The weekend that the congregation meets for their meets.
    .. Note:: May change var name to *weekend*. (string)
    """

    time = Column(String(20), nullable=False)
    """The time the meeting begins. (string)"""

    note = Column(String(250), nullable=True)
    """Notes for the congregation. (string)"""

    visibility = Column(Boolean, nullable=False, default=True)
    """*False* if the congregation has been deleted, otherwise *True*. (boolean)"""


class Hospitality(Base):
    """
    The model for the *hospitality* table in the database.
    """
    __tablename__ = 'hospitality'

    id = Column(Integer, primary_key=True)
    """Primary key for the hospitality table. (int)"""

    name = Column(String(250), nullable=False)
    """The name of the hospitality group. (string)"""

    note = Column(String(250), nullable=True)
    """Notes for the hospitality group. (string)"""

    visibility = Column(Boolean, nullable=False, default=True)
    """*False* if the hospitality group has been deleted, otherwise *True*. (boolean)"""


class Outline(Base):
    """
    The model for the *congregation* table in the database.
    """
    __tablename__ = 'outline'

    id = Column(Integer, primary_key=True)
    """Primary key for the outline table . (int)"""

    number = Column(String(16), nullable=False)
    """The number that coresponds to the outline title. This number can be found on the outline
        list. The reason this field is a string is due to the fact some special outlines have a letter prefix
        before the number. (string)
    """

    title = Column(String(250), nullable=False)
    """The title of the outline. (string)"""

    visibility = Column(Boolean, nullable=False, default=True)
    """*False* if the outline has been deleted, otherwise *True*. (boolean)"""


class SpeakerOut(Base):
    """
    The model for the *speakerOut* table in the database.

    This is a relational table associating outgoing speakers and outlines.

    .. warning:: This table is not finished. Columns such as date may be added in the future.
    """
    __tablename__ = 'speakerOut'

    id = Column(Integer, primary_key=True)
    """Primary key for the speakerOut table. (int)"""

    outline = Column(Integer, ForeignKey('outline.id'))
    """Foreign key of the outline outgoing brother will be giving. (int)"""

    brother = Column(Integer, ForeignKey('brother.id'))
    """Foreign key of the brother who will be going out to give the talk. (int)"""


class DB:
    """
    Initialize a new database
    """

    @staticmethod
    def dbFile():
        """
        Returns the location of the database as recorded in the config.ini file.

        :return: The location of the database file
        :rtype: str
        """

        confgiFile = Config()
        return confgiFile.getValue('DB', 'location')

    def initDB(self):
        """
        Sets up the new Database.

        Takes the location of the created database from the config.ini file. It retrieves this location
        by running the method `DB.dbFile()`.

        :param file: The location where the database will be saved to.
        :type file: str
        """

        engine = create_engine(f"sqlite:///{DB.dbFile()}", echo=True)

        global Base
        Base.metadata.create_all(engine)

    def addItem(self, object):
        """
        Adds a record to the database.

        :param object: The table class object to be written
        :type object: object
        """

        self.object = object

        session.add(object)
        session.commit()


if __name__ == '__main__':
    print('This not a script.')
