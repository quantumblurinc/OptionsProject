class Dog:
  def init (self,name,age,gamesFetch):
    self.name = name
    self.age = age
    self.gamesFetch = gamesFetch
    
  def whoIs(self):
    print("Name: " + self.name)
    print("Age: " + str(self.age))
    print("Games of Fetch Played: " + str(self.gamesFetch))
  
  def birthday(self):
    self.birthday = self.birthday + 1
  
  def playFetch(self,numGames): 
    self.gamesFetch = self.gamesFetch + numGames
