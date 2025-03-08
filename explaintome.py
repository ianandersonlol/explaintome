import argparse
import os
import sys
from pathlib import Path
from openai import OpenAI

def parse_arguments():
    parser = argparse.ArgumentParser(description='Explain code using OpenAI models')
    parser.add_argument('file', help='Path to the file containing code to explain')
    parser.add_argument('--model', default='gpt-4o', help='OpenAI model to use (default: gpt-4o)')
    parser.add_argument('--output', help='Path to save explanation (optional)')
    parser.add_argument('--markdown', action='store_true', help='Save explanation as markdown')
    return parser.parse_args()

def read_file(file_path):
    try:
        with open(file_path, 'r') as file:
            return file.read()
    except Exception as e:
        print(f"Failed to read file: {e}")
        sys.exit(1)

def explain_code(code, model):
    api_key = os.environ.get('OPENAI_API_KEY')
    if not api_key:
        print("Error: OPENAI_API_KEY environment variable not set.")
        print("Set it with: export OPENAI_API_KEY='your-api-key'")
        sys.exit(1)
    
    client = OpenAI(api_key=api_key)
    
    try:
        response = client.chat.completions.create(
            model=model,
            messages=[
                {"role": "system", "content": "Your name is BinkyBonky. You're a friendly AI robot programmed to explain code clearly and accurately. Keep explanations helpful, practical, and occasionally add a touch of playful enthusiasm. Focus on making complex concepts accessible without sacrificing technical accuracy."},
                {"role": "user", "content": f"Please explain the following code and how to use it:\n\n{code}"}
            ],
            max_tokens=2048,
            temperature=0.7
        )
        
        explanation = response.choices[0].message.content.strip()
        return explanation
    except Exception as e:
        print(f"API error: {e}")
        sys.exit(1)

def generate_markdown(code, explanation, file_path):
    file_name = Path(file_path).name
    
    client = OpenAI(api_key=os.environ.get('OPENAI_API_KEY'))
    
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You convert plain text code explanations into well-formatted markdown documentation."},
                {"role": "user", "content": f"Convert this explanation of {file_name} into well-formatted markdown with appropriate headers, code blocks, and sections:\n\nCode:\n```\n{code}\n```\n\nExplanation:\n{explanation}"}
            ],
            max_tokens=2048,
            temperature=0.7
        )
        
        markdown = response.choices[0].message.content.strip()
        return markdown
    except Exception as e:
        print(f"Failed to generate markdown: {e}")
        # Fall back to basic markdown
        return f"# {file_name} Explanation\n\n## Code\n\n```\n{code}\n```\n\n## Explanation\n\n{explanation}"

def save_output(content, output_path):
    try:
        with open(output_path, 'w') as file:
            file.write(content)
        print(f"Explanation saved to {output_path}")
    except Exception as e:
        print(f"Failed to save output: {e}")
        sys.exit(1)

def main():
    args = parse_arguments()
    
    code = read_file(args.file)
    
    print(f"Generating explanation using {args.model}, please wait...")
    explanation = explain_code(code, args.model)
    
    if args.output:
        if args.markdown:
            print("Generating markdown documentation...")
            content = generate_markdown(code, explanation, args.file)
            output_path = args.output if args.output.endswith('.md') else f"{args.output}.md"
        else:
            content = explanation
            output_path = args.output if args.output.endswith('.txt') else f"{args.output}.txt"
        
        save_output(content, output_path)
    
    print(explanation)

if __name__ == "__main__":
    main()