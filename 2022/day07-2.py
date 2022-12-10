class File:
    def __init__(self, name, size, parent):
        self.name = name
        self.size = size
        self.parent = parent

    def __str__(self):
        return "\n" + self.name + " de taille " + str(self.size)


class Directory:
    def __init__(self, name, files, directories, parent):
        self.name = name
        self.files = files
        self.directories = directories
        self.parent = parent

    def add_file(self, name, size):
        self.files.append(File(name, size, self))

    def add_dir(self, name, parent):
        self.directories.append(Directory(name, [], [], parent))

    def get_subdir(self, name):
        return list(filter(lambda d: d.name == name, self.directories))[0]

    def __str__(self):
        result = "\nRépertoire " + self.name

        for directory in self.directories:
            result += str(directory)
        for file in self.files:
            result += str(file)
        return result


sizes = []


def size_of_dir(directory):
    size_dir = 0

    for dire in directory.directories:
        size_dir += size_of_dir(dire)

    for file in directory.files:
        size_dir += file.size

    print('Directory ' + directory.name + ' is of size ' + str(size_dir))
    sizes.append(size_dir)

    return size_dir


f = open("day07-puzzle-input.txt", "r")

fs = Directory('/', [], [], None)

cursor = None

for ligne in f:
    # print(ligne)
    # Command
    if ligne.startswith('$'):
        if ligne.startswith('$ cd /'):
            print('go /')
            cursor = fs
        elif ligne.startswith('$ cd ..'):
            print('go parent')
            cursor = cursor.parent
        elif ligne.startswith('$ cd '):
            print('go child')
            cursor = cursor.get_subdir(ligne.replace('$ cd ', ''))
        else:
            print('gne')
    # Result
    elif ligne.startswith('dir'):
        # print('répertoire')
        # print('ajout ' + ligne.replace('dir ', ''))
        print('nouveau dir')
        cursor.add_dir(ligne.replace('dir ', ''), cursor)
    else:
        # print('fichier')
        print('nouveau fichier')
        cursor.add_file(ligne.split(' ')[1], int(ligne.split(' ')[0]))

print(fs)
size_of_dir(fs)

unused_space = 70000000 - 42080344
minimum = 30000000 - unused_space

print(min(list(filter(lambda s: s >= minimum, sizes))))


