def get_random_cards():
    import random
    return random.sample(player.cards[:-1], len(player.cards)-1)

class player:
  cards = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', '?']

  player_self = []
  def __init__(self, name):
    player.player_self.append(self)
    self.name = name
    self.player_id = len(player.player_self)
    self.deck = get_random_cards()[:5]

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