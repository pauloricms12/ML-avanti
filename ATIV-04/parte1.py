import os
import cv2
import numpy as np
import matplotlib.pyplot as plt

#Consistência dos metadados

##verificar se as imagens são do mesmo tamanho
def check_images_size(directory):
    for main_folder in ['Test']:
        path = os.path.join(directory, main_folder)
        for i, fastfood in enumerate(os.listdir(path)):
            fastfood_path = os.path.join(path, fastfood)

            for image in os.listdir(fastfood_path):
                image_path = os.path.join(fastfood_path, image)
                img = cv2.imread(image_path)
                img_size = img.shape[:2]
                print(img_size)
                if i == 10: break

check_images_size('FastFoodClassificationV2')

def class_distribution(directory):
    fig, axes = plt.subplots(1, 3)
    for i, main_folder in enumerate(['Test', 'Train', 'Valid']):
        food = []
        sizes = []
        main_path = os.path.join(directory, main_folder)
        for fastfood in os.listdir(main_path):
            food.append(fastfood)
            sizes.append(len(os.listdir(os.path.join(main_path, fastfood))))
        axes[i].pie(sizes, labels=food, autopct='%1.1f%%')
        axes[i].set_title(f"Distribuição em {main_folder}")
    # plt.tight_layout()
    plt.show()

class_distribution('FastFoodClassificationV2')

#Identificação de Duplicatas
def duplicate_images(directory):
    for main_folder in ['Test', 'Train', 'Valid']:
        path = os.path.join(directory, main_folder)
        for fastfood in os.listdir(path):
            fastfood_path = os.path.join(path, fastfood)
            images = []

            for image in os.listdir(fastfood_path):
                # print('imagem atual: ', image)
                image_path = os.path.join(fastfood_path, image)
                img = cv2.imread(image_path)
                for image1 in images:
                    image1_path = os.path.join(fastfood_path, image1)
                    img1 = cv2.imread(image1_path)
                    if np.array_equal(img, img1) and image_path!=image1_path:
                        print(f"{image} = {image1}")
                        os.remove(image1_path)
                        images.remove(image1)
                        break
                images.append(image)

duplicate_images('FastFoodClassificationV2')
