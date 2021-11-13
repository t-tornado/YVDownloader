import pytube.request
import os
from Functions import returnUserURL, getDownloadFileFormat, init_getFileDetails, downloadFile

hostname = os.environ['HOME']


pytube.request.default_range_size = 1048576
videoLocation = '{}/Downloads/Video'.format(hostname)
audioLocation = '{}/Downloads/Music'.format(hostname)



def __start_downloader__():
    global URL
    global File_Format
    global File_Title
    global File_Size
    URL = returnUserURL()
    if(type(URL) == str):
        File_Type = getDownloadFileFormat()
        init_results = init_getFileDetails(File_Type, URL)
        try:
            [File_Title, File_Size, streamObj] = init_results
            downloadFile(File_Type, File_Title, streamObj, audioLocation, videoLocation)
        except:
            print('')
    elif(URL == None):
        print('\u001b[31mXX \u001b[1m- - Enter a valid youtube link - - XX')

__start_downloader__()
