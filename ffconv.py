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

    if(filelist == [] and filelist2 == []):
        print("Nincs megfelelő fájl")
    else:
        # encode each file
        for file in filelist:
            encode(file)

        for file in filelist2:
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
    inputShort = inputFile.split('.')[0]
    outputFile = inputShort.upper() + 'conv' + '.mkv'

    try:

        info = c.probe(file)

        videoCodec = info.video.codec
        audioCodec = info.audio.codec
        fileFormat = info.format.format

        print(info.format.format)
        print(info.format.duration)
        print(audioCodec)
        print(videoCodec)

        if (videoCodec == 'h264' and audioCodec == 'ac3' and 'matroska' in fileFormat):
            raise ValueError("Nem kell átkódolni")
        elif (videoCodec != 'h264'):
            conv = c.convert(inputFile, outputFile, options)
        else:
            conv = c.convert(inputFile, outputFile, optionsNoConv)

        print(outputFile)

        for timecode in conv:
            print("Converting (%f) ...\r" % timecode)

    except:
        print('Nem kell átkódolni')

    finally:
        # always cleanup even if there are errors
        #subprocess.call(['rm', '-fr', 'attachments'])
        print('Done')


if __name__ == "__main__":
        process()