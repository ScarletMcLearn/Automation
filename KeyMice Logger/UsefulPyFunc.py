def write_file(file_name, text):
    file_name = str(file_name) + '.txt'
    file = open(file_name, 'a')
    file.write(text)
    file.close


