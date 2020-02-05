#!/usr/bin/env python3


print('Hello World!')

import ffmpeg, os, sys




def process():
    cwd = os.getcwd()
    filetypes = ['mkv','mp4','avi','wmv']
    # get a list of video files in the current directory:
    filelist = filter(lambda f: f.split('.')[-1] in filetypes, os.listdir(cwd))
    filelist = sorted(filelist)

    if(filelist == []):
        print("No video file to process")
    else:
        # encode each file
        for file in filelist:
            encode(file)

        os.chdir('..')


def encode(file):
    inputFile = file
    #Get file extensions:
    print(file)
    filename, file_extension = os.path.splitext(inputFile)
    outputFile = filename.upper() + '.mkv'

    (ffmpeg
    .input(file)
    .output(outputFile, map=0, video_size='hd720', c='copy', **{'c:a': 'ac3'})
    .run()
