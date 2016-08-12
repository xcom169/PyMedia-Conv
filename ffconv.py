import os, sys

from converter import Converter
c = Converter()

def process():
    cwd = os.getcwd()

    # get a list of files that have the extension mkv
    filelist = filter(lambda f: f.split('.')[-1] == 'mp4', os.listdir(cwd))
    filelist2 = filter(lambda f: f.split('.')[-1] == 'mkv', os.listdir(cwd))
    filelist = sorted(filelist)
    filelist2 = sorted(filelist2)

    print(filelist2)
    print(filelist)

    if(filelist == [] or filelist2 == []):
        print("Nincs megfelelő fájl")


    # encode each file
    for file in filelist:
        encode(file)

    for file in filelist2:
        encode(file)

    os.chdir('..')

def encode(file):
    global index
    index = 1
    print(file)

    options = {
    'format': 'mkv',
    'audio': {
        'codec': 'ac3',
        'samplerate': 11025,
        'channels': 2
    },
    'video': {
        'codec': 'h264',
        'width': 720,
        'height': 400,
        'fps': 15
    },
    'subtitle': {
        'codec': 'copy'
    },
    'map': 0
}

    optionsNoConv = {
        'format': 'mkv',
        'audio': {
            'codec': 'ac3',
            'samplerate': 11025,
            'channels': 2
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
    outputFile = inputFile[0:20].upper() + index.__str__() + 'conv' + '.mkv'

    try:

        info = c.probe(file)

        videoCodec = info.video.codec
        audicoCodec = info.audio.codec

        print(info.format.format)
        print(info.format.duration)
        print(audicoCodec)
        print(videoCodec)

        if (videoCodec != 'h264'):
            conv = c.convert(inputFile, outputFile, options)
        else:
            conv = c.convert(inputFile, outputFile, optionsNoConv)


        for timecode in conv:
            print("Converting (%f) ...\r" % timecode)



    finally:
        # always cleanup even if there are errors
        #subprocess.call(['rm', '-fr', 'attachments'])
        index += 1
        print('Done')


if __name__ == "__main__":
        process()