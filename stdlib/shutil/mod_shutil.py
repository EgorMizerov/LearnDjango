import shutil

# Копирование файла
shutil.copyfile('data.txt', 'data_copy.txt')
# Изминение названия каталога
shutil.move('./tst', 'src')
