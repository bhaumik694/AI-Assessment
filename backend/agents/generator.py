from backend.llm import call_llm_json
from backend.schemas import GeneratorOutput


class GeneratorAgent:

    def generate(self, grade, topic, feedback=None):

        prompt = f"""
        Create educational content.

        Grade: {grade}
        Topic: {topic}

        {f"Fix based on feedback: {feedback}" if feedback else ""}

        Rules:
        - Simple language for the grade
        - 5 MCQs only
        - Each MCQ must have 4 options

        Output STRICT JSON:
        {{
          "explanation": "...",
          "mcqs": [
            {{
              "question": "...",
              "options": ["A","B","C","D"],
              "answer": "A"
            }}
          ]
        }}
        """

        data = call_llm_json(prompt)

        return GeneratorOutput(**data)