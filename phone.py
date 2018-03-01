class Phone:
    """class holding Phones' methods."""
    def __init__(self):
        # super(Phone, self).__init__()
        self.contact = {}

    def create_contact(self, name, number):
        """method for create_contact."""

        cont = {}
        cont[name] = number

        if bool(name and number):
            if isinstance(name, str) and isinstance(number, int):
                if number not in self.contact.values() and name not in self.contact.keys():
                    self.contact.update({name:number})
                    return {'message':'contact added successfully'}
                return {'message':'contact already exists'}
            return 'invalid input'
        return {'message':'you must enter BOTH number and name'}


        # self.contact.update({name:number})
        # print self.contact
