import os

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

######################## PLAYERS SECTION ####################

class player:

  cards = ['A', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
  
  barajasplayer1 = [cards[0:2] + cards[11:13] + cards[4:5], cards[3:6] + cards[7:9], cards[5:7] + cards[0:1] + cards[8:10]]
  
  barajasplayer2 = [cards[2:4] + cards[6:7] + cards[6:8], cards[9:12] + cards[1:3], cards[7:9] + cards[2:3] + cards[10:12]]
  
  player1 = None
  mazoplayer1 = None

  player2 = None
  mazoplayer2 = None

  player_id = 0
  
  def __init__(self, name, mazo):
    player.player_id += 1
    self.name = name
    
    if player.player_id == 1:
      player.player1 = self.name
      player.mazoplayer1 = player.barajasplayer1[mazo]
    
    if player.player_id == 2:
      player.player2 =self.name
      player.mazoplayer2 = player.barajasplayer2[mazo]
    
    if player.player_id > 2:
      print 'In the game must be 2 players!'
    
    self.playerid = player.player_id

########################## GAME SECTION #####################

class game(player):
  playerturn = None
  displayedcard = None

######################### START GAME ########################
  @staticmethod
  def startgame(startplayer, cardtotake):

######################## PLAYER 1 START #####################
    
    if str(cardtotake) in game.cards and startplayer == 1:
      game.playerturn = 1
      game.displayedcard = cardtotake

      print 'Player 1: ' + game.player1, game.mazoplayer1
      print ''
      
      print '      Package: ' + '[?]' + '     Take:' + str([game.displayedcard])
      print ''
      
      return 'Player 2: ' + game.player2, ['?', '?', '?', '?', '?']

####################### PLAYER 2 START ######################    
    
    if str(cardtotake) in game.cards and startplayer == 2:
      game.playerturn = 2
      game.displayedcard = cardtotake

      print 'Player 1: ' + game.player1, ['?', '?', '?', '?', '?']
      print ''
      
      print '      Package: ' + '[?]' + '     Take:' + str(game.displayedcard)
      print ''
      
      return 'Player 2: ' + game.player2, game.mazoplayer2

######################### START EXCEPTIONS ###################
    
    if str(cardtotake) not in game.cards and startplayer == 1 or str(cardtotake) not in game.cards and startplayer == 2:
      
      return 'Choose a valid card to show'
    
    if str(cardtotake) in game.cards and startplayer < 1 or str(cardtotake) in game.cards and startplayer > 2:
      
      return 'Choose a valid player to start'
    
    if str(cardtotake) not in game.cards and startplayer > 2 or  str(cardtotake) not in game.cards and startplayer < 1:
      
      return 'Choose a valid player to start and a valid card to show'

######################### PLAYERS ACTIONS ######################

  playeronetaked = False
  playertwotaked = False

  cardsfrompackage = None
  cardnumber = 0

################### TAKE CARD FROM PACKAGE ###################

  @property
  def takefrompackage(self):
    
    if len(game.mazoplayer1) > 5:
      
      return game.player1 + ' have 6 cards!, must leave one!'
    
    if len(game.mazoplayer2) > 5:
      
      return game.player2 + ' have 6 cards!, must leave one!'
    
    else:
######################## PLAYER 1 TAKES ######################     
      
      if game.playerturn == 1 and self.playerid == 1 and game.playeronetaked == False:
        
        game.cardnumber += 1
        game.playerturn = 1
        game.playeronetaked = True
        game.cardfrompackage = game.cards[game.cardnumber-1]
        
        print ''
        print self.name + ' takes from package!'
        
        return 'The card is: ' + str(game.cardfrompackage) + ',' + ' you must keep it or leave it!'
      
      if game.playerturn == 1 and self.playerid == 1 and game.playeronetaked == True:
        
        print ''
        return game.player1 + ' you already took one!'

########################## PLAYER 2 TAKES #####################

      if game.playerturn == 2 and self.playerid == 2 and game.playertwotaked == False:
        
        game.cardnumber += 1
        game.playerturn = 2
        game.playertwotaked = True
        game.cardfrompackage = game.cards[game.cardnumber-1]
        
        print ''
        print self.name + ' takes from package!'
        
        return 'The card is: ' + str(game.cardfrompackage) + ',' + ' you must keep it or leave it!'
      
      if game.playerturn == 2 and self.playerid == 2 and game.playertwotaked == True:
        
        print ''
        return game.player2 + ' you already took one!'

################### TAKE FROM PACKAGE EXCEPTIONS ################
      
      if game.playerturn == 1 and self.playerid == 2:
        
        print ''
        return 'Is the turn of ' + game.player1 + '!'
            
      if game.playerturn == 2 and self.playerid == 1:
        
        print ''
        return 'Is the turn of ' + game.player2 + '!'

########################## KEEP THE CARD ##########################
  
  @property
  def keep(self):  

######################### PLAYER 1 KEEPS ##########################
    
    if game.playerturn == 1 and self.playerid == 1 and len(game.mazoplayer1) < 6:
      
      game.mazoplayer1.append(game.cardfrompackage)
      
      cls()
      print "You can't take more cards and have to leave 1!"
      print ''
      
      return game.startgame(game.playerturn, game.displayedcard)

######################### PLAYER 2 KEEPS ##########################
    
    if game.playerturn == 2 and self.playerid == 2 and len(game.mazoplayer2) < 6:
      
      game.mazoplayer2.append(game.cardfrompackage)
      
      cls()
      print "You can't take more cards and have to leave 1!"
      print ''
      
      return game.startgame(game.playerturn, game.displayedcard)

####################### KEEP EXCEPTIONS ############################
    
    if game.playerturn == 1 and self.playerid == 2:
      
      print ''
      return 'Is the turn of ' + game.player1 + '!'
    
    if game.playerturn == 2 and self.playerid == 1:
      
      print ''
      return 'Is the turn of ' + game.player2 + '!'