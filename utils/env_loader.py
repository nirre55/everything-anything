# Utils/env_loader.py
import os
from dotenv import load_dotenv
from Utils.path_utils import get_single_folder_path


def load_env(env_file=".env"):
    env_path = get_single_folder_path(env_file)
    if os.path.exists(env_path):
        load_dotenv(dotenv_path=env_path)
        print(f"✅ .env loaded from {env_path}")
    else:
        print(f"⚠️ No .env file found at {env_path}")
