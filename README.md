# FreeAiModels
A curated collection of open-source AI models compatible with OpenAI.


## Available Models 🤖
### 1. DeepSeek
- **DeepSeek V3:** `deepseek-v3`
- **DeepSeek R1:** `deepseek-r1`

### 2. Google
- **Gemini 1.5 Flash:** `gemini-1.5-flash`
- **Gemini 2.0 Flash:** `gemini-2.0-flash`
- **Gemini 2.5 Flash:** `gemini-2.5-flash`

### 3. Meta
- **Llama 4 Socut:** `llama-4-socut`
- **Llama 4 Maverick:** `llama-4-maverick`

### 4. Anthropic
- **Claude 4 Sonnet:** `claude-4-sonnet`
- **Claude 3.7 Sonnet:** `claude-3.7-sonnet`
- **Claude 3.5 Sonnet:** `claude-3.5-sonnet`

### 5. Qwen
- **Qwen V2.5 VL:** `qwen-v2.5-vl`

### 6. xAi
- **Grok 4:** `grok-4`
- **Grok 3:** `grok-3`

### 7. OpenAI
- **Gpt 4.1 Mini:** `gpt-4.1-mini`
- **Gpt 4.1 Nano:** `gpt-4.1-nano`
- **Gpt 4 Turbo:** `gpt-4-turbo`


## How To Use 📚

### Installation
```bash
pip install openai
```

## Basic Usage
```python
from openai import OpenAI


client = OpenAI(
    api_key="Venom",
    base_url="http://127.0.0.1:5000"
)


chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": '''Hi''',

        },

    ],
    model="gemini-2.5-flash",
)

 
print(chat_completion.choices[0].message.content)

```
