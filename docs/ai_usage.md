# AI Use Log
- Tool/model & version: ChatGPT-5
- What I asked for: debugging errors
- Snippet of prompt(s): "Im trying to make a module so i can just get a variable with the text of a txt file in one function and one line of code (insteda of typing out open() and the path every time) and im running into this error:
  --------------------------------------------------------------------------- FileNotFoundError Traceback (most recent call last) Cell In[23], line 17 1 text = """ 2 import os 3 (...) 14 15 """ ---> 17 with open("extract_text.py") as file: 18 file.write(text) File /opt/anaconda3/lib/python3.12/site-packages/IPython/core/interactiveshell.py:324, in _modified_open(file, *args, **kwargs) 317 if file in {0, 1, 2}: 318 raise ValueError( 319 f"IPython won't let you open fd={file} by default " 320 "as it is likely to crash IPython. If you know what you are doing, " 321 "you can use builtins' open." 322 ) --> 324 return io_open(file, *args, **kwargs) FileNotFoundError: [Errno 2] No such file or directory: 'extract_text.py'"
- What I changed before committing: Adding the "w" argument to an open() statement
- How I verified correctness (tests, sample data): I realized I'd forgotten the "w" argument when trying to create a new file using open()
