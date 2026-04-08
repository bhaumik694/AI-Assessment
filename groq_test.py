from groq import Groq

# 🔴 PASTE YOUR KEY DIRECTLY HERE (no env)
client = Groq(api_key="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")

res = client.chat.completions.create(
    model="llama-3.3-70b-versatile",
    messages=[{"role": "user", "content": "hello"}]
)

print(res.choices[0].message.content)