from pytube import YouTube
import pytube.request
import sys

pytube.request.default_range_size = 1048576
downloadType = 'audio'
audioPath = '/home/tornado/Downloads/Music'
videoPath = '/home/tornado/Downloads/Video'
URL = 'https://www.youtube.com/watch?v=S39Z6PPC1FM'


def progress_func(stream, chunk, bytes_remaining):
    curr = stream.filesize - bytes_remaining
    done = int(50 * curr / stream.filesize)
    sys.stdout.write("[\r{}{}] ".format('=' * done, ' ' * (50-done)) )
    sys.stdout.flush()

streamObj = YouTube(URL)
streamObj.register_on_progress_callback(progress_func)
streamObj.streams.filter(only_audio=True).desc().first().download(output_path=audioPath, filename=streamObj.title)
