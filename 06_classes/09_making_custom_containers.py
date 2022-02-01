class TagCloud:
    def __init__(self):
        self.tags = {}

    def add(self, tag):
        self.tags[tag.lower()] = self.tags.get(tag.lower(), 0) + 1

    def __getitem__(self, tag):
        return self.tags.get(tag.lower(), 0)

    def __setitem__(self, tag, count):
        self.tags[tag.lower()] = count

    def __len__(self):
        return len(self.tags)

    def __iter__(self):
        return iter(self.tags)


tag_cloud = TagCloud()
tag_cloud.add("python")
tag_cloud.add("python")
tag_cloud.add("python")
tag_cloud.add("Python")
tag_cloud.add("java")
tag_cloud.add("java")
tag_cloud.add("c")
print(tag_cloud.tags)
print(tag_cloud["python"])
tag_cloud["python"] = 20
print(tag_cloud["python"])
print(len(tag_cloud))

for x in tag_cloud:
    print(x)
