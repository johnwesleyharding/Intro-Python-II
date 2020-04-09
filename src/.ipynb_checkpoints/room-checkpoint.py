# Implement a class to hold room information. This should have name and
# description attributes.

class Room:

    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.n_to = None
        self.e_to = None
        self.s_to = None
        self.w_to = None
        self.items = []

#     def n_to(self, connection):
#         self.north = connection

#     def e_to(self, connection):
#         self.east = connection

#     def s_to(self, connection):
#         self.south = connection

#     def w_to(self, connection):
#         self.west = connection
