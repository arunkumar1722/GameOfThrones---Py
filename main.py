# Main Class
from gameofthrones.gameofthroneshouse import GameOfThronesHouse

class Main:
  # House Lannister
  house_lannister = GameOfThronesHouse('Lannister', 'Lion', 'Hear me roar!', 'Tywin Lannister')
  house_lannister.get_characteristics()
  # House Stark
  house_stark = GameOfThronesHouse('Stark', 'Wolf', 'Winter is Coming!', 'Ned Stark')
  house_stark.get_characteristics()
  # Update Lannister Head
  house_lannister.update_head('Jamie Lannister')
  house_lannister.get_characteristics()