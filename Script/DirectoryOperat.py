#coding:utf-8
import logging
import os
import shutil
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

backupDir = "C:/Data/Project/Auto02/2018-08-07"
bashDir = "C:/Data/Project/Auto02/2018-08-16"

def copyFile(fromFile,toDir):
    if os.path.isdir(fromFile):
        clearDir = fromFile[len(bashDir):]
        try:
            os.makedirs(toDir + clearDir)
            print('NewFolder:',fromFile,'===>',(toDir + fromFile[len(bashDir):]))

        except :
            print('NewFolder-PASS:',fromFile)
            return
    else:
        clearDir = os.path.dirname(fromFile)[len(bashDir):]
        if not os.path.isdir(toDir + clearDir):
            os.makedirs(toDir + clearDir)
        try:
            time.sleep(0.2)
            shutil.move(fromFile,toDir + fromFile[len(bashDir):])
            print('MoveFile',fromFile,'===>',(toDir + fromFile[len(bashDir):]))
        except:
            print('MoveFile-PASS:',fromFile)
            return
    return
class FileEventHandler(FileSystemEventHandler):
    def on_any_event(self, event):
        pass
    def __init__(self,pattern='*'):
        self.pattern = pattern
    def on_moved(self,event):
        if event.is_directory:
            print("directory moved from {0} to {1}".format(event.src_path,event.dest_paht))
            # copyFile(event.dest_path, backupDir)
        else:
            print("file moved from {0} to {1}".format(event.src_path,event.dest_path))
    def on_created(self, event):
        if event.is_directory:
            print("directory created:{0}".format(event.src_path))
        else:
            print("file create:{0}".format(event.src_path))
        copyFile(event.src_path, backupDir)
    def on_deleted(self, event):
        if event.is_directory:
            print("directory deleted:{0}".format(event.src_path))
        else:
            print("file deleted:{0}".format(event.src_path))

    def on_modified(self, event):
        if event.is_directory:
            print("directory modified:{0}".format(event.src_path))

        else:
            print("file modified:{0}".format(event.src_path))
        # copyFile(event.src_path, backupDir)
if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s - %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S')
    # path = sys.argv[1] if len(sys.argv) > 1 else '.'

    # event_handler = LoggingEventHandler()
    event_handler = FileEventHandler()
    observer = Observer()
    observer.schedule(event_handler, bashDir, True)
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()