# ## rename .pptx file to .zip
# ## another method is using shutil copy and rename original file
# import os
# my_file = 'test.pptx'
# base = os.path.splitext(my_file)[0]
# os.rename(my_file, base + '.zip')

# ## unarchive .zip file to a new directory - temp
# from zipfile import ZipFile
# os.mkdir('temp')
# with ZipFile('test.zip', 'r') as zipObj:
#     zipObj.extractall('temp')

# ## parse .xml to get essential information
# import xml.etree.ElementTree as ET 
# app = ET.parse('./temp/docProps/app.xml')
# root = app.getroot()
# words = root[1].text
# paragraphs = root[4].text
# slides = root[5].text
# fformat = root[3].text
# print(words, slides, paragraphs, fformat)

from bs4 import BeautifulSoup

with open("./temp/docProps/app.xml") as f:
    data = f.read()
    soup = BeautifulSoup(data, 'xml')
    words = soup.find("Words").get_text()
    slides = soup.find("Slides").get_text()
    paragraphs = soup.find("Paragraphs").get_text()
    pgformat = soup.find("PresentationFormat").get_text()
    print(slides)

## open slideX.xml 
for i in range(int(slides)):  ## int(slides)
    j = i + 1
    f = open('./temp/ppt/slides/slide' + str(j) + '.xml')
    data = f.read()
    soup = BeautifulSoup(data, 'xml')

    frelation = open('./temp/ppt/slides/_rels/slide' + str(j) + '.xml.rels')
    frel_data = frelation.read()
    frel_soup = BeautifulSoup(frel_data, 'xml')
    for relation in frel_soup.find_all('Relationship'):
        if relation.get("Type") == "http://schemas.openxmlformats.org/officeDocument/2006/relationships/slideLayout":
            lyt_addr = relation.get("Target")
            print(lyt_addr)





# for part in root.findall("./TitlesOfParts"):
#     for title in part.findall(".//vt:lpstr"):
#         print(title.text)



