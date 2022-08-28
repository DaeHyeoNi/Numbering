import os
from FileControl import FileControl

INPUT_DIRECTORY = 'input'
ONTPUT_DIRECTORY = 'output'

if __name__ == '__main__':
    # create input and output directory if not exist
    if not os.path.exists(INPUT_DIRECTORY):
        print('create input directory.')
        os.mkdir(INPUT_DIRECTORY)
    if not os.path.exists(ONTPUT_DIRECTORY):
        print('create output directory.')
        os.mkdir(ONTPUT_DIRECTORY)

    # read all files in input directory
    DATA_LIST = os.listdir(INPUT_DIRECTORY)
    print(f'Total files: {len(DATA_LIST)}')

    for i in DATA_LIST:
        fr = FileControl(os.path.join(INPUT_DIRECTORY, i))
        print(f'Converting... {i} {DATA_LIST.index(i) + 1}/{len(DATA_LIST)}')
        data = fr.read_file()
        FileControl(os.path.join(ONTPUT_DIRECTORY, i)).write_file(data)

    print('Done')
