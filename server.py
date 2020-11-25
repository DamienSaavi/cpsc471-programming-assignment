import sys
import os
import socket
import cmds
import data_handling

def execute_cmd(cmd, sock):
    '''
    executes given command from server
    Params:
        cmd: [command, file name (if exists)]
        sock: socket
    '''
    # get command
    if cmd[0] == cmds.CMDS[0]:
        cmds.server_get(sock, cmd[1])
    # put command
    elif cmd[0] == cmds.CMDS[1]:
        cmds.server_put(sock, cmd[1])
    # ls command
    elif cmd[0] == cmds.CMDS[2]:
        cmds.server_ls(sock)
    # quit command
    elif cmd[0] == cmds.CMDS[3]:
        cmds.server_quit(sock)

def main():
    # check correct number of arguments
    if len(sys.argv) < 2:
        print(f'USAGE: $ python {sys.argv[0]} <PORT NUMBER>')
        exit()

    # listening port
    server_port = sys.argv[1]

    # create a socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # bind socket to port
    server_socket.bind(('', int(server_port)))
    # start listening on socket
    server_socket.listen(1)

    # accept connections until interrupt (CTRL+C)
    while True:
        print('Waiting for connections...')

        # accept connection
        client_socket, client_addr = server_socket.accept()
        print(f'Accepted connection from client: {client_addr}')

        # keep connection open until client issues 'quit' command
        while True:
            # get command and file name if exists
            cmd_size = int(data_handling.receive_data(client_socket, 10))
            cmd = data_handling.receive_data(client_socket, cmd_size)
            cmd = cmd.split()

            print(f'Executing command: {cmd[0]}...')
            # get command
            if cmd[0] == cmds.CMDS[0]:
                print(cmd)
            # put command
            elif cmd[0] == cmds.CMDS[1]:
                print(cmd)
            # ls command
            elif cmd[0] == cmds.CMDS[2]:
                cmds.server_ls(client_socket)
                print('Successfully sent list of files to client')
            # quit command
            elif cmd[0] == cmds.CMDS[3]:
                break

        # close socket from server side
        client_socket.close()

if __name__ == '__main__':
    main()
