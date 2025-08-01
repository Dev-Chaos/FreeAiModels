# FreeAiModels
Free OpenAI-compatible API providing access to powerful AI models.
- **To Get Free Api Key Please Contact Me:** [◜𝙑ꫀꪀ᥆ꪑ◞](https://t.me/e_e_9_9)

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

### Basic Usage
```python
from openai import OpenAI


client = OpenAI(
    api_key="Venom",
    base_url="https://venom-ai-apis.vercel.app"
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
### Use DeepSearch
```python
from openai import OpenAI


client = OpenAI(
    api_key="Venom",
    base_url="https://venom-ai-apis.vercel.app"
)


chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": '''Who is the current president of Syria?''',
            "deepsearch": True,
        },

    ],
    model="grok-4",
    
)
 
print(chat_completion.choices[0].message.content)

```
### Models Accept DeepSearch
- **Grok 4:** `grok-4`
- **Grok 3:** `grok-3`
- **Qwen V2.5 VL:** `qwen-v2.5-vl`
- **Gemini 1.5 Flash:** `gemini-1.5-flash`
- **Llama 4 Socut:** `llama-4-socut`
- **Llama 4 Maverick:** `llama-4-maverick`

### Send Image
```python
import base64
from openai import OpenAI


client = OpenAI(
    api_key="Venom",
    base_url="https://venom-ai-apis.vercel.app"
)


# Function to encode the image
def encode_image(image_path):
  with open(image_path, "rb") as image_file:
    return base64.b64encode(image_file.read()).decode('utf-8')

# Getting the base64 string
base64_image = encode_image("Path/to/agi/image.jpeg")


chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": '''what in this image''',
             'data': {
                'imagesData': [
                    {
         
                        'contents': 'data:image/jpeg;base64,'+base64_image,
                    },
                ]},
        },

    ],
    model="grok-4",
)

 
print(chat_completion.choices[0].message.content)
```

### Models Accept Images
- **Grok 4:** `grok-4`
- **Grok 3:** `grok-3`
- **Qwen V2.5 VL:** `qwen-v2.5-vl`
- **Gemini 1.5 Flash:** `gemini-1.5-flash`
- **Llama 4 Socut:** `llama-4-socut`
- **Llama 4 Maverick:** `llama-4-maverick`


## Support 
- **Dev**: [◜𝙑ꫀꪀ᥆ꪑ◞](https://t.me/e_e_9_9)
- **Channel**: [CadoAi 🤖](https://t.me/CadoAi) 
