# Implement a class to hold room information. This should have name and
# description attributes.
class Room:
  def __init__(self, name, description, items):
    self.name = name
    self.description = description
    self.n_to = None
    self.s_to = None
    self.e_to = None
    self.w_to = None
    self.items = []

  def __str__(self):
    output = f'{self.name}: {self.description} \n'
    if self.n_to:
      output += 'To the North is: ' + self.n_to.name + '\n'
    if self.s_to:
      output += 'To the South is: ' + self.s_to.name + '\n'
    if self.e_to:
      output += 'To the East is: ' + self.e_to.name + '\n'
    if self.w_to:
      output += 'To the West is: ' + self.w_to.name + '\n'

    return output

# add items to rooms

