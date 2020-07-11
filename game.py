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
    if game.winner():
      return game.winner()
    
    while(str(card_to_take) not in game.cards):
      cls()
      card_to_take = input('Choose a valid card to show: ')
      if card_to_take in game.cards:
        return self.start_game(card_to_take)
        
######################## PLAYER START #####################
    if self.player_id == 1 or self.player_id == 2:
      print()
      
      game.player_turn = self.player_id
      game.displayed_card = card_to_take
      
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
  card_number = -1

  @property
  def take_from_package(self):
######################## PLAYER TAKES ######################     
      
    if self.taked == False:
      game.card_number += 1
      game.player_turn = self.player_id
      self.taked = True
      game.card_from_package = game.cards[game.card_number]
      
      print(self.start_game(game.displayed_card))
      print(self.name + ' takes from package!')
      option = input('The card is: ' + str(game.card_from_package) + ': 1.keep or 2.leave: ')
      
      while option != '1' and option != '2':
        option = input('Choose a valid move: ')
      
      if option == '1':
        return self.keep_card
      if option == '2':
        if self.keep == False:
          return self.leave('')
        return self.leave(input('Card to leave: '))

########################## KEEP THE CARD ##########################
  @property
  def keep_card(self):  
######################### PLAYER KEEPS ##########################
    
    if len(self.mazo) < 6 :

      self.keep = True
      self.mazo.append(game.card_from_package)
      cls()
      print(game.start_game(self, game.displayed_card))
      return self.leave(input("You can't take more cards and have to leave 1: "))

######################### LEAVE CARD ############################
  def leave(self, card):
######################### PLAYER LEAVES #######################
    if self.taked == True and self.keep == False:
      
      self.taked = False

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
      game.choosed = False
      print(self.name + ' leaved the card ' + game.displayed_card + '!')
      return(game.start_game(game.array[game.array_num], game.displayed_card))
     
############################# CASE 2 ############################    
    
    if self.taked == True and self.keep == True:

      self.taked = False
      self.keep = False
      
      while card == '' or card not in self.mazo:
        print()
        card = input('Must insert a valid card to leave: ')

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
            game.choosed = False
            print(self.name + ' leaved the card ' + card + '!')
            return(game.start_game(game.array[game.array_num], game.displayed_card))
            
###################### TAKE DISPLAYED CARD ####################  
  @property
  def take_displayed_card(self):
######################## PLAYER TAKES ######################     
    if self.taked == False and self.keep == False: 
      if game.displayed_card not in self.mazo:
        print("You don't have a card that matches!, taked from package!")
        self.take_from_package
      else:
        self.taked = True
        self.keep = True
        
        for i in range(-1, len(self.mazo)-1):
          if self.mazo[i] == game.displayed_card:
            if i == -1:
              self.mazo.append(game.displayed_card)
            else:
              self.mazo = self.mazo[:i+1] + [game.displayed_card] + self.mazo[i+1:]

            game.previous_displayed = game.displayed_card 
            self.leave(input(self.name + ' takes the displayed card ' + game.previous_displayed + '! now have to leave one: '))

one = input('Enter name for player 1: ')
if one == '':
  while one == '':
    cls()
    one = input('Enter a valid name: ')
A = game(one, 2)

two = input('Enter name for player 2: ')
if two == '':
  while two == '':
    cls()
    two = input('Enter a valid name: ')
B = game(two, 1)

cls()
card_start = input('Specify the first card to show: ')
cls()
print(A.start_game(card_start))