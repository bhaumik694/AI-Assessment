from backend.agents.generator import GeneratorAgent
from backend.agents.reviewer import ReviewerAgent

generator = GeneratorAgent()
reviewer = ReviewerAgent()


def run_pipeline(grade, topic):

    initial = generator.generate(grade, topic)

    review = reviewer.review(initial.model_dump(),grade)

    refined = None

    if review.status == "fail":
        refined = generator.generate(
            grade,
            topic,
            feedback=review.feedback
        )

    return initial, review, refined