#################### FOR CLEAN COMAND SCREEN #############

import os

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

######################## PLAYERS SECTION ####################

class player:

  cards = ['J', '7', '8', 'Q', '4', '10', '6', '9', '2', '1', '5', 'A', '3', 'K', 'A', '7', '5', '3', '4', 'J', '6', '1', 'Q', '9', 'K', '8', '2', '10', 'Q', '4', '1', '10', '2', 'K', '7', '5', '3', '9', '8', 'A', '6', 'J', '6', 'A', '9', '8', '3', '5', '7', 'K', '2', '10', '1', '4', 'Q', 'J', '?']

################# PLAYERS LIST OF MAZOS (barajas) ############
  
  barajasplayer1 = [cards[0:2] + cards[11:13] + cards[4:5], cards[3:6] + cards[7:9], cards[5:7] + cards[0:1] + cards[8:10]]
  
  barajasplayer2 = [cards[2:4] + cards[6:7] + cards[6:8], cards[9:12] + cards[1:3], cards[7:9] + cards[2:3] + cards[10:12]]

########################### PLAYERS STRUCTURE ###############

  player1 = None
  mazoplayer1 = None

  player2 = None
  mazoplayer2 = None

  player_id = 0

  def __init__(self, name, mazo):
    player.player_id += 1
    self.name = name
    self.taked = False
    self.keep = False

    if player.player_id == 1:
      player.player1 = self.name
      player.mazoplayer1 = player.barajasplayer1[mazo]
    
    if player.player_id == 2:
      player.player2 =self.name
      player.mazoplayer2 = player.barajasplayer2[mazo]
    
    if player.player_id > 2:
      print 'In the game must be 2 players!'
    
    self.playerid = player.player_id

#############################################################

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
      
      print '      Package: ' + '[?]' + '     Displayed: ' + str([game.displayedcard])
      print ''
      
      return 'Player 2: ' + game.player2, ['?', '?', '?', '?', '?']

####################### PLAYER 2 START ######################    
    
    if str(cardtotake) in game.cards and startplayer == 2:
      game.playerturn = 2
      game.displayedcard = cardtotake

      print 'Player 1: ' + game.player1, ['?', '?', '?', '?', '?']
      print ''
      
      print '      Package: ' + '[?]' + '     Displayed: ' + str([game.displayedcard])
      print ''
      
      return 'Player 2: ' + game.player2, game.mazoplayer2

######################### START EXCEPTIONS ###################

############################# CASE 1 ############################

    if str(cardtotake) not in game.cards and startplayer == 1 or str(cardtotake) not in game.cards and startplayer == 2:
      
      return 'Choose a valid card to show'

############################# CASE 2 ############################

    if str(cardtotake) in game.cards and startplayer < 1 or str(cardtotake) in game.cards and startplayer > 2:
      
      return 'Choose a valid player to start'

############################# CASE 3 ############################

    if str(cardtotake) not in game.cards and startplayer > 2 or  str(cardtotake) not in game.cards and startplayer < 1:
      
      return 'Choose a valid player to start and a valid card to show'

################### PLAYERS ACTIONS FUNCTIONS ######################

############################# CHECK WINNER #######################
  playeronewins = False
  playertwowins = False

############################ PLAYER 1 ############################
  
  @classmethod
  def Winnerone(cls, result, i, count):
    
    if i < len(cls.mazoplayer1):
      for info in cls.mazoplayer1:
        if cls.mazoplayer1[i] == info:
          count+= 1
      result.append(count)
      return cls.Winnerone(result, i+1, 0)
    
    if 3 in result and 2 in result:
      cls.playeronewins = True
      return cls.playeronewins
    return False

########################### PLAYER 2 ############################## 
  
  @classmethod
  def Winnertwo(cls, result, i, count):
    
    if i < len(cls.mazoplayer2):
      for info in cls.mazoplayer2:
        if cls.mazoplayer2[i] == info:
          count+= 1
      result.append(count)
      return cls.Winnertwo(result, i+1, 0)
    
    if 3 in result and 2 in result:
      cls.playertwowins = True
      return cls.playertwowins
    return False

########################## RESULTS ################################## 
  
  @staticmethod
  def Winneresult():
    if game.Winnerone([], 0, 0):
      cls()
      return game.player1 + ' WINS!', game.mazoplayer1
    
    if game.Winnertwo([], 0, 0):
      cls()
      return game.player2 + ' WINS!', game.mazoplayer2

################### TAKE CARD FROM PACKAGE ###################
  
  cardfrompackage = None
  cardnumber = -1

  @property
  def takefrompackage(self):
################### TAKE FROM PACKAGE EXCEPTIONS ################

########################### PLAYER 1 ############################

      if game.playerturn == 1 and self.playerid == 2:
        
        print ''
        return 'Is the turn of ' + game.player1 + '!'
      
      if game.playerturn == 1 and self.playerid == 1 and self.taked == True:
        
        print ''
        return game.player1 + ' you already took one!'

########################### PLAYER 2 ############################   

      if game.playerturn == 2 and self.playerid == 1:
        
        print ''
        return 'Is the turn of ' + game.player2 + '!'
      
      if game.playerturn == 2 and self.playerid == 2 and self.taked == True:
        
        print ''
        return game.player2 + ' you already took one!'

######################## PLAYER 1 TAKES ######################     
      
      if self.playerid == 1 and self.taked == False:
        
        game.cardnumber += 1
        game.playerturn = 1
        self.taked = True
        game.cardfrompackage = game.cards[game.cardnumber]
        
        print ''
        print self.name + ' takes from package!'
        
        return 'The card is: ' + str(game.cardfrompackage) + ',' + ' you must keep it or leave it!'

######################### PLAYER 2 TAKES #####################

      if self.playerid == 2 and self.taked == False:
        
        game.cardnumber += 1
        game.playerturn = 2
        self.taked = True
        game.cardfrompackage = game.cards[game.cardnumber]
        
        print ''
        print self.name + ' takes from package!'
        
        return 'The card is: ' + str(game.cardfrompackage) + ',' + ' you must keep it or leave it!'

########################## KEEP THE CARD ##########################

  @property
  def keepcard(self):  

######################## PLAYER 1 KEEP EXCEPTIONS #######################
    
    if game.playerturn == 1 and self.playerid == 2:
      
      print ''
      return 'Is the turn of ' + game.player1 + '!'
    
    if game.playerturn == 1 and self.playerid == 1 and self.taked == False:
      print ''
      return game.player1 + '!, ' + "you can't keep a card if you don't take before!"
    
    if game.playerturn == 1 and self.playerid == 1 and self.keep == True:
      print ''
      return self.name + ' you already keep one!'

######################## PLAYER 2 KEEP EXCEPTIONS #######################
    
    if game.playerturn == 2 and self.playerid == 1:
      
      print ''
      return 'Is the turn of ' + game.player2 + '!'
    
    if game.playerturn == 2 and self.playerid == 2 and self.taked == False:
      print ''
      return game.player2 + '!, ' + "you can't keep a card if you don't take before!"
    
    if game.playerturn == 2 and self.playerid == 2 and self.keep == True:
      print ''
      return self.name + ' you already keep one!'

######################### PLAYER 1 KEEPS ##########################
    
    if self.playerid == 1 and self.taked == True and len(game.mazoplayer1) < 6 :

      self.keep = True
      game.mazoplayer1.append(game.cardfrompackage)
      
      cls()
      print "You can't take more cards and have to leave 1!"
      print ''
      
      return game.startgame(game.playerturn, game.displayedcard)

######################### PLAYER 2 KEEPS ##########################
    
    if self.playerid == 2 and self.taked == True and len(game.mazoplayer2) < 6:
      
      self.keep = True
      game.mazoplayer2.append(game.cardfrompackage)
      
      cls()
      print game.startgame(game.playerturn, game.displayedcard)
      print ''
      
      return "You can't take more cards and have to leave 1!"   

######################### LEAVE CARD ############################
  takedisplayed = False

  def leave(self, card):

    if game.Winneresult():
      return game.Winneresult()
#################### PLAYER 1 LEAVE EXCEPTIONS #######################
    if game.playerturn == 1 and self.playerid == 2:
      print ''
      return 'Is the turn of ' + game.player1 + '!'
    
    if game.playerturn == 1 and self.playerid == 1 and self.taked == False and self.keep == False:
      print ''
      return game.player1 + '!, ' + "you can't leave a card if you don't take or keep before!"

#################### PLAYER 2 LEAVE EXCEPTIONS #######################
    
    if game.playerturn == 2 and self.playerid == 1:
      print ''
      return 'Is the turn of ' + game.player2 + '!'

    if game.playerturn == 2 and self.playerid == 2 and self.taked == False and self.keep == False:
      print ''
      return game.player2 + '!, ' + "you can't leave a card if you don't take or keep before!"

######################### PLAYER 1 LEAVES #######################

############################# CASE 1 ############################

    if self.playerid == 1 and self.taked == True and self.keep == False and card != '':
      
      self.taked = False
      
      if len(game.mazoplayer1) == 5:
        print ''
        return self.name + '!, ' "you haven't got any card!"
      
      else:
        
        if card in game.mazoplayer1:
          for i in range(-1, len(game.mazoplayer1)):
            
            if game.mazoplayer1[i] == card:
              
              game.mazoplayer1.remove(game.mazoplayer1[i])
              game.displayedcard = card
              game.playerturn = 2
              
              cls()
              print self.name + ' leaves the card ' + card + '!'
              print ''
              print game.startgame(game.playerturn, game.displayedcard)
              print ''
              
              return 'Is your turn ' + game.player2 + '!'

############################# CASE 2 ############################   
    
    if self.playerid == 1 and self.taked == True and self.keep == False and card == '':
      
      self.taked = False

      if len(game.mazoplayer1) > 5:
        game.displayedcard = game.mazoplayer1.pop()
      else:
        game.displayedcard = game.cardfrompackage
        
      game.playerturn = 2

      cls()
      print game.player1 + ' leaves the card ' + game.displayedcard + '!'
      print ''
      print game.startgame(game.playerturn, game.displayedcard)
      print ''
    
      return 'Is your turn ' + game.player2 + '!'

############################# CASE 3 ############################    
    
    if self.playerid == 1 and self.taked == True and self.keep == True and card != '':

      self.taked = False
      self.keep = False
      
      if card in game.mazoplayer1:
        for i in range(-1, len(game.mazoplayer1)):
          
          if game.mazoplayer1[i] == card:
            
            game.mazoplayer1.remove(game.mazoplayer1[i])
            game.displayedcard = card
            game.playerturn = 2
            
            cls()
            print game.player1 + ' leaves the card ' + card + '!'
            print ''
            print game.startgame(game.playerturn, game.displayedcard)
            print ''
            
            return 'Is your turn ' + game.player2 + '!'

############################# CASE 4 ############################

    if self.playerid == 1 and self.taked == True and self.keep == True and card == '':

      self.taked = False
      self.keep = False
      
      if game.takedisplayed == True:
        game.displayedcard = game.previousdisplayed
        
        for i in range(-1, len(game.mazoplayer1)-1):
          if game.mazoplayer1[i] == game.displayedcard:
            game.mazoplayer1 = game.mazoplayer1[:i] + game.mazoplayer1[i+1:]
      else:
        game.displayedcard = game.cardfrompackage
      
      game.takedisplayed = False
      game.playerturn = 2

      cls()
      print game.player1 + ' leaves the card ' + game.displayedcard + '!'
      print ''
      print game.startgame(game.playerturn, game.displayedcard)
      print ''
    
      return 'Is your turn ' + game.player2 + '!'


########################## PLAYER 2 LEAVES ########################    

############################# CASE 1 ############################

    if self.playerid == 2 and self.taked == True and self.keep == False and card != '':
      
      self.taked = False
      
      if len(game.mazoplayer2) == 5:
        print ''
        return self.name + '!, ' "you haven't got any card!"
      
      else:
        
        if card in game.mazoplayer2:
          for i in range(-1, len(game.mazoplayer2)):
            
            if game.mazoplayer2[i] == card:
              
              game.mazoplayer2.remove(game.mazoplayer2[i])
              game.displayedcard = card
              game.playerturn = 1
              
              cls()
              print 'Is your turn ' + game.player1 + '!'
              print ''
              print game.startgame(game.playerturn, game.displayedcard)
              print ''
              
              return game.player2 + ' leaves the card ' + card + '!'

############################# CASE 2 ############################   

    if self.playerid == 2 and self.taked == True and self.keep == False and card == '':
      
      self.taked = False
      
      if len(game.mazoplayer2) > 5:
        game.displayedcard = game.mazoplayer2.pop()
      else:
        game.displayedcard = game.cardfrompackage
      
      game.playerturn = 1

      cls()
      print 'Is your turn ' + game.player1 + '!'
      print ''
      print game.startgame(game.playerturn, game.displayedcard)
      print ''
      
      return game.player2 + ' leaves the card ' + game.displayedcard + '!'

############################# CASE 3 ############################    
    
    if self.playerid == 2 and self.taked == True and self.keep == True and card != '':

      self.taked = False
      self.keep = False
      
      if card in game.mazoplayer2:
        for i in range(-1, len(game.mazoplayer2)):
          
          if game.mazoplayer2[i] == card:
            
            game.mazoplayer2.remove(game.mazoplayer2[i])
            game.displayedcard = card
            game.playerturn = 1
            
            cls()
            print 'Is your turn ' + game.player1 + '!'
            print ''
            print game.startgame(game.playerturn, game.displayedcard)
            print ''
            
            return game.player2 + ' leaves the card ' + game.displayedcard + '!'

############################# CASE 4 ############################

    if self.playerid == 2 and self.taked == True and self.keep == True and card == '':

      self.taked = False
      self.keep = False
      
      if game.takedisplayed == True:
        game.displayedcard = game.previousdisplayed
        
        for i in range(-1, len(game.mazoplayer2)-1):
          if game.mazoplayer2[i] == game.displayedcard:
            game.mazoplayer2 = game.mazoplayer2[:i] + game.mazoplayer2[i+1:]
      else:
        game.displayedcard = game.cardfrompackage
      
      game.takedisplayed = False
        
      game.playerturn = 1

      cls()
      print 'Is your turn ' + game.player1 + '!'
      print ''
      print game.startgame(game.playerturn, game.displayedcard)
      print ''
      
      return game.player2 + ' leaves the card ' + game.displayedcard + '!'

###################### TAKE DISPLAYED CARD ####################  
  @property
  def takedisplayedcard(self):

################## TAKE DISPLAYED CARD PLAYER 1 EXCEPTIONS ##########
    
    if game.playerturn == 1 and self.playerid == 2:
      print ''
      return 'Is the turn of ' + game.player1 + '!'
    
    if game.playerturn == 1 and self.playerid == 1 and self.taked == True:
      
      print ''
      return self.name + ' you already took one!'

################## TAKE DISPLAYED CARD PLAYER 2 EXCEPTIONS ##########
    
    if game.playerturn == 2 and self.playerid == 1:
      print ''
      return 'Is the turn of ' + game.player2 + '!'
    
    if game.playerturn == 2 and self.playerid == 2 and self.taked == True:
      
      print ''
      return self.name + ' you already took one!'
  
######################## PLAYER 1 TAKES ######################     

############################# CASE 1 ############################

    if self.playerid == 1 and self.taked == False and self.keep == False: 

      if game.displayedcard in game.mazoplayer1:
       
        self.taked = True
        self.keep = True
        game.takedisplayed = True
        for i in range(-1, len(game.mazoplayer1)-1):
            
          if game.mazoplayer1[i] == game.displayedcard:
            if i == -1:

              game.mazoplayer1.append(game.displayedcard)
              game.previousdisplayed = game.displayedcard

              cls()
              print self.name + ' takes the displayed card ' + game.displayedcard + '!, ' + 'now have to leave one!'
              print ''
              return game.startgame(game.playerturn, '?')
              
            else:

              game.mazoplayer1 = game.mazoplayer1[:i+1] + [game.displayedcard] + game.mazoplayer1[i+1:]
              game.previousdisplayed = game.displayedcard

              cls()
              print self.name + ' takes the displayed card ' + game.displayedcard + '!, ' + 'now have to leave one!'
              print ''

              return game.startgame(game.playerturn, '?')
      else:
        print ''
        return self.name + '!, ' + "you don't have a card that matches!"

######################## PLAYER 2 TAKES ######################     

############################# CASE 1 ############################
    if self.playerid == 2 and self.taked == False and self.keep == False: 

      if game.displayedcard in game.mazoplayer2:
        
        self.taked = True
        self.keep = True
        
        for i in range(-1, len(game.mazoplayer2)-1):

          
            
          if game.mazoplayer2[i] == game.displayedcard:
            if i == -1:

              game.mazoplayer2.append(game.displayedcard)
              game.previousdisplayed = game.displayedcard

              cls()
              print game.startgame(game.playerturn, '?')
              print ''

              return self.name + ' takes the displayed card ' + game.displayedcard + '!, ' + 'now have to leave one!'
              
            else:

              game.mazoplayer2 = game.mazoplayer2[:i+1] + [game.displayedcard] + game.mazoplayer2[i+1:]
              game.previousdisplayed = game.displayedcard

              cls()
              print game.startgame(game.playerturn, '?')
              print ''

              return self.name + ' takes the displayed card ' + game.displayedcard + '!, ' + 'now have to leave one!'
      else:
          print ''
          return self.name + '!, ' + "you don't have a card that matches!"