# Class for Game of Thrones Great Houses
class GameOfThronesHouse:
  def __init__(self, name, sigil, motto, head):
    # Constructor
    self.name = name
    self.sigil = sigil
    self.motto = motto
    self.head = head
  
  def get_characteristics(self):
    # Retrieve all characteristics of a House
    print("House", self.name, "Characteristics")
    print("Name  : ", self.name)
    print("Sigil : ", self.sigil)
    print("Motto : ", self.motto)
    print("Head  : ", self.head)
    print('***********************')
  
  def update_head(self, head):
    # Update current head of a House
    print("Updated current head of House", self.name)
    self.head = head