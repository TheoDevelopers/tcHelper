Requirements
============
The requirements for tcHelper 1.0

Functionality
-------------
The application should ...

database
~~~~~~~~
- allow the user to create or open a database.

brothers
~~~~~~~~
- allow the user to add edit, or delete a brother.
- allow the user to search for brothers within all congregations.
- allow the user to search for brothers within a specific congregation.
- allow the user to sort by first name, last name or responsibility.
- keep track of the following information for each brother:
    - First name
    - Middle name (if applicable)
    - Last name
    - Two phone numbers
    - Email account
    - Congregation belong to
    - Outlines able to give
    - Responsibility (Elder, MS, etc)
    - Notes
- prevent duplicate brothers from being added.

congregations
~~~~~~~~~~~~~
- allow the user to create, edit, delete congregations.
- keep track of the following information for each congregation:
    - Name of congregation
    - Address
    - Email address to the video department (Send scriptures to be used, music to play, etc).
    - Date of the weekly public meetings is held.
    - Time the meeting begins.
- prevent duplicate congregations from being added.

outlines
~~~~~~~~
- allow the user to add, edit, and delete outlines.
- keep track of outlines' ...
    - number
    - title
- prevent user from adding a duplicate outline number and/or title.

schedules
~~~~~~~~~
- allow the user to see, add, edit, remove schedules indefinitely into the future.
- display itself stating with next scheduled talk.
- allow the user to create a schedule of outgoing speakers.
- keep track of the following information:
    - Full name of the speaker
    - The week the speaker will give the talk
    - The outline number and title
    - The congregation the speaker is ...
        - from when giving a talk at their local congregation.
        - going to when giving an outgoing-talk away from the local congregation
    - The group name that is responsible for hospitality
    - Show the stage of request (has the speaker been requested, confirmed, reminded)
- allow the user to set the stage of the request:
    - requested
    - confirmed
    - reminded
- allow hospitality to be set to none on special occasions.
- take into account dates that meetings are canceled or special occasions such as ...
    - assemblies
    - conventions
    - circuit overseer's visit
    - user defined
- prevent the end user from giving the same brother two assignments on the same day.

hospitality
~~~~~~~~~~~
- allow the user to create hospitality groups.
- prevent the user from creating duplicate groups.

chairmanship
~~~~~~~~~~~~
- allow the user to select which local brothers can serve as chairman.

local speakers
~~~~~~~~~~~~~~
- allow the user to select which local brothers can serve as a speaker.

documents
~~~~~~~~~
- allow the creation of a schedule that can be posted on the builtin board at the local congregation.

Non Functional Requirements
---------------------------
The application should be ...

- well documented.
- well tested.
- intuitive and obvious to used.
- have documentation for the end user.

Design & Implementation
-----------------------
- **Database**: SQLite via SQLAlchemy
- **GUI**: Qt via PySide2
- **Programming Language**: Python 3.7+
