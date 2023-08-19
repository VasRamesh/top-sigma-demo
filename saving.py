import pickle
import os

def save_with_pkl(videos: list):
    path = "videos.pkl"
    if not os.path.exists(path):
        with open(path, "wb") as f:
            pickle.dump(videos, f)
            print(f"Saved to {path}!")
    else:
        print(f"File already exists at {path}. Delete this before re-saving")

def check_exists(path: str)-> bool:
    if os.path.exists(path): return True
    else: return False

