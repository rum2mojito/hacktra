class resouce:
  def __init__(self, lumber=0, clay=0, iron=0, crop=0):
    self.lumber = lumber
    self.clay = clay
    self.iron = iron
    self.crop = crop

  def updateResource(self, lumber=0, clay=0, iron=0, crop=0):
    self.lumber = lumber
    self.clay = clay
    self.iron = iron
    self.crop = crop
    
  def getResource(self):
    return [self.lumber, self.clay, self.iron, self.crop]