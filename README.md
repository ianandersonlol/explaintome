# ExplainToMe

`explaintome.py` is a Python script that uses OpenAI models to generate explanations of code. It reads code from a file provided as a command line argument, sends that code to the OpenAI API, and prints the generated explanation.

## Requirements

- Python 3.7 or later
- OpenAI Python package (can be installed via `pip install openai`)
- OpenAI API key

## Setting Up OpenAI Developer Account and API Key

1. Visit the OpenAI website at [https://www.openai.com/](https://www.openai.com/).
2. Click on the "Sign Up" button and create an account.
3. After verifying your email address and logging in, navigate to the API section.
4. In the API section, you will find your API key. Copy this key and keep it safe.
5. Set your API key as an environment variable:
   ```
   export OPENAI_API_KEY='your-api-key'
   ```

## Usage

Basic usage:
```
python explaintome.py path/to/your/code.py
```

Advanced options:
```
python explaintome.py path/to/your/code.py --model gpt-3.5-turbo --output explanation --markdown
```

### Command Line Arguments

- `file`: Path to the file containing code to explain (required)
- `--model`: OpenAI model to use (default: gpt-4o)
- `--output`: Path to save explanation (optional)
- `--markdown`: Save explanation as markdown (optional)

## Examples

Simple explanation:
```
python explaintome.py example.py
```

Using a different model and saving to a file:
```
python explaintome.py example.py --model gpt-3.5-turbo --output explanation
```

Generate markdown documentation:
```
python explaintome.py example.py --output docs/explanation --markdown
```

## Disclaimer

While OpenAI models are powerful tools, they are not infallible. They may not always generate perfect explanations, particularly for complex or poorly written code. Always review the generated explanations and use your own judgment.