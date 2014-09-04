from video_metadata_models import *
from peewee import *
import sys
import os
import xml.etree.ElementTree as ET

def main(argv):
    fullpath = os.path.abspath(argv[1])
    print fullpath
    pathlist = list(os.path.split(fullpath))
    pathlist[-1] = 'movie.nfo'
    nfoPath = os.path.join(*pathlist)
    
    videofile = VideoFile.get(VideoFile.path == fullpath)
    movie = HomeVideo.get(HomeVideo.mapper_id == videofile.mapper_id)

    tree = ET.parse(nfoPath)
    root = tree.getroot()
    
    #print 'title:', root.find('title').text
    movie.title = root.find('title').text
    movie.sort_title = movie.title
    movie.save()

    for tag in root.findall('tag'):
        #print 'tag:', tag.text
        Genre.insert(mapper_id=videofile.mapper_id, genre=tag.text).execute()

    for actor in root.findall('actor'):
        #print 'actor:', actor.find('name').text
        Actor.insert(mapper_id=videofile.mapper_id, actor=actor.find('name').text).execute()

if __name__ == '__main__':
    sys.exit(main(sys.argv))
