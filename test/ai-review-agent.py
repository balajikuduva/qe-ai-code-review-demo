import subprocess
import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

# Get code diff
diff = subprocess.check_output(
    ["git", "diff", "origin/main...HEAD"]
).decode()

prompt = f"""
You are a Corporate Quality Engineering reviewer.

Review the following code changes and identify:

- security issues
- coding standard violations
- performance issues
- missing tests
- maintainability problems

Code changes:

{diff}

Provide clear feedback and suggested fixes.
"""

response = openai.ChatCompletion.create(
    model="gpt-4o",
    messages=[{"role": "user", "content": prompt}]
)

print(response.choices[0].message.content)
