import os

os.chdir('../..')
os.environ['CG_ROOT_FOLDER'] = os.path.abspath(os.curdir)
print(os.environ['CG_ROOT_FOLDER'])