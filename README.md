# Wrapper for various LLM models
Often we require to make calls to different language models. In this repo, we have a simple wrapper for various model providers. 

Requirements:
- There is a `requirements.txt` file that has the necessary files to pip install. 
- Make sure to have a `secrets.json` file with the API keys. The structure of the API keys can be found below.

-----

To use the code simply go to the root directory and run `pip install -e .`. Afterwards, you should be able to import models.

```python
from llm_wrappers.models import OpenAIModel, HumanMessage

# Create an instance of the OpenAIModel
model = OpenAIModel()

# Use the model to process a HumanMessage
response = model([HumanMessage('Hello')])
```

### Structure of secrets.json

```json
{
    "openai": {
        "key1": "value1",
        "key2": "value2"
    },
    "azure": {
        "lab_key": "value3"
    }
}```

For all the providers have a key and all the keys.