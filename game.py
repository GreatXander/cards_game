import os
def cls():
    os.system('cls' if os.name=='nt' else 'clear')
    
########################## GAME SECTION #####################
import players
class game(players.player):
  
  player_turn = None
  displayed_card = None

######################### START GAME ########################
  def start_game(self, card_to_take):
######################### START EXCEPTIONS ###################
    if game.winner():
      return game.winner()

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
      print(self.name + "'s turn")
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
  def keep_card(self):  
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
      print(game.start_game(self, game.displayed_card))
      print('')
      return "You can't take more cards and have to leave 1!"

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
      
######################### PLAYER LEAVES #######################
    if self.taked == True and self.keep == False:
      
      self.taked = False
      
      if card in self.mazo:
        print('')
        return "You can't leave a card if you dont keep it!" 
      
      if len(self.mazo) > 5:
        game.displayed_card = self.mazo.pop()
      else:
        game.displayed_card = game.card_from_package
      
      if self.player_id == 1: 
        game.array_num = 1
        game.player_turn = 2
      else:
        game.array_num = 0
        game.player_turn = 1
      
      if self.player_id == 1:
        players.player.mazoplayer1 = self.mazo
      else:
          players.player.mazoplayer2 = self.mazo
      
      cls()
      print(game.start_game(game.array[game.array_num], game.displayed_card))
      print('')
      return(self.name + ' leaves the card ' + game.displayed_card + '!')

############################# CASE 2 ############################    
    
    if self.taked == True and self.keep == True:

      self.taked = False
      self.keep = False
      
      if card == '':
        print('')
        return 'Must insert a card to leave!'

      if card in self.mazo:
        for i in range(-1, len(self.mazo)):
          if self.mazo[i] == card:
            self.mazo.remove(self.mazo[i])
            game.displayed_card = card
            
            if self.player_id == 1: 
              game.array_num = 1
              game.player_turn = 2
            else:
              game.array_num = 0
              game.player_turn = 1
            
            if self.player_id == 1:
              players.player.mazoplayer1 = self.mazo
            else:
              players.player.mazoplayer2 = self.mazo   

            cls()
            print(game.start_game(game.array[game.array_num], game.displayed_card))
            print('')
            return(self.name + ' leaved the card ' + card + '!')

###################### TAKE DISPLAYED CARD ####################  
  @property
  def take_displayed_card(self):
############### TAKE DISPLAYED CARD PLAYERS EXCEPTIONS ##########
    
    if self.player_id != game.player_turn:
      print('')
      return 'Is not your turn ' + self.name + '!'
    
    if self.taked == True:
      print('')
      return self.name + ' you already took one!'

######################## PLAYER TAKES ######################     
    if self.taked == False and self.keep == False: 
      if game.displayed_card in self.mazo:
        
        self.taked = True
        self.keep = True
        game.takedisplayed = True

        for i in range(-1, len(self.mazo)-1):
          if self.mazo[i] == game.displayed_card:
            if i == -1:
              self.mazo.append(game.displayed_card)
            else:
              self.mazo = self.mazo[:i+1] + [game.displayed_card] + self.mazo[i+1:]
    
            game.previousdisplayed = game.displayed_card 
            cls()
            print(game.start_game(self, '?'))
            print('')
            return(self.name + ' takes the displayed card ' + game.previousdisplayed + '!, ' + 'now have to leave one!')
      else:
        print('')
        return self.name + '!, ' + "you don't have a card that matches!"