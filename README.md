This is a simple implementation of the Blackjack card game in Python. The game allows you to play against a computer dealer, where you can choose to take another card or keep your current hand.

How to play:
1. The game begins by dealing two cards each to the player and the dealer (Which in this case, is the computer).
2. You will see your cards and the dealer's first card.
3. Type 'y' to take another card. Type 'n' to keep your current hand and end your turn.
4. The dealer will draw cards until their score is 17 or higher.
5. The scores are compared to determine the winner.

Notes:
1. Aces count as 11 unless it causes the hand to go over 21, in which case they count as 1.
2. Face cards (Jack, Queen, King) count as 10.
3. If your initial two cards sum to 21, you have a "Blackjack" and win automatically unless the dealer also has a Blackjack, in which case it is a draw.
4. If your score exceeds 21, you lose the game.
5. The dealer must draw cards until their score is at least 17.
6. The highest score that does not exceed 21 wins.
