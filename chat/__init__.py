
from . import chatbot
import os

print('__name__:', __name__, ', pid:', os.getpid(), ', RUN_MAIN:', os.environ.get('RUN_MAIN'))

# Will not init in auto-reloader process.
if os.environ.get('RUN_MAIN') == 'true':
    chatbot.try_start_bot()