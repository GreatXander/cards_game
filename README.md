# Card game 3 and 2
-This game consists of two players having 5 cards (they cannot have more than 5), on the "game table" is the pack of cards that they cannot see and next to it is a displayed card. The game is that the player who has 3 equal cards of one type and 2 equal cards of another type wins the game.

# How to play:
The rules are very simple, either player can start, when it is a player's turn he has 2 options:

1- Take the displayed card.
2- Take a card from the package.

-Option 1: For the player to be able to take the displayed card he must have in his deck one that is the same, if so, the player who take the card must leave a card from his deck and that card pass to be the card shown and pass the turn, if not, then he cannot take the displayed card and is forced to take one from the package.

-Option 2: When the player takes a card from the package he decides if he wants to keep it or leave it as the card shown, if the player keeps it then he must leave a card from his deck to be the card shown and pass the turn, otherwise the card that took from the package happens to be the card shown and pass the turn.

-This loop is maintained until one of the two players has 3 equal cards of one type and 2 equal cards of another type, if this is so then that player is the winner.

# How to play with the program

1- Create players: to create the players we use the game class and first specify the name of the player and then the deck of cards to be used, for example: A = game ('Alexander', 1).

2- Start the game: to start the game we use the declaration of the player who is going to start followed by a period and 'start_game', in parentheses we will put the card we want to be the card shown at the beginning of the game, for example: A. start_game ('J').

(Player actions)
3- Take a card from the package: to take a card from the package we only have to put the declaration of the player that will do it followed by a period and 'take_from_package', for example: A.take_from_package.

4- Take the displayed card: We put the declaration of the player that will do it followed by a period and 'take_displayed_card', for example: A.take_displayed_card.

5- Keep the card: To keep a card that has been taken we only put the declaration of the player that will do it followed by a period and 'keep_card', for example: A.keep_card.

6- Leave the card: To leave a card we only put the declaration of the player that will do it followed by a period and 'leave', if taked a card and don't keep it yet and want to leave it: A.leave(''), otherwise if already keep it: in brackets we put the card that we want to leave, for example: A.leave ('J').
