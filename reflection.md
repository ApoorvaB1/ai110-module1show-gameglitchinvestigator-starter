# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").

**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input | Expected Behavior | Actual Behavior | Console Output / Error |
|-------|-------------------|-----------------|------------------------|
| | | | |
| | | | |
| | | | |

---

## 2. How did you use AI as a teammate?
 I used AI  to help me debug the broken functions, such as check_guess. At times I would not accept the changes claude was suggesting, because it was going out of the scope that I outlined it too. At other times, the fixes it suggested were not enough to fix the bug, so I would go through the code and highlight lines I see bugs in, and specifically point it out to claude. that bug was the attempt bug, It took multiple suggestions to fix. AI suggested a change in the lines, and then once I kept prompting it, it found the correct line to fix, adding a max() function. I verified the result by running the app again, testing it oout myself. One change that was correct that I accepted was when I was testing PyTest. I couldn't run it at first, due to an error from the import logic_utils line. I prompted claude, and after multiple suggestions, it finally moved the functions being tested from app.py to logic_utils, and the PyTest ran. 

---

## 3. Debugging and testing your fixes

I ran the app to check if the attempts was fixed, and if the higher and loweer was working the right way. next time, as I write code, I will write tests alongside it, so I can test my code through that without having to run the app every time.

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.
