

from PIL import Image

from resizeimage import resizeimage

from os import walk

import os

mypath = '' # inputFolder

outfolder = '' #outputfolder

size = [1366, 613] # output size

#-------------

if not os.path.exists(outfolder):
    os.makedirs(outfolder)

filenames = next(os.walk(mypath)) 

directoryes = next(os.walk(mypath+'\\'))[1]


print('Directories: ')
print(directoryes)

ledir = len(directoryes)
print('File Count:')
print( str(ledir))


print('\n\n\nWorking\n')

log = open("log.txt", "a")
    

for d in directoryes:
    i = 0
    flname = next(walk(mypath+'\\'+d), (None, None, []))[2]
    print('dir:' + d)
    for x in flname:
        try:
            print('File: '+x) 
            loc = mypath+'\\'+d+'\\'+x
            print('loc: ')
            print(loc)
            with open(loc, 'r+b') as f:
                with Image.open(f) as image:
                    cover = resizeimage.resize_cover(image, size)
                    if not os.path.exists(outfolder+'\\'+d):
                        os.makedirs(outfolder+'\\'+d)
                    cover.save(outfolder+'\\'+d+'\\'+str(i)+'_'+x, image.format)
        except:
            print('Error on dir and file:')
            print(d)
            print(x)
            log.write('Error on dir and file:\n' + d + '\n'  + f)
        i = i + 1

log.close()

print('eady!!!')


# i = 0
# print(len(filenames))

# for x in filenames:
#     print(x) 
#     with open(mypath+'\\'+x, 'r+b') as f:
#         with Image.open(f) as image:
#             cover = resizeimage.resize_cover(image, size)
#             cover.save(outfolder+'\\'+str(i)+'_'+x, image.format)
#     i = i + 1