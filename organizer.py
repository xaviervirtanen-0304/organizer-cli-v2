#!/usr/bin/env python3
"""Sort files by extension into subfolders."""
import os, shutil, argparse
MAP = {"pdf": "docs", "jpg": "images", "png": "images", "mp4": "videos", "zip": "archives", "mp3": "audio"}
def main():
      ap = argparse.ArgumentParser(); ap.add_argument("folder"); ap.add_argument("--dry-run", action="store_true")
      a = ap.parse_args(); folder = os.path.expanduser(a.folder); moved = 0
      for name in os.listdir(folder):
                p = os.path.join(folder, name)
                if not os.path.isfile(p): continue
                          ext = name.rsplit(".", 1)[-1].lower() if "." in name else "others"
                d = os.path.join(folder, MAP.get(ext, "others")); os.makedirs(d, exist_ok=True)
                if not a.dry_run: shutil.move(p, os.path.join(d, name))
                          moved += 1
            print(f"{'[DRY] ' if a.dry_run else ''}moved {moved}")
if __name__ == "__main__": main()
  
