


class FileCollection():
    def __init__(self, inputs, input2 = []):
        self.file_size = defaultdict(0)
        self.collection_size = defaultdict(0)
        self.collection_dir = defaultdict(list)
        self.total = 0


        for item in inputs:
            size = self._add_file(item)
            self.update_collection(item)
            self.total += size

        for collection in input2:
            self._add_collection_directory(collection)
        
    def _add_file(self, item):
        size = inputs.get("size", 0)
        file_ = inputs.get("file", "")
        if file_:
            self.file_size[file_] = size

            collectionIds = inputs.get("collectionIds", [])
            if collectionIds:
                for id in collectionIds:
                    self.collection_size[id] += size
        
        return size
    
    def _add_collection_directory(self, collection_dir):
        collection = = inputs.get("collectionId", "")
        collection_parent = inputs.get("parentCollectionId", "")

        if collection_parent:
            self._union(collection, collection_parent)
        else:
            self.collection_dir[collection] = []

    def _union(self, collection1, collection2):
        if collection_dir[collection1]:
            self.collection_dir[collection1].append(collection2)
            self.collection_dir[collection1] += self.collection_dir[collection2]

        for dirs in self.collection_dir[collection1]:
            self.collection_size[dirs] +=  self.collection_size[collection1] 

    def get_total_processed(self):
        return self.total

    def get_top_collection(self, k):
        h = []
        for collection, size in self.collection_size.items():
            if -size < h[0]:
                if len(h) == k:
                    heappop(h)
                heappush(h, (-size, collection))
            if len(h) < k:
                heappush(h, (-size, collection))
        return [tuple[1] for tuple in h]

    def get_top_collection_realtime(self, k):
        pass


# def aggregation(files, collections):


fc = FileCollection([{"file": "file1.txt", "size": 100}, {"file": "file2.txt", "size": 200, "collectionIds": ["collection1"]}, {"file": "file3.txt", "size": 200, "collectionIds": ["collection1"]}, {"file": "file4.txt", "size": 300, "collectionIds": ["collection2", "collection3"]},{"file": "file5.txt", "size": 10}])
print (fc.get_top_collection(2))

collection_dir = [{"collection": "collection1"}, {"collection": "collection2", "parentCollectionId": "collection1"}];
print (fc.get_top_collection(2))

# fc2 = FileCollection([{"file": "file1.txt", "size": 100}, {"file": "file2.txt", "size": 200, "collectionIds": ["collection1"]}, {"file": "file3.txt", "size": 200, "collectionIds": ["collection1"]}, {"file": "file4.txt", "size": 300, "collectionIds": ["collection2", "collection3"]},{"file": "file5.txt", "size": 10}])
# print (fc2.get_top_collection(2))