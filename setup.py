import sys
import subprocess

packagelist = [
                'numpy',
                'scipy',
                'matplotlib',
                'Numba',
                'lxml',
                'pymodbus',
                'python-dateutil', #is a dependency for now, but still a first-class package
                'Markdown',
                'pyserial',
                'lxml',
                'Markdown',
                'Python-docx',
                'Tensorflow',
                'Keras',
                'pyinstaller',
                
]

for p in packagelist:
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', p])