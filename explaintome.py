import openai
import sys

OPENAI_API_KEY = "YOURAPIKEY"
openai.api_key = OPENAI_API_KEY

# Check that a filename has been provided as a command line argument
if len(sys.argv) < 2:
    print("Please provide a filename as a command line argument.")
    sys.exit(1)

filename = sys.argv[1]

try:
    with open(filename, 'r') as file:
        code = file.read()
except Exception as e:
    print(f"Failed to read file: {e}")
    sys.exit(1)

def explain_code(code):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a knowledgeable AI trained to explain Python code."},
            {"role": "user", "content": f"Please explain the following code:\n{code}"},
        ],
        max_tokens=2048,
        temperature=0.7,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0,
    )

    explanation = response['choices'][0]['message']['content'].strip()
    return explanation

try:
    print(explain_code(code))
except Exception as e:
    print(f"Failed to generate explanation: {e}")
    sys.exit(1)
