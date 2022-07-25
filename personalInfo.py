class PersonalInfo :

    def __init__(self,name: str, id: str,phone_number: str, email: str):
        """
        Constructor
        :param name:
        :param id:
        :param phone_number:
        :param email:
        """
        self.name = name
        self.id = id
        self.phone = phone_number
        self.email = email

    def __str__(self):
        """
        to String
        :return: str of object
        """
        return f"Name : {self.name}, Id : {self.id}," \
               f" Phone Number : {self.phone}, email : {self.email}"



