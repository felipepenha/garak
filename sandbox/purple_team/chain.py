import toml
import sys
import torch
from langchain_core.prompts import PromptTemplate
from langchain_community.llms import HuggingFacePipeline
from langchain_core.output_parsers import StrOutputParser
import transformers


def get_prompt_file():
    try:
        with open("config/prompt.toml", "r") as f:
            config = toml.load(f)
            return config.get("prompt_file")
    except FileNotFoundError:
        print("Error: prompt.toml not found.")
        return None
    except Exception as e:
        print(f"Error reading prompt.toml: {e}")
        return None

def get_pipeline():
    # 1. Load the system prompt
    prompt_file = get_prompt_file()
    if not prompt_file:
        return None

    try:
        with open(prompt_file, "r") as f:
            system_prompt = f.read()
    except FileNotFoundError:
        print(f"Error: {prompt_file} not found.")
        print("Please make sure the prompt file exists in the correct location.")
        return None

    # 2. Create a PromptTemplate
    template = system_prompt + "\n\n{user_input}"
    prompt_template = PromptTemplate.from_template(template)

    # 3. Instantiate the LLM (replace with your desired LLM)
    try:
        with open("config/llm.toml", "r") as f:
            config = toml.load(f)
            model_id = config.get("llm", {}).get("model_id")
            pipeline_kwargs = config.get("pipeline", {})
    except FileNotFoundError:
        print("Error: llm.toml not found.")
        return None
    except Exception as e:
        print(f"Error reading llm.toml: {e}")
        return None

    try:
        llm = HuggingFacePipeline.from_model_id(
            model_id=model_id,
            task="text-generation",
            device_map="auto",
            pipeline_kwargs=pipeline_kwargs,
            model_kwargs={"trust_remote_code": True},
        )
    except ImportError:
        print("Error: langchain-community or transformers is not installed. Please install it with 'pip install langchain-community transformers'")
        return None
    except Exception as e:
        print(f"Error: {e}")
        return None

    # 4. Create the pipeline
    return prompt_template | llm | StrOutputParser()

pipeline = get_pipeline()

def generate(prompt: str) -> list[str]:
    if pipeline is None:
        return ["Pipeline not initialized."]
    return [pipeline.invoke({"user_input": prompt})]

if __name__ == "__main__":
    if pipeline is None:
        exit()
    print("Running chain example...")
    if len(sys.argv) > 1:
        user_input = sys.argv[1]
    else:
        user_input = "Who are you?"
    print(f"User: {user_input}")
    response = generate(user_input)
    print(f"AI: {response[0]}")
