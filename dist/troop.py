class troop:
  def __init__(self, race, name, resLumber, resClay, resIron, resCrop, xCropRes, resTime,
               trainLumber, trainClay, trainIron, trainCrop, xCropTrain, trainTime, velocity, carry,
               level, needLumber, needClay, needIron, needCrop, trainTimeLevel1, trainTimeLevel20, attack, infantry, cavalry):
    self.race = race
    self.name = name
    #Table1 Research
    self.resLumber = resLumber
    self.resClay = resClay
    self.resIron = resIron
    self.resCrop = resCrop
    self.xCropRes = xCropRes
    self.resTime = resTime
    #Table1 Training
    self.trainLumber = trainLumber
    self.trainClay = trainClay
    self.trainIron = trainIron
    self.trainCrop = trainCrop
    self.xCropTrain = xCropTrain
    self.trainTime = trainTime
    #Table1 Velocity & Carry
    self.velocity = velocity
    self.carry = carry
    #Table2
    self.level = level
    self.needLumber = needLumber
    self.needClay = needClay
    self.needIron = needIron
    self.needCrop = needCrop
    self.trainTimeL1 = trainTimeLevel1
    self.trainTimeL2 = trainTimeLevel20
    # ATTACK & DEFENSE
    self.attack = attack
    self.infantry = infantry
    self.cavalry = cavalry

  def train(self, number, lumber, clay, iron, crop):
    if (self.lumber*number >= lumber and self.clay*number >= clay and
        self.iron*number >= iron and self.crop*number >= crop):
      return True
    return False