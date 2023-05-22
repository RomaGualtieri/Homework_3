import os
file_list = ['1.txt', '2.txt', '3.txt']
files = []
for file in file_list:
    with open(file, 'r', encoding='utf-8') as one_file:
        files.append([len(one_file.readlines()), file])
        with open('result.txt', 'w', encoding='utf-8') as result_file:
            for file in sorted(files):
                result_file.write(f'{file[1]}')
                result_file.write('\n')
                result_file.write(f'{file[0]}')
                result_file.write('\n')
                one_file = open(file[1], 'r', encoding='utf-8')
                result_file.writelines(one_file.readlines())
                result_file.write('\n')
                one_file.close()

print(result_file)
