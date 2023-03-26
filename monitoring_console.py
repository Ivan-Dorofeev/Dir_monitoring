import os
import sys
import logging

from cprint import cprint
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler


class Handler(FileSystemEventHandler):
    path = './'

    def on_any_event(self, event):
        if not event.event_type in ['opened', 'closed', 'modified']:
            cprint.info('Изменения в директории', event.event_type, event.src_path)
            for path, dir, file in sorted(os.walk(self.path)):
                if path:
                    print(path)
                if file:
                    for file in sorted(file):
                        print(' -', file)


def main():
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
    path = sys.argv[1] if len(sys.argv) > 1 else './1'
    Handler.path = path

    observer = Observer()
    observer.schedule(Handler(), path, recursive=True)
    observer.start()

    while True:
        try:
            pass
        except KeyboardInterrupt:
            observer.stop()


if __name__ == "__main__":
    main()
