class troop:
  def __init__(self, race, name, needLumber, needClay,
               needIron, needCrop, trainTime, velocity, carry):
    self.race = race
    self.name = name
    self.lumber = needLumber
    self.clay = needClay
    self.iron = needIron
    self.crop = needCrop
    self.train = trainTime
    self.velocity = velocity
    self.carry = carry

  def train(self, number, lumber, clay, iron, crop):
    if (self.lumber*number >= lumber and self.clay*number >= clay and
        self.iron*number >= iron and self.crop*number >= crop):
      return True
    return False