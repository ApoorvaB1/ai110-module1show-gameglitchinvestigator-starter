# 🎮 Game Glitch Investigator: The Impossible Guesser

## 🚨 The Situation

You asked an AI to build a simple "Number Guessing Game" using Streamlit.
It wrote the code, ran away, and now the game is unplayable. 

- You can't win.
- The hints lie to you.
- The secret number seems to have commitment issues.

## 🛠️ Setup

1. Install dependencies: `pip install -r requirements.txt`
2. Run the broken app: `python -m streamlit run app.py`

## 🕵️‍♂️ Your Mission

1. **Play the game.** Open the "Developer Debug Info" tab in the app to see the secret number. Try to win.
2. **Find the State Bug.** Why does the secret number change every time you click "Submit"? Ask ChatGPT: *"How do I keep a variable from resetting in Streamlit when I click a button?"*
3. **Fix the Logic.** The hints ("Higher/Lower") are wrong. Fix them.
4. **Refactor & Test.** - Move the logic into `logic_utils.py`.
   - Run `pytest` in your terminal.
   - Keep fixing until all tests pass!

## 📝 Document Your Experience

- [ ] Describe the game's purpose: For users to guess the secret number
- [ ] Detail which bugs you found: play again button doesn't reset the game, higher and lower are being said oppositelty, attempts don't count till after first attempt, ends game at 1 attempt left, ranges keep automating to 1-100
- [ ] Explain what fixes you applied: I fixed the attempt counter, and the higher and lower mechanism, and the new game button generates a new number.

## 📸 Demo Walkthrough

Demo Walkthrough
1. User selects between Easy, Normal, or Hard difficulty.
2. Game randomly generates a secret number (e.x., 60).
3. User guesses a number; the game responds with either "Too High", or "Too Low."
4. Based on difficulty, user will only get certain number of attempts to guess number before losing game.
5. User clicks New Game to generate a new secret number and restart.

**Screenshot** *(optional)*: <!-- Insert a screenshot of your fixed, winning game here -->

## 🧪 Test Results

```
# Paste your pytest output here, e.g.:
# pytest tests/
# ========================= X passed in 0.XXs =========================
```

## 🚀 Stretch Features

- [ ] [If you choose to complete Challenge 4, describe the Enhanced UI changes here — a screenshot is optional]
