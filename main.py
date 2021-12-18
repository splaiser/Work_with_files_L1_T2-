def get_sorted():
    count_file_1 = sum(1 for line in open('1.txt', 'r', encoding='UTF-8'))
    count_file_2 = sum(1 for line in open('2.txt', 'r', encoding='UTF-8'))
    count_file_3 = sum(1 for line in open('3.txt', 'r', encoding='UTF-8'))
    if count_file_1 < count_file_2 < count_file_3:
        with open('1.txt' , 'r', encoding='UTF-8') as file_1, \
                open('2.txt' , 'r', encoding='UTF-8') as file_2, \
                open('3.txt', 'r', encoding='UTF-8') as file_3, \
                open('final.txt', 'w', encoding='UTF-8') as file_f:
            file_f.write('1.txt\n')
            file_f.write(str(count_file_1) + '\n')
            file_f.write(file_1.read() + '\n')
            file_f.write('2.txt\n')
            file_f.write(str(count_file_2) + '\n')
            file_f.write(file_2.read() + '\n')
            file_f.write('3.txt\n')
            file_f.write(str(count_file_3) + '\n')
            file_f.write(file_3.read() + '\n')

    elif count_file_2 < count_file_3 < count_file_1:
        with open('1.txt' , 'r', encoding='UTF-8') as file_1, \
                open('2.txt' , 'r', encoding='UTF-8') as file_2, \
                open('3.txt', 'r', encoding='UTF-8') as file_3, \
                open('final.txt', 'w', encoding='UTF-8') as file_f:
            file_f.write('2.txt\n')
            file_f.write(str(count_file_2) + '\n')
            file_f.write(file_2.read() + '\n')
            file_f.write('3.txt\n')
            file_f.write(str(count_file_3) + '\n')
            file_f.write(file_3.read() + '\n')
            file_f.write('1.txt\n')
            file_f.write(str(count_file_1) + '\n')
            file_f.write(file_1.read() + '\n')


    elif count_file_3 < count_file_2 < count_file_1:
        with open('1.txt' , 'r', encoding='UTF-8') as file_1, \
                open('2.txt' , 'r', encoding='UTF-8') as file_2, \
                open('3.txt', 'r', encoding='UTF-8') as file_3, \
                open('final.txt', 'w', encoding='UTF-8') as file_f:
            file_f.write('3.txt\n')
            file_f.write(str(count_file_3) + '\n')
            file_f.write(file_3.read() + '\n')
            file_f.write('2.txt\n')
            file_f.write(str(count_file_2) + '\n')
            file_f.write(file_2.read() + '\n')
            file_f.write('1.txt\n')
            file_f.write(str(count_file_1) + '\n')
            file_f.write(file_1.read() + '\n')

    elif count_file_2 < count_file_1 < count_file_3:
        with open('1.txt', 'r', encoding='UTF-8') as file_1, \
                open('2.txt', 'r', encoding='UTF-8') as file_2, \
                open('3.txt', 'r', encoding='UTF-8') as file_3, \
                open('final.txt', 'w', encoding='UTF-8') as file_f:
            file_f.write('2.txt\n')
            file_f.write(str(count_file_2) + '\n')
            file_f.write(file_2.read() + '\n')
            file_f.write('1.txt\n')
            file_f.write(str(count_file_1) + '\n')
            file_f.write(file_1.read() + '\n')
            file_f.write('3.txt\n')
            file_f.write(str(count_file_3) + '\n')
            file_f.write(file_3.read() + '\n')



get_sorted()

def sort_lines():
    pass