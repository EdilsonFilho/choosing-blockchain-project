# tests/test_advanced_mode.py
import random
from app.recommender import recommend_blockchain, recommendations

def generate_sample_advanced_answers(n=100):
    """
    Generate 'n' random samples of 30 boolean answers for advanced mode.
    """
    samples = []
    for _ in range(n):
        answers = [random.choice([True, False]) for _ in range(30)]
        samples.append(answers)
    return samples

def test_advanced_mode_samples():
    """
    Test random samples of advanced mode answers.
    Ensure that each sample returns a valid recommendation key.
    """
    samples = generate_sample_advanced_answers(n=100)
    for answers in samples:
        key = recommend_blockchain(answers)
        assert key in recommendations, f"Invalid recommendation key for answers {answers}: {key}"

def test_advanced_mode_extremes():
    """
    Test extreme cases: all True and all False
    """
    extremes = [
        [True]*30,
        [False]*30
    ]
    for answers in extremes:
        key = recommend_blockchain(answers)
        assert key in recommendations, f"Invalid recommendation key for extreme answers: {key}"
