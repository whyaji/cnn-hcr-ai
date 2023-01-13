import zipfile

chars = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
folders = ['Train']
archive = zipfile.ZipFile('archive.zip')


for folder in folders:
    for char in chars:
        start = folder + '/' + char + '/'
        names_foo = [i for i in archive.namelist() if i.startswith(start) ]
        i = 0
        for file in names_foo:
            print('extrac: ' + file)
            i+=1
            if i <= 3200:
                archive.extract(file, 'input/handwritten-characters/Train')
            elif i <= 4000:
                archive.extract(file, 'input/handwritten-characters/Validation')
            else:
                break
