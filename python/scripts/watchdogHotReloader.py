import os
import sys
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

# HOW TO USE: Save this file in the same directory as your project.
# then do: python watchdogHotReloader.py

class MyEventHandler(FileSystemEventHandler):
    def on_any_event(self, event):
        if event.src_path.endswith('.py'):  # Specify the file extension(s) to watch
            print('Restarting the application...')
            time.sleep(1)  # Give some time for the file modifications to complete
            python = sys.executable
            os.execl(python, python, *sys.argv)

if __name__ == '__main__':
    event_handler = MyEventHandler()
    observer = Observer()
    observer.schedule(event_handler, path='.', recursive=True)  # Specify the directory to watch
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()

    observer.join()

