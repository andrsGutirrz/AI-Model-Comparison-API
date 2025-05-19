# AI Model Comparison API

A Flask API that enables direct comparison between OpenAI's ChatGPT and Anthropic's Claude responses through their APIs. Compare different model versions and generations side by side.

## Features

- Single endpoint to query both AI models simultaneously
- Configurable model selection for both providers
- JSON-based request/response format

## API Documentation

### POST /chat

Compare responses between ChatGPT and Claude models.

#### Request

```json
{
  "prompt": "What is the meaning of life?",
  "chatgpt_model": "gpt-4",  // optional, defaults to "gpt-4o-mini"
  "claude_model": "claude-3-sonnet-20240229" // optional, defaults to "claude-3-7-sonnet-20250219"
}
```

#### Response

```json
{
  "prompt": "What is the meaning of life?",
  "chatgpt_response": "The meaning of life is...",
  "claude_response": "From a philosophical perspective..."
}
```

## Real example

### gpt-4.1 vs claude-3-haiku-20240307

```json
{
    "prompt": "act as python developer, how to do a hello world in python. Keep it short",
    "chatgpt_response": "```python\nprint(\"Hello, world!\")\n```",
    "claude_response": "```python\nprint(\"Hello, World!\")\n```"
}
```

### gpt-4o-mini vs claude-3-7-sonnet-20250219

```json
{
    "prompt": "act as python developer, how to do a hello world in python. Keep it short",
    "chatgpt_response": "To print \"Hello, World!\" in Python, simply use the `print` function. Here's the code:\n\n```python\nprint(\"Hello, World!\")\n```\n\nRun this code in your Python environment, and it will display the message.",
    "claude_response": "# Hello World in Python\n\n```python\nprint(\"Hello, World!\")\n```\n\nThat's it! Just save this in a file with `.py` extension (e.g., `hello.py`) and run it with `python hello.py` from your command line."
}
```

## Requirements

### API Keys and Credits

1. **OpenAI API Key**
   - Create an account at [OpenAI Platform](https://platform.openai.com)
   - Generate an API key
   - Minimum recommended balance: $5 USD

2. **Anthropic API Key**
   - Create an account at [Anthropic Console](https://console.anthropic.com)
   - Generate an API key
   - Minimum recommended balance: $5 USD

### Environment Variables

Create a `.env` file in the project root:

```env
openai_api_key=your-openai-key-here
anthropic_api_key=your-anthropic-key-here
```

### Installation

```bash
pip install -r requirements.txt
```

### How to run

#### Via VSCODE
Withing this repo you will find `.vscode/launch.json` which enables you to run the app using the Run and Debug menu.

#### Via terminal
1. Enable the following env variables
  - `export FLASK_APP=app/main.py`
  - `export PYTHONPATH="${PYTHONPATH}:/path/to/AI-Model-Comparison-API"`
  - Run the app. `flask run`

## Available Models

### OpenAI Models
- GPT-4 Turbo
- GPT-4
- GPT-3.5 Turbo
- [Full list of OpenAI models](https://platform.openai.com/docs/models)
- [Check your model access](https://platform.openai.com/settings/organization/limits)

### Anthropic Models
- Claude 3 Opus
- Claude 3 Sonnet
- Claude 2.1
- [Full list of Anthropic models](https://docs.anthropic.com/en/api/models-list)

## Dashboard

Access your usage and credits:
- OpenAI: [Usage Dashboard](https://platform.openai.com/usage)
- Anthropic: [Console Dashboard](https://console.anthropic.com/settings/usage)

## Disclaimer

This is a weekend project created as my first exploration into AI APIs from a developer's perspective. The main goal is learning and understanding how to interact with different AI models programmatically. While functional, this project is:

- Built for educational purposes
- A learning experiment with AI APIs
- Not intended for production use
- Open to improvements and suggestions
- Created to compare different AI models' responses

Feel free to use this as a starting point for your own AI API exploration journey!

