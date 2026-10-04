from logic_utils import check_guess, update_score
from streamlit.testing.v1 import AppTest


def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    outcome, message = check_guess(50, 50)
    assert outcome == "Win"


def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    outcome, message = check_guess(60, 50)
    assert outcome == "Too High"


def test_guess_too_low(): # with AI, updated assert statements to check tuples, not just strings
    # If secret is 50 and guess is 40, hint should be "Too Low"
    outcome, message = check_guess(40, 50)
    assert outcome == "Too Low"


def test_attempts_counter_starts_at_zero():
    at = AppTest("app.py", default_timeout=5)
    at.run()
    assert at.session_state["attempts"] == 0, "Attempts should initialize to 0, not 1"


def test_attempts_increment_on_valid_submit():
    at = AppTest("app.py", default_timeout=5)
    at.run()

    at.session_state["secret"] = 50
    at.text_input[0].set_value("40")
    at.button[0].click()
    at.run()

    assert at.session_state["attempts"] == 1, "Attempts should be 1 after first valid guess"


def test_game_ends_at_attempt_limit_not_before():
    at = AppTest("app.py", default_timeout=5)
    at.run()

    secret = 50
    at.session_state["secret"] = secret
    attempt_limit = 8

    for attempt in range(1, attempt_limit + 1):
        at.text_input[0].set_value("40")
        at.button[0].click()
        at.run()

        if attempt < attempt_limit:
            assert at.session_state["status"] == "playing", f"Game should still be playing at attempt {attempt}/{attempt_limit}"
        else:
            assert at.session_state["status"] == "lost", f"Game should end exactly at attempt {attempt_limit}"


def test_update_score_win_logic():
    score = update_score(current_score=0, outcome="Win", attempt_number=1)
    assert score == 90, "Win on attempt 1 should award 90 points (100 - 10*1)"

    score = update_score(current_score=0, outcome="Win", attempt_number=5)
    assert score == 50, "Win on attempt 5 should award 50 points (100 - 10*5)"

    score = update_score(current_score=0, outcome="Win", attempt_number=10)
    assert score == 10, "Win on attempt 10 should award min 10 points, not negative"


def test_update_score_wrong_guess_penalty():
    score = update_score(current_score=100, outcome="Too High", attempt_number=1)
    assert score == 95, "Too High should deduct 5 points"

    score = update_score(current_score=100, outcome="Too Low", attempt_number=1)
    assert score == 95, "Too Low should deduct 5 points (same as Too High)"
