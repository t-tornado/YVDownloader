#!/home/tornado/anaconda3/bin/python3

from pytube import YouTube
import pytube.request
import sys

pytube.request.default_range_size = 1048576
downloadPath = '/home/tornado/Download/Video'
global completeMessage

def progress_func(stream, chunk, bytes_remaining):
    curr = stream.filesize - bytes_remaining
    done = int(50 * curr / stream.filesize)
    sys.stdout.write("[\r{}{}] ".format('=' * done, ' ' * (50-done)) )
    sys.stdout.flush()


def complete_func():
    sys.stdout.write("\r{}".format(completeMessage))
    sys.stdout.flush()


def downloadError():
    sys.stdout.write('-- ERROR -- Download Failed. Try again')


try:
    print('Enter video URL')
    inputURL = str(input())
    streamObj = YouTube(inputURL, on_progress_callback=progress_func, on_complete_callback=complete_func)
    filename = streamObj.title
    videoObject = streamObj.streams.get_by_resolution(720)
    print(videoObject)
except:
    downloadError()