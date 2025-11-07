import anthropic
import os
import subprocess

client = anthropic.Anthropic(api_key=os.environ.get("ANTHROPIC_API_KEY"))

# Get the diff
diff = subprocess.check_output(['git', 'diff', 'HEAD~1']).decode('utf-8')

message = client.messages.create(
    model="claude-sonnet-4-20250514",
    max_tokens=4000,
    messages=[{
        "role": "user",
        "content": f"Please review this code change and provide feedback on potential bugs, security issues, and code quality:\n\n{diff}"
    }]
)

print(message.content[0].text)