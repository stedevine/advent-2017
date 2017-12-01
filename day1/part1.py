def read_file(file_name):
    """Helper function, read file return contents as string"""
    file_handle = open(file_name, 'r')
    return file_handle.read()

#print(floor_finder(read_file('input.txt')))
