from langchain import PromptTemplate
from langchain.prompts.loading import load_prompt_from_config

from promptlytics.utils import (get_api_key, promptlytics_get_prompt,
                               promptlytics_publish_prompt)


def get_prompt(prompt_name, langchain=False, version=None):
    """
    Get a prompt template from PromptLayer.
    version: The version of the prompt to get. If not specified, the latest version will be returned.
    """
    api_key = get_api_key()
    prompt = promptlytics_get_prompt(prompt_name, api_key, version)
    if langchain:
        if "_type" not in prompt["prompt_template"]:
            prompt["prompt_template"]["_type"] = "prompt"
        return load_prompt_from_config(prompt["prompt_template"])
    else:
        return prompt["prompt_template"]


def publish_prompt(prompt_name, tags=[], prompt_template=None):
    api_key = get_api_key()
    if type(prompt_template) == dict:
        promptlytics_publish_prompt(prompt_name, prompt_template, tags, api_key)
    elif isinstance(prompt_template, PromptTemplate):
        promptlytics_publish_prompt(
            prompt_name, prompt_template.dict(), tags, api_key)
    else:
        raise Exception(
            "Please provide either a JSON prompt template or a langchain prompt template.")
