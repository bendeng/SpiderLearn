import os


#遍历文件夹下的所有文件和文件夹
def loop_dir_files(path):
    g = os.walk(path)

    for path, dir_list, file_list in g:
        print('path->'+path)
        for dir_name in dir_list:
            print('dir->'+os.path.join(path, dir_name))

        for file in file_list:
            print('file->'+os.path.join(path, file))


loop_dir_files('.')