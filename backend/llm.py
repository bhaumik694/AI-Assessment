from groq import Groq
import os
import json
from dotenv import load_dotenv

load_dotenv()

client = Groq(api_key="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")


def call_llm_json(prompt: str):
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "system",
                "content": "Return ONLY valid JSON. No explanation, no text, no markdown."
            },
            {"role": "user", "content": prompt}
        ],
        temperature=0
    )

    content = response.choices[0].message.content.strip()

    print("RAW LLM OUTPUT:\n", content)  # 🔥 debug

    try:
        return json.loads(content)

    except:
        # 🔥 Extract JSON manually
        import re

        match = re.search(r"\{.*\}", content, re.DOTALL)

        if match:
            return json.loads(match.group())

        raise ValueError("LLM did not return valid JSON")