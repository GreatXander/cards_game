import os
def cls():
    os.system('cls' if os.name=='nt' else 'clear')
    
########################## GAME SECTION #####################
import players
class game(players.player):
  
  game_start = False
  choosed = False

  player_turn = None
  displayed_card = None

######################### START GAME ########################
  def start_game(self, card_to_take):
######################### START EXCEPTIONS ###################
    while(str(card_to_take).upper() not in game.cards_game):
      cls()
      card_to_take = input('Choose a valid card to show: ')
      if card_to_take in game.cards_game:
        return self.start_game(card_to_take)
        
######################## PLAYER START #####################
    if self.player_id == 1 or self.player_id == 2:
      print()
      game.displayed_card = card_to_take.upper()
      
      print(self.name + "'s turn")
      print('')
      print('Player ' + str(self.player_id) + ': ' + self.name, self.mazo)
      print('')
      print('     1.Package: ' + '[?]' + '     2.Displayed: ' + str([game.displayed_card]))
      print()
        
      if game.choosed == False:
        option = input('Choose your move ' + self.name + ': ')
        if option != '1' and option != '2':
          while option != '1' and option != '2':
            option = input('Choose a valid move: ')
        game.choosed = True
        if option == '1':
          cls()
          return(self.take_from_package)
            
        if option == '2':
          print()
          return(self.take_displayed_card)
      return ''
##################################################################################

################### TAKE CARD FROM PACKAGE ###################
  card_from_package = None
  card_number = 0
  
  @property
  def take_from_package(self):
######################## PLAYER TAKES ######################
    if game.card_number == len(game.cards_game)-2:
      game.card_number = -1     
    
    game.card_from_package = game.cards_game[game.card_number]
    game.card_number += 1
    self.taked = True
    
    print(self.start_game(game.displayed_card))
    print(self.name + ' takes from package!')
    option = input('The card is: ' + str(game.card_from_package) + ': 1.keep or 2.leave: ')
      
    while option != '1' and option != '2':
      option = input('Choose a valid move: ')
      
    if option == '1':
      return self.keep_card
    if option == '2':
      return self.leave('')
########################## KEEP THE CARD ##########################
  @property
  def keep_card(self):  
######################### PLAYER KEEPS ##########################
    self.keep = True
    self.mazo.append(game.card_from_package)
    cls()
    if game.winner(self):
      print(game.start_game(self, game.displayed_card))
      self.leave(input("You can't take more cards_game and have to leave 1: "))
      return game.winner(self)
    else:
      print(game.start_game(self, game.displayed_card))
      return self.leave(input("You can't take more cards_game and have to leave 1: "))

############################# LEAVE CARD ###############################
  def leave(self, card):
############################# Player leaves ############################    
    self.taked = False
    self.keep = False
    if card == '':
      card = game.card_from_package
      game.displayed_card = card
    else:
      while card.upper() not in self.mazo:
        print()
        card = input('Must insert a valid card to leave: ')
      
      for i in range(-1, len(self.mazo)-1):
        if self.mazo[i] == card.upper():
          self.mazo.remove(self.mazo[i])
          game.displayed_card = card.upper()
        
    if self.player_id == 1: 
      game.self_index = 1
    else:
      game.self_index = 0
        
    cls()
    if game.winner(self):
      return game.winner(self)
    else:
      game.choosed = False
      print(self.name + ' leaved the card ' + card.upper() + '!')
      return(game.start_game(game.player_self[game.self_index],game.displayed_card))
            
###################### TAKE DISPLAYED CARD ####################  
  @property
  def take_displayed_card(self):
######################## PLAYER TAKES ######################     
    if game.displayed_card not in self.mazo:
      cls()
      print("You don't have a card that matches!, taked from package!")
      self.take_from_package
    else:
      self.taked = True
      self.keep = True
        
      for i in range(-1, len(self.mazo)-1):
        if self.mazo[i] == game.displayed_card.upper():
          if i == -1:
            self.mazo.append(game.displayed_card.upper())
          else:
            self.mazo = self.mazo[:i+1] + [game.displayed_card.upper()] + self.mazo[i+1:]
            
          game.previous_displayed = game.displayed_card 
            
          cls()
          if game.winner(self):
            print (self.start_game('?'))
            self.leave(input(self.name + ' takes the displayed card ' +game.previous_displayed + '! now have to leave one: '))
            return game.winner(self)
          else:
            print(self.start_game('?'))
            return self.leave(input(self.name + ' takes the displayed card ' + game.previous_displayed + '! now have to leave one: '))
i = 0
while i <= 1: 
  i+= 1
  name = input('Enter name for player ' + str(i) + ': ')
  while name == '':
    cls()
    name = input('Enter a valid name: ')
  if i == 1:
    A = game(name, 1)
  else:
    B = game(name, 1)
cls()
card_start = input('Specify the first card to show: ')
cls()
print(A.start_game(card_start))