import os

import openai
from promptlytics.langchain.chat_models import PromptLyticsChatOpenAI
from promptlytics.langchain.llms import PromptLyticsOpenAIChat

import promptlytics

promptlytics.api_key = os.environ.get("PROMPTLYTICS_API_KEY")
openai = promptlytics.openai
openai.api_key = os.environ.get("OPENAI_API_KEY")


def before_all(context):
    context.openai = openai
    context.langchain_chat_openai = PromptLyticsChatOpenAI()
    context.langchain_openai_chat = PromptLyticsOpenAIChat()
