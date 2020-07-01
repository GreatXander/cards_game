import os
def cls():
    os.system('cls' if os.name=='nt' else 'clear')
    
########################## GAME SECTION #####################
from players import player
class game(player):
  
  player_turn = None
  displayed_card = None
  
######################### START GAME ########################
  def start_game(self, card_to_take):
    import def_winner
######################### START EXCEPTIONS ###################
    if str(card_to_take) not in game.cards:
      return 'Choose a valid card to show!'
    
    if game.player1 == '' or game.player2 == '':
      return 'You must enter a name for the two players!'
      
    if game.player_id -2 > 2:
      return 'In the game must be 2 players!'
        
######################## PLAYER START #####################
    
    if self.player_id == 1 or self.player_id == 2:
      game.player_turn = self.player_id
      game.displayed_card = card_to_take
      print(self.name + "'s turn!")
      print('')
      print('Player ' + str(self.player_id) + ': ' + self.name, self.mazo)
      print('')
      return('      Package: ' + '[?]' + '     Displayed: ' + str([game.displayed_card]))

##################################################################################

################### TAKE CARD FROM PACKAGE ###################
  card_from_package = None
  card_number = -1

  @property
  def take_from_package(self):
################### TAKE FROM PACKAGE EXCEPTIONS ################
    if self.player_id != game.player_turn:
      print('')
      return 'Is not your turn ' + self.name + '!'
    
    if self.taked == True:
      print('')
      return self.name + ' you already took one!'
######################## PLAYER TAKES ######################     
      
    if self.taked == False:
      game.card_number += 1
      game.player_turn = self.player_id
      self.taked = True
      game.card_from_package = game.cards[game.card_number]
      print('')
      print(self.name + ' takes from package!')
      return 'The card is: ' + str(game.card_from_package) + ',' + ' you must keep it or leave it!'

########################## KEEP THE CARD ##########################
  @property
  def keepcard(self):  
######################## PLAYER KEEP EXCEPTIONS #######################
    
    if self.player_id != game.player_turn:
      print('')
      return 'Is not your turn ' + self.name + '!'
    
    if self.taked == False:
      print('')
      return self.name + '!, ' + "you can't keep a card if you don't take before!"
    
    if self.keep == True:
      print('')
      return self.name + ' you already keep one!'

######################### PLAYER KEEPS ##########################
    
    if len(self.mazo) < 6 :

      self.keep = True
      self.mazo.append(game.card_from_package)
      cls()
      print("You can't take more cards and have to leave 1!")
      print('')
      return game.start_game(game.player_turn, game.displayed_card)

######################### LEAVE CARD ############################
  takedisplayed = False
  def leave(self, card):
#################### PLAYER LEAVE EXCEPTIONS #######################
    
    if self.player_id != game.player_turn:
      print('')
      return 'Is not your turn ' + self.name + '!'
    
    if self.taked == False and self.keep == False:
      print('')
      return self.name + '!, ' + "you can't leave a card if you don't take or keep before!"
      
######################### PLAYER 1 LEAVES #######################

############################# CASE 1 ############################

    if self.player_id == 1 and self.taked == True and self.keep == False:
      
      self.taked = False
      
      if card in game.mazoplayer1:
        return "You can't leave a card if you dont keep it!" 
      
      if card == '':
        if len(game.mazoplayer1) > 5:
          game.displayed_card = game.mazoplayer1.pop()
        else:
          game.displayed_card = game.card_from_package
        
        game.player_turn = 2
        
        cls()
        print(game.player1 + ' leaves the card ' + game.displayed_card + '!')
        print('')
        print(game.start_game(game.player_turn, game.displayed_card))
        print('')
        
        return 'Is your turn ' + game.player2 + '!'
      else:
        
        if card in game.mazoplayer1:
          for i in range(-1, len(game.mazoplayer1)):
            if game.mazoplayer1[i] == card:
              
              game.mazoplayer1.remove(game.mazoplayer1[i])
              game.displayed_card = card
              game.player_turn = 2
              
              cls()
              print(self.name + ' leaves the card ' + card + '!')
              print('')
              print(game.start_game(game.player_turn, game.displayed_card))
              print('')
              
              return 'Is your turn ' + game.player2 + '!'

############################# CASE 2 ############################    
    
    if self.player_id == 1 and self.taked == True and self.keep == True:

      self.taked = False
      self.keep = False
      
      if card == '':
        if game.takedisplayed == True:
          game.displayed_card = game.previousdisplayed
          
          for i in range(-1, len(game.mazoplayer1)-1):
            if game.mazoplayer1[i] == game.displayed_card:
              
              game.mazoplayer1 = game.mazoplayer1[:i] + game.mazoplayer1[i+1:]
        else:
          game.displayed_card = game.card_from_package
        
        game.takedisplayed = False
        game.player_turn = 2
        
        cls()
        print(game.player1 + ' leaves the card ' + game.displayed_card + '!')
        print('')
        print(game.start_game(game.player_turn, game.displayed_card))
        print('')
        
        return 'Is your turn ' + game.player2 + '!'
      
      else:
        
        if card in game.mazoplayer1:
          for i in range(-1, len(game.mazoplayer1)):
            if game.mazoplayer1[i] == card:
              
              game.mazoplayer1.remove(game.mazoplayer1[i])
              game.displayed_card = card
              game.player_turn = 2
              
              cls()
              print(game.player1 + ' leaves the card ' + card + '!')
              print('')
              print(game.start_game(game.player_turn, game.displayed_card))
              print('')
              
              return 'Is your turn ' + game.player2 + '!'

######################### PLAYER 2 LEAVES #######################

############################# CASE 1 ############################

    if self.player_id == 2 and self.taked == True and self.keep == False:
      
      self.taked = False
      if card in game.mazoplayer2:
        print('')
        return "You can't leave a card if you dont keep it!" 

      if card == '':
        if len(game.mazoplayer2) > 5:
          game.displayed_card = game.mazoplayer2.pop()
        else:
          game.displayed_card = game.card_from_package
        
        game.player_turn = 1
        
        cls()
        print('Is your turn ' + game.player1 + '!')
        print('')
        print(game.start_game(game.player_turn, game.displayed_card))
        print('')
        
        return self.name + ' leaves the card ' + game.displayed_card + '!'
      else:
        
        if card in game.mazoplayer2:
          for i in range(-1, len(game.mazoplayer2)):
            if game.mazoplayer2[i] == card:
              
              game.mazoplayer2.remove(game.mazoplayer2[i])
              game.displayed_card = card
              game.player_turn = 1
              
              cls()
              print('Is your turn ' + game.player1 + '!')
              print('')
              print(game.start_game(game.player_turn, game.displayed_card))
              print('')
              
              return self.name + ' leaves the card ' + card + '!'
############################# CASE 2 ############################    
    
    if self.player_id == 2 and self.taked == True and self.keep == True:

      self.taked = False
      self.keep = False
      
      if card == '':
        if game.takedisplayed == True:
          game.displayed_card = game.previousdisplayed
          
          for i in range(-1, len(game.mazoplayer2)-1):
            if game.mazoplayer2[i] == game.displayed_card:
              
              game.mazoplayer2 = game.mazoplayer2[:i] + game.mazoplayer2[i+1:]
        else:
          game.displayed_card = game.card_from_package
        
        game.takedisplayed = False
        game.player_turn = 1
        
        cls()
        print('Is your turn ' + game.player1 + '!')
        print('')
        print(game.start_game(game.player_turn, game.displayed_card))
        print('')
        
        return self.name + ' leaves the card ' + game.displayed_card + '!'
      else:
        
        if card in game.mazoplayer2:
          for i in range(-1, len(game.mazoplayer2)):
            if game.mazoplayer2[i] == card:
              
              game.mazoplayer2.remove(game.mazoplayer2[i])
              game.displayed_card = card
              game.player_turn = 1
              
              cls()
              print('Is your turn ' + game.player1 + '!')
              print('')
              print(game.start_game(game.player_turn, game.displayed_card))
              print('')
              
              return self.name + ' leaves the card ' + card + '!'

###################### TAKE DISPLAYED CARD ####################  
  @property
  def takedisplayed_card(self):

################## TAKE DISPLAYED CARD PLAYER 1 EXCEPTIONS ##########
    
    if game.player_turn == 1 and self.player_id == 2:
      print('')
      return 'Is the turn of ' + game.player1 + '!'
    
    if game.player_turn == 1 and self.player_id == 1 and self.taked == True:
      
      print('')
      return self.name + ' you already took one!'

################## TAKE DISPLAYED CARD PLAYER 2 EXCEPTIONS ##########
    
    if game.player_turn == 2 and self.player_id == 1:
      print('')
      return 'Is the turn of ' + game.player2 + '!'
    
    if game.player_turn == 2 and self.player_id == 2 and self.taked == True:
      
      print('')
      return self.name + ' you already took one!'
  
######################## PLAYER 1 TAKES ######################     

############################# CASE 1 ############################

    if self.player_id == 1 and self.taked == False and self.keep == False: 

      if game.displayed_card in game.mazoplayer1:
       
        self.taked = True
        self.keep = True
        game.takedisplayed = True
        for i in range(-1, len(game.mazoplayer1)-1):
            
          if game.mazoplayer1[i] == game.displayed_card:
            if i == -1:

              game.mazoplayer1.append(game.displayed_card)
              game.previousdisplayed = game.displayed_card

              cls()
              print(self.name + ' takes the displayed card ' + game.displayed_card + '!, ' + 'now have to leave one!')
              print('')
              return game.start_game(game.player_turn, '?')
              
            else:

              game.mazoplayer1 = game.mazoplayer1[:i+1] + [game.displayed_card] + game.mazoplayer1[i+1:]
              game.previousdisplayed = game.displayed_card

              cls()
              print(self.name + ' takes the displayed card ' + game.displayed_card + '!, ' + 'now have to leave one!')
              print('')

              return game.start_game(game.player_turn, '?')
      else:
        print('')
        return self.name + '!, ' + "you don't have a card that matches!"

######################## PLAYER 2 TAKES ######################     

############################# CASE 1 ############################
    if self.player_id == 2 and self.taked == False and self.keep == False: 

      if game.displayed_card in game.mazoplayer2:
        
        self.taked = True
        self.keep = True
        
        for i in range(-1, len(game.mazoplayer2)-1):
          
          if game.mazoplayer2[i] == game.displayed_card:
            if i == -1:

              game.mazoplayer2.append(game.displayed_card)
              game.previousdisplayed = game.displayed_card

              cls()
              print(game.start_game(game.player_turn, '?'))
              print('')

              return self.name + ' takes the displayed card ' + game.displayed_card + '!, ' + 'now have to leave one!'
              
            else:

              game.mazoplayer2 = game.mazoplayer2[:i+1] + [game.displayed_card] + game.mazoplayer2[i+1:]
              game.previousdisplayed = game.displayed_card

              cls()
              print(game.start_game(game.player_turn, '?'))
              print('')

              return self.name + ' takes the displayed card ' + game.displayed_card + '!, ' + 'now have to leave one!'
      else:
          print('')
          return self.name + '!, ' + "you don't have a card that matches!"