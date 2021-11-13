from pytube import YouTube
import pytube.request
import sys

# Tasks
# Print an alert to user to receive video URL from terminal
# Request whether the file should be audio or video.
#  Display file information
# Pass URL to the download file functon.
# Display progress of download
# Show popup when download completes


MB = 1048576
pytube.request.default_range_size = 1048576
videoLocation = '/home/tornado/Downloads/Video'
audioLocation = '/home/tornado/Downloads/Music'

def progress_function(stream,file_handle, bytes_remaining):
    curr = stream.filesize - bytes_remaining
    done = int(50 * curr / stream.filesize)
    percent = round(curr/stream.filesize * 100, 1)
    sys.stdout.write("\r[{done}{pending}] || {percentage}% ".format(done='█' * done,pending='=' * (50 - done), percentage=percent))
    sys.stdout.flush()


def finish_function(stream, file_path):
    sys.stdout.write(' File Downloaded successfully \nPath to file:  {path}'.format(path=file_path))
def returnUserURL():
    print('WELCOME TO YOUTUBE DOWNLOADER.')
    print('Enter youtube link below:  ')
    url = str(input())
    if url and  url.startswith('http://www.youtube.com'):
        return url
    else:
        return None

def getDownloadFileFormat():
    print('Download Audio or Video? [A/V]')
    format = str(input())
    file_format = 'Video' if format == "V" else "Audio" if format == "A" else "invalid"
    return  file_format

def init_getFileDetails(fileType,url):
    if(fileType and fileType != "invalid"):
        print('<>  INITIALIZING DOWNLOADER  <>')
        try:
            StreamObj = YouTube(url, on_progress_callback=progress_function, on_complete_callback=finish_function)
            file_name = StreamObj.title
            if (fileType and fileType == 'Audio'):
                streamObj = StreamObj.streams.filter(only_audio=True).desc().first()
                fileSize = streamObj.filesize_approx
                fileSize /= MB
                fileSize = round(fileSize, 2)
                return [file_name, fileSize,streamObj]
            elif (fileType and fileType == 'Video'):
                streamObj = StreamObj.streams.get_highest_resolution()
                fileSize = streamObj.filesize_approx
                fileSize /= MB
                fileSize = round(fileSize, 2)
                return [file_name if file_name else None , fileSize if fileSize else None, streamObj if streamObj else None]
        except pytube.exceptions.VideoUnavailable:
            print('- - DOWNLOAD FAILED: Video is unavailable - - ')
        except pytube.exceptions.AgeRestrictedError:
            print('- - DOWNLOAD FAILED: Video is age restricted - - ')
        except pytube.exceptions.HTMLParseError:
            print('- - DOWNLOAD FAILED: HTML Parsing error - -')
        except pytube.exceptions.LiveStreamError:
            print('- - DOWNLOAD FAILED: LiveStreamError - - ')
        except pytube.exceptions.MaxRetriesExceeded:
            print('- - DOWNLOAD FAILED: Max retries exceeded - - ')
        except pytube.exceptions.MembersOnly:
            print('- - DOWNLOAD FAILED: This video is restricted to members only - - ')
        except pytube.exceptions.PytubeError:
            print('- - DOWNLOAD FAILED: Downloader failed.  - - ')
        except pytube.exceptions.RecordingUnavailable:
            print('- - DOWNLOAD FAILED: This recording is unavailable - - ')
        except pytube.exceptions.VideoPrivate:
            print('- - DOWNLOAD FAILED: This video is a private video - - ')
        except pytube.exceptions.VideoRegionBlocked:
            print('- - DOWNLOAD FAILED: This video is unavailable in your region - - ')
        else:
            print('Please enter A to download Audio or V to download Video !!')


def downloadFile(file_type, file_title, streamObj):
    try:
       if(file_type and file_type == 'Audio'):
           print('-- Starting Audio Download --')
           streamObj.download(output_path=audioLocation, filename=file_title)
           print('- -  DOWNLOAD SUCCESSFUL - - ')
       elif(file_type and file_type == 'Video'):
           print('--- Starting Video download --')
           streamObj.download(output_path=videoLocation, filename=file_title)
    except:
        print('- - An error might have occured. Please try again - -')

def display_init_complete():
    sys.stdout.write('- - Download Initializing complete - - ')


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
            downloadFile(File_Type, File_Title, streamObj)
        except:
            print('')
    elif(URL == None):
        print('XX - - Enter a valid youtube link - - XX')

__start_downloader__()