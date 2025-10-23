# tests/test_quick_mode.py
import itertools
from app.recommender import recommend_blockchain, recommendations

def test_quick_mode_all_combinations():
    """
    Test all 32 possible combinations of 5 yes/no questions in quick mode.
    Ensure that each combination returns a valid recommendation key.
    """
    # 5 questions -> 2^5 = 32 combinations
    all_combinations = list(itertools.product([False, True], repeat=5))

    for answers in all_combinations:
        # Extend answers to 30 items to satisfy recommend_blockchain
        extended_answers = list(answers) + [False]*25
        key = recommend_blockchain(extended_answers)

        assert key in recommendations, f"Invalid recommendation key for answers {answers}: {key}"
