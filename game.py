from cards import Deck, hand_value


class Blackjack:
    def __init__(self):
        self.chips = 100

    def show(self, player, dealer, hide=True):
        shown_dealer = ["??"] if hide else [f"{r}{s}" for r, s in dealer]
        print("Dealer:", " ".join(shown_dealer))
        print("Player:", " ".join(f"{r}{s}" for r, s in player),
              "=", hand_value(player))


    def round(self):
        print("\nChips:", self.chips)

        # Ask for a valid bet.
        while True:
            raw_bet = input("Place your bet: ").strip()

            try:
                bet = int(raw_bet)
            except ValueError:
                print("Invalid bet. Enter a whole number.")
                continue

            if bet <= 0:
                print("Bet must be greater than zero.")
            elif bet > self.chips:
                print("You cannot bet more chips than you have.")
            else:
                break

        deck = Deck()
        player = [deck.draw(), deck.draw()]
        dealer = [deck.draw(), deck.draw()]
        self.show(player, dealer)

        # Settle the wager once when the round ends.
        def finish(result, message, profit=None):
            if result == "win":
                self.chips += bet if profit is None else profit
            elif result == "loss":
                self.chips -= bet

            print(message)
            print("Chips after round:", self.chips)
            return True

        # Check for Blackjack on the initial two cards.
        player_bj = len(player) == 2 and hand_value(player) == 21
        dealer_bj = len(dealer) == 2 and hand_value(dealer) == 21

        if player_bj or dealer_bj:
            self.show(player, dealer, hide=False)

            if player_bj and dealer_bj:
                return finish("push", "Push. Both have Blackjack.")
            elif player_bj:
                profit = bet * 3 // 2
                return finish("win", "Blackjack! Player wins.", profit)
            else:
                return finish("loss", "Dealer has Blackjack. Dealer wins.")

        # Player's turn.
        while hand_value(player) < 21:
            key = input("[h]it [s]tand [q]uit: ").strip().lower()

            if key == "q":
                return False
            if key == "s":
                break
            if key == "h":
                player.append(deck.draw())
                self.show(player, dealer)

                if hand_value(player) > 21:
                    self.show(player, dealer, hide=False)
                    return finish("loss", "Bust.")

        # Dealer draws until reaching at least 17.
        while hand_value(dealer) < 17:
            dealer.append(deck.draw())

        self.show(player, dealer, hide=False)
        pv, dv = hand_value(player), hand_value(dealer)

        if dv > 21 or pv > dv:
            return finish("win", "Player wins.")
        elif pv < dv:
            return finish("loss", "Dealer wins.")
        else:
            return finish("push", "Push.")


    def run(self):
        print("Blackjack — starting chips:", self.chips)

        while self.chips > 0:
            if not self.round():
                return

            if self.chips == 0:
                print("Game Over! You have no chips left.")
                return

            if input("Play again? [y/n]: ").strip().lower() != "y":
                return

        print("Game Over! You have no chips left.")
