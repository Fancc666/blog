from datetime import datetime
import os

ROOT = os.path.dirname(os.path.abspath(__file__))

theme = input("主题:")

time_day = datetime.strftime(datetime.now(), "%Y-%m-%d")
time_minu = datetime.strftime(datetime.now(), "%Y-%m-%d %H:%M")

template = f"""---
title: {theme}
date: {time_minu}
tags: []
categories: []
---
"""

with open(os.path.join(ROOT, f"./_posts/{time_day}-{theme}.md"), 'w') as f:
    f.write(template)

print("Generate", f"{time_day}-{theme}.md", "success")
