class player:

  cards = ['J', '7', '8', 'Q', '4', '10', '6', '9', '2', '1', '5', 'A', '3', 'K', 'A', '7', '5', '3', '4', 'J', '6', '1', 'Q', '9', 'K', '8', '2', '10', 'Q', '4', '1', '10', '2', 'K', '7', '5', '3', '9', '8', 'A', '6', 'J', '6', 'A', '9', '8', '3', '5', '7', 'K', '2', '10', '1', '4', 'Q', 'J', '?']

################# PLAYERS LIST OF MAZOS (barajas) ############
  
  barajas_player1 = [cards[0:2] + cards[11:13] + cards[4:5], cards[3:6] + cards[7:9], cards[5:7] + cards[0:1] + cards[8:10]]
  
  barajas_player2 = [cards[2:4] + cards[6:7] + cards[6:8], cards[9:12] + cards[1:3], cards[7:9] + cards[2:3] + cards[10:12]]

########################### PLAYERS STRUCTURE ###############
  mazoplayer1 = None
  mazoplayer2 = None

  player_id = 0
  
  def __init__(self, name, mazo):
    player.player_id += 1
    self.name = name
    self.taked = False
    self.keep = False

    if mazo > 3 or mazo < 1:
      mazo = 1

    if player.player_id == 1:
      player.player1 = self.name
      self.mazo = player.barajas_player1[mazo-1]
      player.mazoplayer1 = player.barajas_player1[mazo-1]
    
    if player.player_id == 2:
      player.player2 =self.name
      self.mazo = player.barajas_player2[mazo-1]
      player.mazoplayer2 = player.barajas_player2[mazo-1]
    
    self.player_id = player.player_id

##################################################################################