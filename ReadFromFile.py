import re

with open('Scenes.txt', 'r') as open_file:
    scenes = {}
    line = open_file.readline()
    while line:
        scene = re.search("(/./)([^/]*)(.*)", line).group(2)
        if scene not in scenes:
            scenes[scene] = 1
        else:
            scenes[scene] += 1
        line = open_file.readline()
print(scenes)