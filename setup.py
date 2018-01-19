import sys
from cx_Freeze import setup, Executable


# Dependencies are automatically detected, but it might need fine tuning.
build_exe_options = {
    'packages': ['pygame'],
    'excludes': ['tkinter', 'numpy', 'json', 'curses', 'urllib', 'lib2to3',
                 'xml', 'OpenGL', 'ctypes', 'email', 'html', 'logging',
                 'multiprocessing', 'xmlrpc', 'unittest', 'test', 'http',
                 'pydoc_data', '_hashlib'],
    'include_files': ['graphics', 'sounds', 'README.md', 'Credits.txt'],
    }

def find_data_file(filename):
    if getattr(sys, 'frozen', False):
        # The application is frozen
        datadir = os.path.dirname(sys.executable)
    else:
        # The application is not frozen
        # Change this bit to match where you store your data files:
        datadir = os.path.dirname(__file__)

    return os.path.join(datadir, filename)

# GUI applications require a different base on Windows (the default is for a
# console application).
base = None
if sys.platform == 'win32':
    base = 'Win32GUI'

setup(
    name = 'Länderquiz',
    version = '1.0.13',
    description = 'A geography and vexillology quiz.',
    options = {'build_exe': build_exe_options},
    executables = [Executable('länderquiz.py', base=base)]
    )
