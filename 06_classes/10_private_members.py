class TagCloud:
    def __init__(self):
        self.__tags = {}

    def add(self, tag):
        self.__tags[tag.lower()] = self.__tags.get(tag.lower(), 0) + 1

    def __getitem__(self, tag):
        return self.__tags.get(tag.lower(), 0)

    def __setitem__(self, tag, count):
        self.__tags[tag.lower()] = count

    def __len__(self):
        return len(self.__tags)

    def __iter__(self):
        return iter(self.__tags)


tag_cloud = TagCloud()
tag_cloud.add("python")
tag_cloud.add("Python")
tag_cloud.add("python")
print(tag_cloud["PYTHON"])
# print(tag_cloud.tags["PYTHON"])
print(tag_cloud.__dict__)
# print(tag_cloud._TagCloud__tags["python"])
