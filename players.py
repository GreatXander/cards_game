class player:
  import random 
  cards = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', '?']
  cards_shuffle = random.sample(cards[:-1], len(cards)-1)

  player_id = 0
  player_self = []
  def __init__(self, name):
    player.player_self.append(self)
    player.player_id += 1
    self.name = name
    if player.player_id == 1: 
      self.deck = player.cards_shuffle[:5]
    else:
      self.deck = player.cards_shuffle[6:11]
    self.player_id = player.player_id

  def winner(self):
    count = 0
    result = []
    card = -1
    while card != len(self.deck)-1:
      for cards in self.deck:
        if self.deck[card] == cards:
          count += 1
      result.append(count)
      count = 0
      card+= 1    
    if 3 in result and 2 in result:
      return self.name + ' WINS!', self.deck