import os
from pathlib import Path
from openai import OpenAI, APIStatusError, RateLimitError

env_path = Path(__file__).resolve().parent.parent / ".env"
if env_path.exists():
    for line in env_path.read_text(encoding="utf-8").splitlines():
        if line.strip() and not line.startswith("#") and "=" in line:
            key, value = line.split("=", 1)
            os.environ.setdefault(key.strip(), value.strip())

api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise RuntimeError("OPENAI_API_KEY is not set. Add it to your environment before running this script.")

client = OpenAI(api_key=api_key)

messages = [
    {
        "role": "system",
        "content": "You are going to act as a storyteller with my prompts."
    },
    {
        "role": "user",
        "content": "Tell me a short fantasy story about a lost lantern."
    }
]

try:
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=messages,
        temperature=0.7,
    )
    print(response.choices[0].message.content)
except (RateLimitError, APIStatusError) as e:
    print(f"OpenAI request failed: {e}")
    print("This usually means your API quota is exhausted or your billing plan needs attention.")