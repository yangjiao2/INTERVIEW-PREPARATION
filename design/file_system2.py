class TrieNode():
    def __init__(self, isFile, content = ""):
        self.isFile = isFile
        self.content = content
        self.children = {} # dir, files map



# /root/dir1/ -> split ('/')
# /root/dir1/file1 filecontent -> isfile, content

class FileSystem:

    def __init__(self):
        self.root = TrieNode(isFile=False)


    def ls(self, directory):
        directories = directory.split("/")
        node = self.root

        for i, d in enumerate(directories):
            if not d: # empty, which means the last /
                continue
            if d in node.children:
                node = node.children[d]

        return list(node.children.keys())


    def mkdir(self, directory):
        directories = directory.split("/")
        node = self.root

        for i, d in enumerate(directories):
            if not d: # empty, which means the last /
                continue
            if d in node.children:
                node = node.children[d]

            else:
                node.children =  {d: TrieNode(isFile=False, content="")}


    def appendfile(self, path, data):

        temp = path.split("/")
        directories = temp[:-1]
        filename = temp[-1]

        node = self.root

        for i, d in enumerate(directories):
            if not d: # empty, which means the last /
                continue
            if d in node.children:
                node = node.children[d]
            else:
                return False

        node.children[filename] = TrieNode(isFile=True, content = data)
        return True

    def read(self, path):

        temp = path.split("/")
        directories = temp[:-1]
        filename = temp[-1]

        node = self.root

        for i, d in enumerate(directories):
            if not d: # empty, which means the last /
                continue
            if d in node.children:
                node = node.children[d]
            else:
                print ("path not exist ",  path)
                return

        if filename in node.children and node.children[filename].isFile == True:
            print (node.children[filename].content)
        else:
            print ("file not exist ",  filename)
            return

fs = FileSystem()
# create dir
fs.mkdir("/path1")
# add file
fs.appendfile("/path1/file1" , "content1")
fs.appendfile("/path1/file2" , "content2")
fs.appendfile("/path1/file3" , "content3")
# list
fs.ls("/path1")
# print
fs.read("/path1/file1")
fs.read("/path1/file2")
fs.read("/path1/file3")

# print error
print ("error case")
fs.read("/path1/file4")
fs.read("/path1")
fs.appendfile("/path1/noexist/file3" , "content3")
