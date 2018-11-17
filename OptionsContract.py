class OptionsContract:
  def init (self,callOrPut,ticker,strikePrice,contractPrice,underlyingPrice,theta,delta,daysToExpiration):
    self.callOrPut = callOrPut
      #please add these for each variable..
    
  def quote(self):
    print("This is a $" + str(self.strikePrice))+" "+self.callOrPut+" for $"+self.ticker+".")
    print(self.ticker+" currently trades at $"+str(self.underlyingPrice)+" per share, and the contract is worth $"+str(self.contractPrice)+".")
    print("The option expires in "+str(self.daysToExpiration)+" days.")

  
  def birthday(self):
    self.birthday = self.birthday + 1
  
  def playFetch(self,numGames): 
    self.gamesFetch = self.gamesFetch + numGames
