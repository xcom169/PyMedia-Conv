#!/usr/bin/python3
import ffmpeg, os, sys


def process():
    cwd = os.getcwd()
    #Select video file types
    filetypes = ['mkv','mp4','avi','wmv']
    # get a list of video files in the current directory:
    filelist = filter(lambda f: f.split('.')[-1] in filetypes, os.listdir(cwd))
    filelist = sorted(filelist)

    if(filelist == []):
        print("No video files to process")
    else:
        #Encode each file
        for file in filelist:
            check(file)

        os.chdir('..')


def encodev2(file):
    inputFile = file
    #Get file extensions:
    print(file)
    filename, file_extension = os.path.splitext(inputFile)
    outputFile = filename.upper() + '.mkv'
    #Remove spaces
    outputFile = ''.join(outputFile.split())

    #Encode with ffmpeg-python
    (ffmpeg
    .input(file)
    .output(outputFile, map=0, video_size='hd720', c='copy', **{'c:a': 'ac3'}, **{'c:v': 'libx264'}, **{'preset': 'superfast'})
    .overwrite_output()
    .run()
     )



def encodev1(file):

    inputFile = file
    #Get file extensions:
    print(file)
    filename, file_extension = os.path.splitext(inputFile)
    outputFile = filename.upper() + '.mkv'
    #Remove spaces
    outputFile = ''.join(outputFile.split())

    #Encode with ffmpeg-python
    (ffmpeg
    .input(file)
    .output(outputFile, map=0, video_size='hd720', c='copy', **{'c:a': 'ac3'}, **{'c:v': 'copy'}, **{'preset': 'superfast'})
    .overwrite_output()
    .run()
     )

def check(file):
     inputFile = file
     print(file)
     probe = ffmpeg.probe(file)
     video_stream = next((stream for stream in probe['streams'] if stream['codec_type'] == 'video'), None)
     codec = video_stream['codec_name']
     print(codec)
     if codec.find("264") == -1:
         encodev2(file)
     else:
         encodev1(file)

if __name__ == "__main__":
        process()
