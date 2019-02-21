# simp2
simple example with import

My error
john@cave-mint18 ~/github/simp2 $ simp2
Python 3.5.2
Traceback (most recent call last):
  File "/home/john/.local/bin/simp2", line 11, in <module>
    load_entry_point('simple2', 'gui_scripts', 'simp2')()
  File "/home/john/.local/lib/python3.5/site-packages/pkg_resources/__init__.py", line 487, in load_entry_point
    return get_distribution(dist).load_entry_point(group, name)
  File "/home/john/.local/lib/python3.5/site-packages/pkg_resources/__init__.py", line 2728, in load_entry_point
    return ep.load()
  File "/home/john/.local/lib/python3.5/site-packages/pkg_resources/__init__.py", line 2346, in load
    return self.resolve()
  File "/home/john/.local/lib/python3.5/site-packages/pkg_resources/__init__.py", line 2352, in resolve
    module = __import__(self.module_name, fromlist=['__name__'], level=0)
  File "/home/john/github/simp2/simp2/simp2.py", line 15, in <module>
    import importme
ImportError: No module named 'importme'

Yet importme.py is in site-packages

john@cave-mint18 ~ $ cd .local
john@cave-mint18 ~/.local $ cd lib
john@cave-mint18 ~/.local/lib $ cd python3.5
john@cave-mint18 ~/.local/lib/python3.5 $ cd site-packages
john@cave-mint18 ~/.local/lib/python3.5/site-packages $ cd simp2
john@cave-mint18 ~/.local/lib/python3.5/site-packages/simp2 $ ls
importme.py  __init__.py  __pycache__  simp2.py

here is the output from sys.path

['/home/john/.local/bin', '/usr/lib/python35.zip', '/usr/lib/python3.5', '/usr/lib/python3.5/plat-x86_64-linux-gnu', '/usr/lib/python3.5/lib-dynload', '/home/john/.local/lib/python3.5/site-packages', '/home/john/programs/pyqt5/mainwindow', '/home/john/github/7i76e', '/home/john/github/simp2', '/usr/local/lib/python3.5/dist-packages', '/usr/lib/python3/dist-packages']
