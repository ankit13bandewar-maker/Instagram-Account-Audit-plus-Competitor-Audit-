import os

# Delegate to build_pdf_v2.py logic for consistent PDF template generation
with open("build_pdf_v2.py", "r", encoding="utf-8") as f:
    code = f.read()

exec(code)
