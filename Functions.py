import sys
import pytube
from pytube import YouTube

MB = 1048576
check = u'\u2713'

def progress_function(stream,file_handle, bytes_remaining):
    curr = stream.filesize - bytes_remaining
    done = int(50 * curr / stream.filesize)
    percent = round(curr/stream.filesize * 100, 1)
    sys.stdout.write("\u001b[32m\r[{done}{pending}] || {percentage}% ".format(done='█' * done,pending='=' * (50 - done), percentage=percent))
    sys.stdout.flush()


def finish_function(stream, file_path):
    sys.stdout.write('\u001b[30m File Downloaded successfully {check} \nPath to file:  {path}'.format(check=check, path=file_path))


def returnUserURL():
    print('\u001b[1m\u001b[4mWELCOME TO YOUTUBE DOWNLOADER.\u001b[0m')
    print('\u001b[30mEnter youtube link below:  \u2193')
    url = str(input())
    if url and  url.startswith('https://www.youtube.com'):
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
        print('\u001b[44m\u001b[37m<>  INITIALIZING DOWNLOADER  <>\u001b[0m')
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
                return [file_name , fileSize , streamObj]
        except pytube.exceptions.VideoUnavailable:
            print('\u001b[31m- - DOWNLOAD FAILED: Video is unavailable - - ')
        except pytube.exceptions.AgeRestrictedError:
            print('\u001b[31m- - DOWNLOAD FAILED: Video is age restricted - - ')
        except pytube.exceptions.HTMLParseError:
            print('\u001b[31m- - DOWNLOAD FAILED: HTML Parsing error - -')
        except pytube.exceptions.LiveStreamError:
            print('\u001b[31m- - DOWNLOAD FAILED: LiveStreamError - - ')
        except pytube.exceptions.MaxRetriesExceeded:
            print('\u001b[31m- - DOWNLOAD FAILED: Max retries exceeded - - ')
        except pytube.exceptions.MembersOnly:
            print('\u001b[31m- - DOWNLOAD FAILED: This video is restricted to members only - - ')
        except pytube.exceptions.PytubeError:
            print('\u001b[31m- - DOWNLOAD FAILED: Downloader failed.  - - ')
        except pytube.exceptions.RecordingUnavailable:
            print('- - DOWNLOAD FAILED: This recording is unavailable - - ')
        except pytube.exceptions.VideoPrivate:
            print('- - DOWNLOAD FAILED: This video is a private video - - ')
        except pytube.exceptions.VideoRegionBlocked:
            print('- - DOWNLOAD FAILED: This video is unavailable in your region - - ')
        else:
            print('Please enter A to download Audio or V to download Video !!')



def downloadFile(file_type, file_title, streamObj, audioLocation, videoLocation):
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
