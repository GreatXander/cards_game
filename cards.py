import os

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

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
    self.confirmazo = 'mazo1'
    
    return 'Player 1 is: ' + self.name, game.mazoplayer1
  
  def setplayer2(self, mazo):
    
    player.player2 = self.name
    player.mazoplayer2 = self.barajasplayer2[mazo]
    self.confirmazo = 'mazo2'

    return 'Player 2 is: ' + self.name, game.mazoplayer2

class game(player):
  playerturn = None
  cardfrompackage = None
  packagenumber = 0
  cardtotake = None
  taked1 = False
  taked2 = False

  @staticmethod
  def startgame(startplayer, cardtotake):

    if str(cardtotake) in game.cards and startplayer == 1:
      game.playerturn = 1

      print 'Player 1: ' + game.player1, game.mazoplayer1
      print ''
      
      print '      Package: ' + '[?]' + '     Take:' + str([cardtotake])
      print ''
      
      return 'Player 2: ' + game.player2, ['?', '?', '?', '?', '?']
    
    if str(cardtotake) in game.cards and startplayer == 2:
      game.playerturn = 2

      print 'Player 1: ' + game.player1, ['?', '?', '?', '?', '?']
      print ''
      
      print '      Package: ' + '[?]' + '     Take:' + str([cardtotake])
      print ''
      
      return 'Player 2: ' + game.player2, game.mazoplayer2
    
    if str(cardtotake) not in game.cards and startplayer == 1 or str(cardtotake) not in game.cards and startplayer == 2:
      return 'Choose a valid card to show'
    
    if str(cardtotake) in game.cards and startplayer < 1 or str(cardtotake) in game.cards and startplayer > 2:
      return 'Choose a valid player to start'
    
    if str(cardtotake) not in game.cards and startplayer > 2 or  str(cardtotake) not in game.cards and startplayer < 1:
      return 'Choose a valid player to start and a valid card to show'
  
  @property
  def takefrompackage(self):
    if len(game.mazoplayer1) > 5:
      return 'You have 6 cards!, you must leave one!'
    else:
      
      if game.playerturn == 1 and self.confirmazo == 'mazo1' and game.taked1 == False:
        game.packagenumber += 1
        game.playerturn = 1
        game.taked1 = True
        game.cardfrompackage = game.cards[game.packagenumber-1]
        print ''
        print self.name + ' takes from package!'
        return 'The card is: ' + str(game.cardfrompackage) + ',' + ' you must take it or leave it!'
      
      if game.playerturn == 1 and self.confirmazo == 'mazo1' and game.taked1 == True:
        print ''
        return game.player1 + ' you already took one!'

      if game.playerturn == 2 and self.confirmazo == 'mazo2' and game.taked2 == False:
        game.packagenumber += 1
        game.playerturn = 2
        game.taked2 = True
        game.cardfrompackage = game.cards[game.packagenumber-1]
        print ''
        print self.name + ' takes from package!'
        return 'The card is: ' + str(game.cardfrompackage) + ',' + ' you must take it or leave it!'
      
      if game.playerturn == 2 and self.confirmazo == 'mazo2' and game.taked2 == True:
        print ''
        return game.player2 + ' you already took one!'
          
      if game.playerturn == 1 and self.confirmazo == 'mazo2':
        print ''
        return 'Is the turn of ' + game.player1 + '!'
            
      if game.playerturn == 2 and self.confirmazo == 'mazo1':
        print ''
        return 'Is the turn of ' + game.player2 + '!'
  
  @property
  def take(self):  
    if game.playerturn == 1 and self.confirmazo == 'mazo1' and len(game.mazoplayer1) < 6:
      game.mazoplayer1.append(game.cardfrompackage)
      cls()
      print "You can't take more cards and have to leave 1!"
      print ''
      return game.startgame(game.playerturn, 'J')
    
    if game.playerturn == 2 and self.confirmazo == 'mazo2' and len(game.mazoplayer2):

      game.mazoplayer2.append(game.cardfrompackage)
      cls()
      print game.startgame(game.playerturn, 'J')
      print ''
      return "You can't take more cards and have to leave 1!"

    if game.playerturn == 1 and self.confirmazo == 'mazo2':
      print ''
      return 'Is not your turn ' + game.player2 + '!'
    
    if game.playerturn == 2 and self.confirmazo == 'mazo1':
      print ''
      return 'Is not your turn ' + game.player1 + '!'