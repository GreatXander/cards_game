class player:
  
  #####################PLAYERS SECTION###################
  cards = ['A', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
  
  player1 = None
  mazoplayer1 = None
  
  player2 = None
  mazoplayer2 = None

  barajasplayer1 = [cards[0:2] + cards[11:-1] + cards[4:5], cards[3:6] + cards[7:9], cards[5:7] + cards[0:1] + cards[8:10]]
  
  barajasplayer2 = [cards[2:4] + cards[6:7] + cards[6:8], cards[9:12] + cards[1:3], cards[7:9] + cards[2:3] + cards[10:12]]

  def __init__(self, name):
    self.name = name
  
  def setplayer1(self, mazo):
    
    player.player1 = self.name
    player.mazoplayer1 = self.barajasplayer1[mazo]
    self.mazo = self.barajasplayer1[mazo]
    
    return 'Player 1 is: ' + self.name, self.mazo
  
  def setplayer2(self, mazo):
    
    player.player2 = self.name
    player.mazoplayer2 = self.barajasplayer2[mazo]
    self.mazo = self.barajasplayer2[mazo]
    
    return 'Player 2 is: ' + self.name, self.mazo

class game(player):
  packagecard = None
  cardtotake = None

  @staticmethod
  def startgame(startplayer, cardtotake):

    if str(cardtotake) in game.cards and startplayer == 1 or startplayer == 2:
      print 'Player 1: ' + game.player1, game.mazoplayer1
      print ''
      
      print '      Package: ' + '[?]' + '       Take:' + str([cardtotake])
      print ''
      
      return 'Player 2: ' + game.player2, game.mazoplayer2
    
    if str(cardtotake) not in game.cards and startplayer == 1 or str(cardtotake) not in game.cards and startplayer == 2:
      return 'Choose a valid card to show'
    
    if str(cardtotake) in game.cards and startplayer < 1 or str(cardtotake) in game.cards and startplayer > 2:
      return 'Choose a valid player to start'
    
    if str(cardtotake) not in game.cards and startplayer > 2 or  str(cardtotake) not in game.cards and startplayer < 1:
      return 'Choose a valid player to start and a valid card to show'