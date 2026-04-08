from backend.llm import call_llm_json
from backend.schemas import ReviewerOutput
from backend.grade_rules import get_grade_rule


class ReviewerAgent:

    def review(self, content, grade):

        rule = get_grade_rule(grade)

        prompt = f"""
        Review the following educational content:

        {content}

        Expected Grade: {grade}

        Difficulty Guidelines:
        {rule}

        Your job is to evaluate whether the content is appropriate for the given grade.

        Carefully analyze:
        - Concept correctness
        - Clarity of explanation
        - Alignment between explanation and MCQs
        - Difficulty level relative to grade

        IMPORTANT:
        - Think step-by-step internally before answering
        - Provide clear reasoning separately
        - Do NOT mix reasoning inside feedback
        - Feedback must be concise, actionable points

        If difficulty or correctness is not appropriate → mark as "fail"

        Output STRICT JSON ONLY:
        {{
          "status": "pass" or "fail",
          "reasoning": "clear explanation of what is right/wrong and why",
          "feedback": ["specific issue 1", "specific issue 2"]
        }}
        """

        data = call_llm_json(prompt)

        return ReviewerOutput(**data)