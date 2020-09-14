import os
def cls():
    os.system('cls' if os.name=='nt' else 'clear')
import players

class game(players.player):
  
  def print_game_status(self, displayed_card):
    game.displayed_card = displayed_card.upper()
    print(
    "\n",
    self.name + "'s turn",
    "\n \n",
    'Player ' + str(self.player_id) + ': ' + self.name,self.deck,
    "\n \n",
    '     1.Package: ' + '[?]' + '     2.Displayed:' + str([displayed_card.upper()])
    )
    return '\n'
  
  def card_find_match(self, card):
    for cards in range(-1, len(self.deck)-1):
      if self.deck[cards] == card:
        card_index = cards
    self.deck.insert(card_index, card)

  def start_game(self, displayed_card, option_choosed):
    self.print_game_status(displayed_card)
    if option_choosed == False:
      print("\n")
      option = input('Choose your move ' + self.name + ': ')
      while option != '1' and option != '2':
        option = input('Choose a valid move: ')
      option_choosed = True
      if option == '1':
        cls()
        return(self.take_from_package)
      else:
        print('\n')
        return(self.take_displayed_card)
    return ''

  @property
  def take_from_package(self):
    game.card_from_package = players.get_random_cards()[0]
    print(self.print_game_status(game.displayed_card))
    print(self.name + ' takes from package!')
    option = input('The card is: ' + str(game.card_from_package) + ': 1.keep or 2.leave: ')
    while option != '1' and option != '2':
      option = input('Choose a valid move: ')
    if option == '1':
      return self.keep_card
    if option == '2':
      return self.leave_card('', True)

  @property
  def keep_card(self):
    if game.card_from_package in self.deck:
      self.card_find_match(game.card_from_package)
    else:
      self.deck.append(game.card_from_package)
    cls()
    print(self.start_game(game.displayed_card, True))
    option = input("You have to leave one card: ")
    if game.winner(self):
      self.leave_card(option, False)
      return game.winner(self)
    else:
      return self.leave_card(option, False)

  def leave_card(self, card, is_from_package):
    if is_from_package:
      card = game.card_from_package
      game.displayed_card = card
    else:
      while card == '' or card.upper() not in self.deck:
        print('\n')
        card = input('Must insert a valid card to leave: ').upper()
      card = card.upper()
      for cards in range(-1, len(self.deck)-1):
        if self.deck[cards] == card:
          self.deck.remove(self.deck[cards])
          game.displayed_card = card
    cls()
    if game.winner(self):
      return game.winner(self)
    else:
      if self.player_id == 1:
        self_index = 1
      else:
        self_index = 0
      print(self.name + ' leaved the card ' + card + '!')
      return(game.player_self[self_index].start_game(game.displayed_card, False))

  @property
  def take_displayed_card(self):
    if game.displayed_card not in self.deck:
      cls()
      print("You don't have a card that matches!, taked from package!")
      self.take_from_package
    else:
      self.card_find_match(game.displayed_card)
      game.previous_displayed = game.displayed_card
      cls()
      print(self.start_game('?', True))
      option = input(self.name + ' takes the displayed card ' + game.previous_displayed + '!  \n' + 'write the card you want to leave: ')
      if game.winner(self):
        self.leave_card(option, False)
        return game.winner(self)
      else:
        return self.leave_card(option, False)

  def Run():
    player_number = 0
    while player_number < 2:
      player_number+= 1
      name = input('Enter name for player ' + str(player_number) + ': ')
      while name == '':
        cls()
        name = input('Enter a valid name for player ' + str(player_number) + ': ')
      if player_number == 1:
        A = game(name)
      else:
        B = game(name)
        cls()
        displayed_card = input('Choose a card to display on table: ')
        while(str(displayed_card).upper() not in game.cards):
          cls()
          displayed_card = input('Choose a valid card to display on table: ')
        print(A.start_game(displayed_card, False))

game.Run();