class player:
  
  cards = ['A', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
  
  mazosplayer1 = [cards[0:2] + cards[11:-1] + cards[4:5], cards[3:6] + cards[7:9], cards[5:7] + cards[0:1] + cards[8:10]]
  
  mazosplayer2 = [cards[2:4] + cards[6:7] + cards[6:8], cards[9:12] + cards[1:3], cards[7:9] + cards[2:3] + cards[10:12]]

  def __init__(self, name, mazo):
    self.name = name
    self.mazo = mazo
    print 'Registered player ' + self.name + '! ' + 'set your player to play!'
  
  @property
  def setplayer(self):
    qty_players = 0
    self.playercards = []
    
    if qty_players == 0:
      self.playercards = self.mazosplayer1[self.mazo]
      qty_players+= 1
      print qty_players
      return 'Player ' + str(qty_players) + ' is: ' + self.name, self.playercards

  
    if qty_players == 1:
      self.cards = self.mazosplayer2[self.mazo]
      qty_players+= 1
      return 'Player ' + str(qty_players) + ' is: ' + self.name, self.playercards
    
    else:

      return 'There are already two players!'