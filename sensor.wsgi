import sys
sys.path.insert(0, '/home/pi/FlaskTemperature')

from app import app
from werkzeug.debug import DebuggedApplication
application = DebuggedApplication(app, True)
