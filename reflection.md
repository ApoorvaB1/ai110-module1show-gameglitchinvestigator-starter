# 💭 Reflection: Game Glitch Investigator

This experience really taught me to look closely at what the AI is fixing. I needed to reject certain changes and question the Ai further on it's reasoning, because someimes I was not sure about what it waa doing. I learnt how to fix bugs, use PyTest, and not trust AI as much.

## 1. What was broken when you started?

When I first ran the game , the higher and lower were working oppositely, and I noticed the ranges of the numbers vs what the range should've been wasn't aligned. I also noticed the count of the attempt left was 1 off.
  (for example: "the hints were backwards").

**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input | Expected Behavior | Actual Behavior | Console Output / Error |
|-------|-------------------|-----------------|------------------------|
| Guess number| Display the correct "Too High" or "Too Low" hint | Hints were reversed | No console error
| Start game and make guesses|Display the correct number of attempts remaining | Attempt counter was off by 1| no console output|
| Restart game | Create new number to guess | Gamew was not reset| no console output|

---

## 2. How did you use AI as a teammate?
 I used AI  to help me debug the broken functions, such as check_guess. At times I would not accept the changes claude was suggesting, because it was going out of the scope that I outlined it too. At other times, the fixes it suggested were not enough to fix the bug, so I would go through the code and highlight lines I see bugs in, and specifically point it out to claude. that bug was the attempt bug, It took multiple suggestions to fix. AI suggested a change in the lines, and then once I kept prompting it, it found the correct line to fix, adding a max() function. I verified the result by running the app again, testing it oout myself. One change that was correct that I accepted was when I was testing PyTest. I couldn't run it at first, due to an error from the import logic_utils line. I prompted claude, and after multiple suggestions, it finally moved the functions being tested from app.py to logic_utils, and the PyTest ran. 

---

## 3. Debugging and testing your fixes

I ran the app to check if the attempts was fixed, and if the higher and loweer was working the right way. next time, as I write code, I will write tests alongside it, so I can test my code through that without having to run the app every time.

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

I learned that Streamlit reruns the entire script when a user used the app, and that the changes you make on the code end become live on streamlit app. I would explain streamlit reruns by saying that it is important to reset the session state when starting a new game, so the user doesn't lose track of progress.
---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?

One habit i want to reuse is closely looking into what suggestions AI is changing, and scrutinizing it more. I will continue to develop this skill by asking other ai bots if the suggestion claude is making is the most optimal one, using other chatbots as second opinions. This project changed the way I think about AI generated code as it taught me that it isn't always right.

