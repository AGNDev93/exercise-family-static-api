
"""
update this file to implement the following already declared methods:
- add_member: Should add a member to the self._members list
- delete_member: Should delete a member from the self._members list
- update_member: Should update a member from the self._members list
- get_member: Should return a member from the self._members list
"""
from random import randint

class FamilyStructure:
    def __init__(self, last_name):
        self.last_name = last_name
        self._next_id += 0

        # example list of members
        self._members = []

    # read-only: Use this method to generate random members ID's when adding members into the list
    def _generateId(self):

        generated_id = self._next_id
        self._next_id += 1
        return generated_id

        return randint(0, 99999999)

    def add_member(self, member):
        # fill this method and update the return
        if member["age"]<=0:
            print("La edad debe ser un número mayor que cero")
            return False
        self._generateId()
        member["id"]=self._next_id
        member["last_name"]=self.last_name
        self._members.append(member)
        return True

    def delete_member(self, id):
        # fill this method and update the return
        pass

    def get_member(self, id):
        # fill this method and update the return
        pass

    # this method is done, it returns a list with all the family members
    def get_all_members(self):
        return self._members
