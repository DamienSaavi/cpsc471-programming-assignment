import os
import data_handling

# ******************************************************************************
# Available commands
# ******************************************************************************
CMDS = ('get', 'put', 'ls', 'quit')

# ******************************************************************************
# File directories
# ******************************************************************************
package_dir = os.path.dirname(os.path.abspath(__file__))
CLIENT_FILES_DIR = os.path.join(package_dir, 'client_files')
SERVER_FILES_DIR = os.path.join(package_dir, 'server_files')


# ******************************************************************************
# Client commands
#   - command responses from client socket
# ******************************************************************************
def client_get(sock, file_name):
    '''
    downloads file from server to client
    '''
    # send name of file to download from server
    sock.send(file_name.encode())

    # receive first 10 bytes (file size indicator)
    file_size_buffer = data_handling.receive_data(sock, 10)
    # get file size
    file_size = int(file_size_buffer)

    print(f'Downloading file: {file_name} (Size: {file_size}) from server...')

    # receive file data
    file_data = data_handling.receive_data(sock, file_size)

    # create file with received data in client_files directory
    file_path = os.path.join(CLIENT_FILES_DIR, file_name)
    file = open(file_path, 'w')
    file.write(file_data)

def client_put(sock):
    '''
    uploads file to the server from client
    '''

def client_ls(sock):
    '''
    lists files on server
    '''
    files_list_size = int(data_handling.receive_data(sock, 10))
    files_list = data_handling.receive_data(sock, files_list_size)
    for file in files_list.split('/'):
        print(file)

def client_quit(sock):
    '''
    disconnects from server and exits
    '''
    sock.close()
    exit()

# ******************************************************************************
# Server commands
#   - command responses from server socket
# ******************************************************************************
def server_get(sock, file_name):
    '''
    downloads file from server to client
    '''

def server_put(sock, file_name):
    '''
    uploads file to server from client
    '''

def server_ls(sock):
    '''
    lists files on server
    '''
    dir_list = os.listdir(SERVER_FILES_DIR)
    dir_list_str = '/'.join(dir_list)
    data_handling.send_data(sock, dir_list_str)
