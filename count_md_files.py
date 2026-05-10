#!/usr/bin/python3
import os

path = "prompt_patterns_library/prompts"

if os.path.exists(path):
    files = [f for f in os.listdir(path) if f.endswith('.md')]
    print(len(files))
else:
    print(0)
