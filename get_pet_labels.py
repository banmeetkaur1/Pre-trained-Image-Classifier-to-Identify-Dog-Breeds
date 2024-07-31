#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/get_pet_labels.py
#                                                                             
# PROGRAMMER: Banmeet Kaur
# DATE CREATED: June 25, 2024                                
# REVISED DATE: June 27, 2024

##
# Imports python modules
from os import listdir


def get_pet_labels(image_dir):
    """
    Creates a dictionary of pet labels (results_dic) based upon the filenames 
    of the image files. These pet image labels are used to check the accuracy 
    of the labels that are returned by the classifier function, since the 
    filenames of the images contain the true identity of the pet in the image.
    Be sure to format the pet labels so that they are in all lower case letters
    and with leading and trailing whitespace characters stripped from them.
    (ex. filename = 'Boston_terrier_02259.jpg' Pet label = 'boston terrier')
    Parameters:
     image_dir - The (full) path to the folder of images that are to be
                 classified by the classifier function (string)
    Returns:
      results_dic - Dictionary with 'key' as image filename and 'value' as a 
      List. The list contains for following item:
         index 0 = pet image label (string)
    """
   
    filename_list = listdir(image_dir)
    #print("\nPrints 25 filenames from folder pet_images/")
    #for idx in range(0, 25, 1):
    #  print("{:2d} file: {:>25}".format(idx + 1, filename_list[idx]) )


    results_dic = dict()

    for idx in range(0, len(filename_list), 1):
      if filename_list[idx][0] != ".":
         file_name = ""

         file_name = filename_list[idx]
        
         low_pet_label = file_name.lower()
         
         pet_label_list = low_pet_label.split("_")
         

         pet_name = " ".join([word.strip() for word in pet_label_list if word.isalpha()])

         
         #print("\nFilename=", file_name, "   Label=", pet_name)

         if file_name not in results_dic:
          results_dic[file_name] = [pet_name]

          
         else:
          print("** Warning: Duplicate files exist in directory:", file_name)



       
       
    return results_dic
