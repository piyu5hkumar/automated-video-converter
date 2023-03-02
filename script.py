from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import os
import time
import datetime

from dotenv import load_dotenv, find_dotenv


dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
load_dotenv(find_dotenv(), override=True)

ENV = os.environ

class MyCustomHandler(FileSystemEventHandler):
    def __init__(self, source_folder, destination_folder):
        self.source_folder = source_folder
        self.destination_folder = destination_folder

    def on_modified(self, event):
        for dir_entry in os.scandir(self.source_folder):
            if (
                dir_entry.is_file()
                and dir_entry.name.split(".").__len__() == 2
                and dir_entry.name.split(".")[1].lower() == "webm"
                and dir_entry.name.split(".")[0].startswith("screen-capture")
            ):
                try:
                    src = f"{self.source_folder}/{dir_entry.name}"
                    file_modified_timestamp = dir_entry.stat().st_mtime
                    dt_object = datetime.datetime.fromtimestamp(file_modified_timestamp)
                    formatted_date = dt_object.strftime("%d_%m_%Y_(%H:%M)")
                    dest_with_file_name = f'{self.destination_folder}/{dir_entry.name.split(".")[0]}__{formatted_date}.{dir_entry.name.split(".")[1]}'
                    os.rename(src, dest_with_file_name)
                    print(f'moved file {src}')
                except:
                    pass


event_handler = MyCustomHandler(
    source_folder=ENV.get('SRC_FOLDER'),
    destination_folder=ENV.get('DEST_FOLDER')
)

if not event_handler.source_folder or not event_handler.destination_folder:
    exit()

observer = Observer()
print('we are here', event_handler.source_folder, event_handler.destination_folder)
observer.schedule(event_handler, event_handler.source_folder, recursive=True)
observer.start()

try:
    while True:
        time.sleep(60)
except KeyboardInterrupt:
    observer.stop()
