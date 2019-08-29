#!/usr/bin/python3

import os, sys


from converter import Converter
c = Converter()

def process():
    cwd = os.getcwd()
    filetypes = ['mkv','mp4','avi','wmv']
    # get a list of files that have the extension mkv
    filelist = filter(lambda f: f.split('.')[-1] in filetypes, os.listdir(cwd))
    filelist = sorted(filelist)

    if(filelist == []):
        print("Nincs megfelelő fájl")
    else:
        # encode each file
        for file in filelist:
            encode(file)

        os.chdir('..')




def encode(file):
    print(file)

    options = {
    'format': 'mkv',
    'audio': {
        'codec': 'ac3'
    },
    'video': {
        'codec': 'h264'
    },
    'subtitle': {
        'codec': 'copy'
    },
    'map': 0
}

    optionsNoConv = {
        'format': 'mkv',
        'audio': {
            'codec': 'ac3'
        },
        'video': {
            'codec': 'copy'
        },
        'subtitle': {
            'codec': 'copy'
        },
        'map': 0
    }

    inputFile = file
    #SKiterjesztés leválasztása
    filename, file_extension = os.path.splitext(inputFile)
    outputFile = filename.upper() + '.mkv'



    info = c.probe(file)

    videoCodec = info.video.codec
    audioCodec = info.audio.codec
    fileFormat = info.format.format
    fileStreams = info.streams
    dca = False
    mFormats = ['eac3','dca']

#Is there any DCA stream? Only DCA streams should be encoded. 
    for s in fileStreams:
        if('dca' in s.codec or 'eac3' in s.codec):
             dca = True
        else:
             print("Nem DCA/eac3 stream")
    try:
        print(info.format.format)
        print(info.format.duration)
        print(audioCodec)
        print(videoCodec)

        if (videoCodec == 'h264' and dca == False and 'matroska' in fileFormat):
            raise ValueError("Nem kell átkódolni")
        elif (videoCodec != 'h264'):
            conv = c.convert(inputFile, outputFile, options)
        else:
            conv = c.convert(inputFile, outputFile, optionsNoConv)

        print(outputFile)

        for timecode in conv:
            print("Converting (%f) ...\r" % timecode)

    except:
        print('There is no need to convert')

    finally:
        # always cleanup even if there are errors
        #subprocess.call(['rm', '-fr', 'attachments'])
        print('Konvertálás kész!')


if __name__ == "__main__":
        process()
