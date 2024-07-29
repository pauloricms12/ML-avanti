import os
#Formato
def images_format(directory):
    total = 0
    jpg = 0
    png = 0
    others = 0
    for main_folder in ['Test', 'Train', 'Valid']:
        path = os.path.join(directory, main_folder)
        for food in os.listdir(path):
            food_path = os.path.join(path, food)
            for image in os.listdir(food_path):
                image_path = os.path.join(food_path, image)
                format = os.path.splitext(image_path)
                if format[1] in [".jpg", ".jpeg"]:
                    jpg += 1
                elif format[1] == ".png":
                    png += 1
                else:
                    others += 1
    print(f'jpg = {jpg}\npng = {png}\nothers={others}')

images_format("FastFoodClassificationV2")