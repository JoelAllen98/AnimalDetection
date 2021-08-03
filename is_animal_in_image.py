import visualization.visualization_utils as viz_utils
import json
import sys
import ntpath
from shutil import copy2

THRESHOLD = 0.7
def detect_animals(output_filepath):
    imageList = []
    if output_filepath[:-1] != "\\":
        output_filepath = output_filepath + "\\"
    
    with open("Output\output.json") as json_file:
        data = json.load(json_file)

        for p in data['images']:
            is_animal = False
            for i in p['detections']:
                if i['conf'] > THRESHOLD and i['category'] == "1":
                    is_animal= True
            if is_animal:        
                imageList.append(p['file'])

    for i in imageList:
        print(i)
        copy2(i, output_filepath + ntpath.basename(i))
        



def detect_animals_with_discards(output_filepath,discarded_images_filepath):
    imageList = []
    non_imageList = []
    if output_filepath[:-1] != "\\":
        output_filepath = output_filepath + "\\"
    if discarded_images_filepath[:-1] != "\\":
        discarded_images_filepath = discarded_images_filepath + "\\"
    with open("Output\output.json") as json_file:
        data = json.load(json_file)

        for p in data['images']:
            
            is_animal = False
            for i in p['detections']:
                if i['conf'] > THRESHOLD and i['category'] == "1":
                    is_animal= True
            if is_animal:        
                imageList.append(p['file'])
            else:
                print("!")
                non_imageList.append(p['file'])

    for i in imageList:
        print(i)
        copy2(i, output_filepath + ntpath.basename(i))
        
    for i in non_imageList:
        print(i)
        copy2(i, discarded_images_filepath + ntpath.basename(i))



def main():
    output_images_filepath = sys.argv[1]
    try:
        print("!")
        discarded_images_filepath = sys.argv[2]
        detect_animals_with_discards(output_images_filepath,discarded_images_filepath)
    except:
        detect_animals(output_images_filepath)
        
    


if __name__ == "__main__":
    main()




