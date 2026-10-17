# Lab 4: Blackjack (Vibe Coding with an LLM)

Terminal Blackjack vs Dealer game in Python. The broken code was fixed and the
missing features were added one task at a time using an LLM coding assistant.

Code repo with a separate commit for each task:
https://github.com/devikan0111/SE_18_blackjack

## Contents

| File | Description |
| --- | --- |
| `before.mp4` | Video of the original code, before any changes |
| `after.mp4` | Video of the final code, after all changes |
| `main.py`, `game.py`, `cards.py`, `requirements.txt` | Updated code |
| `PES1UG24AM080_Chat_History.pdf` | Exported chat history with prompts and explanations |

## Before video (`before.mp4`)

The video runs the original game with `python main.py`.

1. The first hand is `8C 9H = 17`. Hitting draws `5H` and the total becomes 22,
   so the player busts. This is a correct bust.
2. The next hand is `JC 2C = 12`. Hitting draws `AH`, and the game shows
   `JC 2C AH = 23` and says **Bust**. This is the bug: the Ace is always counted
   as 11. The correct total is **13**, because the Ace should count as 1.
3. In the third round the player reaches `7H 5S 9S = 21`, and the game shows
   "Player wins".

Other problems visible in the original game:
- No betting. The prompt goes straight to hit or stand.
- Chips are never shown during play.
- A bust prints only "Bust." with no result or chip balance.
- Any answer other than `y` at "Play again?" quits.

## After video (`after.mp4`)

The video runs the final game with all four tasks applied.

1. A bet is asked first (`Place your bet (or q to quit)`), and the chips are
   shown at the start of the round (100 chips).
2. The hand `5C AD = 16` hits and draws `KD`. The game shows
   `5C AD KD = 16`, so the Ace dropped from 11 to 1. The old code would have
   shown 26 and busted.
3. Every draw prints a message such as `Player drew KD. New total: 16`.
4. Hitting again draws `10D` and the total is 26, so the player busts. The game
   prints "Player busts." and "Chips remaining: 90".
5. A new round starts after `y` at "Play again?", with the updated chips (90).
6. An invalid command (`d`) is rejected with "Invalid command. Enter h, s, or q."
   and the prompt repeats.
7. The dealer reveals cards and the round ends with the result and the chips
   remaining (80). Answering `n` quits the game.

## Tasks and commits

| Task | What changed | File |
| --- | --- | --- |
| 1. Fix Ace scoring | Aces count as 11 and drop to 1 when needed to avoid a bust | `cards.py` |
| 2. Round resolution | Natural blackjack, bust, dealer draws to 17, push, and the round ends cleanly | `game.py` |
| 3. Chips and betting | Validated bets, chips carry over, blackjack pays 3:2 (rounded down for odd bets), game over at 0 chips | `game.py` |
| 4. Feedback and robustness | Draw messages, validated play-again, `q` quits from any prompt, safe handling of an empty deck | `game.py` |

## How to run

```
python main.py
```

Use `h` to hit, `s` to stand and `q` to quit.
