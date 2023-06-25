import os
import sys
from pathlib import Path

from llama_index import download_loader

# 从同级目录下的utils目录中导入setup_workdir和setup_env函数
# sys.path.insert(0, os.path.expanduser("~")+"/langchain-ChatGLM")
sys.path.insert(0, os.path.dirname(__file__) + "/../..")
from utils.base import setup_env, setup_workdir

setup_workdir(os.path.dirname(__file__))
UnstructuredReader = download_loader("UnstructuredReader")

loader = UnstructuredReader()
documents = loader.load_data(file=Path("./10k_filing.html"))
print(f"Number of documents: {len(documents)}")
print(f"First document: {documents[0]}")
