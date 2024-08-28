import sys, os
# INTERP = os.path.join(os.environ['HOME'], 'deleteplastic.io', 'venv', 'bin', 'python3')
INTERP = os.path.expanduser("~/venv/bin/python3")
if sys.executable != INTERP:
    os.execl(INTERP, INTERP, *sys.argv)
sys.path.append(os.getcwd())
sys.path.append('~/deleteplastic.io/app')
from app.app import app as application

if __name__ == '__main__':
    application.run(debug=False)



