import os
# 设置工作目录
def setup_workdir(path: str = ".")->str:
    try:
        work_dir = os.environ["WORK_DIR"]
    except KeyError:
        work_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), path))
    print(f"WORK_DIR: {work_dir}")
    os.chdir(work_dir)
    return work_dir

import openai
from dotenv import load_dotenv, find_dotenv

# 读取.env文件
def setup_env():
	_ = load_dotenv(find_dotenv())
	openai.api_key = os.getenv("OPENAI_API_KEY")