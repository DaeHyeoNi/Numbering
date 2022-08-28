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
    data_list = []
    for file in os.listdir(INPUT_DIRECTORY):
        if file.endswith('.txt'):
            data_list.append(file)
    
    print(f'Total files: {len(data_list)}')

    for i in data_list:
        fr = FileControl(os.path.join(INPUT_DIRECTORY, i))
        print(f'Converting... {i} {data_list.index(i) + 1}/{len(data_list)}')
        data = fr.read_file()
        FileControl(os.path.join(ONTPUT_DIRECTORY, i)).write_file(data)

    print('Done')
