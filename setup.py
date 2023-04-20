from setuptools import find_packages, setup

try:
    # read the contents of your README file
    from pathlib import Path
    this_directory = Path(__file__).parent
    long_description = (this_directory / "README.md").read_text()
except:
    long_description = ""

setup(
    name="promptlytics",
    description="Promptlytics is a package to keep track of your GPT models training",
    long_description=long_description,
    long_description_content_type='text/markdown',
    author="Chinmay",
    author_email="chinmay@hybrowlabs.com",
    url="https://www.promptlytics.com",
    project_urls={"Documentation": "https://magniv.notion.site/Prompt-Layer-Docs-db0e6f50cacf4564a6d09824ba17a629",},
    version="0.1.80",
    py_modules=["promptlytics"],
    packages=find_packages(),
    install_requires=["requests", "openai", "langchain"],
)
