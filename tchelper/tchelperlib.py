class Brother:
    """
    Brother class that defines a person.

    """

    def __init__(self, id, first, middle, last, phone1,
                 congregation, responsibility, speaker,
                 chairman, coordinator, phone2=None,
                 note=None, visibility=True):
        """
        Init the brother object.

        :param id: id for the brother
        :param first: First name of the brother
        :param middle: Middle name of the brother if applicable
        :param last: Last name of the brother
        :param phone1: Primary phone number for the brother
        :param phone2: Optinal second phone number for the brother
        :param congregation: Congregation the brother belongs to
        :param responsibility: The responsibility the brother holds, ie *Elder*, *Ministerial Servant*, *Publisher*
        :param speaker: *True* if the brother has been approved to give local or outgoing talks, otherwise False
        :param chairman: *True* if the brother has been approved to be chairman, otherwise *False*
        :param coordinator: *True* if the brother is coordinator of the congregation, otherwise *False*
        :param note: Notes for the brother
        :param visibility: *False* if the brother has been deleted
        :type id: int
        :type first: str
        :type middle: str
        :type last: str
        :type phone1: str
        :type phone2:str
        :type congregation: int
        :type responsibility: str
        :type speaker: bool
        :type chairman: bool
        :type coordinator: bool
        :type note: str
        :type visibility: bool
        """

        self.id = id
        self.first = first
        self.middle = middle
        self.last = last
        self.phone1 = phone1
        self.phone2 = phone2
        self.congregation = congregation
        self.responsibility = responsibility
        self.speaker = speaker
        self.chairman = chairman
        self.coordinator = coordinator
        self.note = note
        self.visibility = visibility

    def setFullName (self, first, middle, last):
        """
        Sets/change the name of the brother

        :param first: The first name of the brother to be set or changed
        :param middle: The optinal middle name of the brother to be set or changed
        :param last: The last name of the brother to be set or changed
        :type first: str
        :type middle: str
        :type last: str
        """
        self.first = first
        self.middle = middle
        self.last = last

    def setFirstName(self, firstName):
        """
        Sets or changes the first name of the brother

        :param firstName: The first name of the brother to be set or changed
        :type firstName: str
        """

        self.first = firstName

    def setMiddleName(self, middleName):
        """
        Sets or changes the middle name of the brother

        :param middleName: The middle name of the brother to be set or changed
        :type middleName: str
        """

        self.middle = middleName

    def setLastName(self, lastName):
        """
        Sets or changes the last name of the brother

        :param lastName: The last name of the brother to be set or changed
        :type lastName: str
        """
