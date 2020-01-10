import os
import glob
import xml.etree.ElementTree as ET
import pandas as pd

def convert_annotations_to_xml(path):
    data = []
    for file in sorted(glob.glob(path + '/*.xml')):
        doc = ET.parse(file)
        root = doc.getroot()
        filename = root.find('filename').text
        size = root.find('size')
        for member in root.findall('object'):
            value = (filename,
                    int(size[0].text),
                    int(size[1].text),
                    member[0].text,
                    int(member[4][0].text),
                    int(member[4][1].text),
                    int(member[4][2].text),
                    int(member[4][3].text)
                    )
            data.append(value)
    columns = ['filename', 'width', 'height', 'class', 'xmin', 'ymin', 'xmax', 'ymax']
    df = pd.DataFrame(data, columns=columns)
    return df

def main():
    annotations_path = os.path.join(os.getcwd(), 'annotations')
    output_path = os.path.join(os.getcwd(), 'data', 'annotations.csv')
    df = convert_annotations_to_xml(annotations_path)
    df.to_csv(output_path, index=None)



main()    
