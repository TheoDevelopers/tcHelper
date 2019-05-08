Use Cases
=========

Add a Brother
-------------
- **Actor**: End-User
- **Scenario**:
    1. End-User enters all required information to create a new brother.
    2. System confirm all required information was entered.
    3. System save information to the database.
- **Extensions**
    1. Required information is missing.
        a. System notifies End-User to enter required information.
    2. System finds duplicate brother entry.
        a. System finds duplicate brother.
        b. System informs End-User of duplicate brother and show the information for the older brother record.
        c. End-User decides to abort adding new brother or to delete the older brother record.

Edit a Brother
----------------
- **Actor**: End-User
- **Scenario**:
    1. End-User edits a brother.
    2. System confirms required information are included.
    3. System adds updates to the database.
- **Extensions**
    2. Required information is not included.
        a. System notifies End-User to enter required information.

Delete a Brother
----------------
    - **Actor**: End-User
    - **Scenario**:
        1. End-User deletes a brother.
        2. System deletes brother.
    - **Extensions**
        2. System does not really deletes the brother entry.
            a. System updates entry to make viability False
            b. System does not display entries with viability set to False


Open a Database
---------------
- **Actor**: End-User
- **Scenario**:
    1. End-User opens a database.
    2. System opens the database.
    3. System updates configuration file with new path to the database.
- **Extensions**
    2. System opens an invalid or corrupt file/Database
        a. System aborts the opening of the file
        b. System notifies End-User of the problem.

New Database
---------------
- **Actor**: End-User
- **Scenario**:
    1. End-User creates a new database.
    2. End-User decides location of the database
    3. System creates a new database at the location specified by End-user.
    4. System updates configuration file with new location of the database.

Set an Incoming Talk
--------------------
- **Actor**: End-User
- **Scenario**:
    1. End_Use finds brother by searching or looking through brother's congregation list of brothers.
    2. System adds brother, outline, and his from-congregation to the schedule.
    3. System displays updated schedule.
- **Extensions**
    2. Required information is not included.
        a. System notifies End-User to enter required information.

Set Outgoing Talk
-----------------
- **Actor**: End-User
- **Scenario**:
    1. End-Use finds brother by searching or looking through local congregation list of brothers.
    2. System adds brother, outline, and congregation he will travel-to to the schedule.
    3. System displays updated schedule.
- **Extensions**
    2. Brother being scheduled is scheduled for another duty.
        a. System notifies End-User of the problem.
