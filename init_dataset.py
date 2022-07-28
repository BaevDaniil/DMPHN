import os

DATASET_DIR = "./datas/256_data/"



def test_blur():
    test_blur_files = open(DATASET_DIR + "test_blur_file.txt", "w")
    os.chdir(DATASET_DIR + "test/circles/blur")
    listdir = os.listdir()
    for img in listdir:
        test_blur_files.write("test/circles/blur/" + img + '\n')
    test_blur_files.close()
    os.chdir("../../../../..")

def test_sharp():
    test_sharp_files = open(DATASET_DIR + "test_sharp_file.txt", "w")
    os.chdir(DATASET_DIR + "test/circles/sharp")
    listdir = os.listdir()
    for img in listdir:
        test_sharp_files.write("test/circles/sharp/" + img + '\n')
    test_sharp_files.close()
    os.chdir("../../../../..")

def train_blur():
    test_blur_files = open(DATASET_DIR + "train_blur_file.txt", "w")
    os.chdir(DATASET_DIR + "train/circles/blur")
    listdir = os.listdir()
    for img in listdir:
        test_blur_files.write("train/circles/blur/" + img + '\n')
    test_blur_files.close()
    os.chdir("../../../../..")

def train_sharp():
    test_blur_files = open(DATASET_DIR + "train_sharp_file.txt", "w")
    os.chdir(DATASET_DIR + "train/circles/sharp")
    listdir = os.listdir()
    for img in listdir:
        test_blur_files.write("train/circles/sharp/" + img + '\n')
    test_blur_files.close()
    os.chdir("../../../../..")

if __name__ == "__main__":
    test_blur()
    test_sharp()
    train_blur()
    train_sharp()