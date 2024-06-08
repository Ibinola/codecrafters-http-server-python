# Uncomment this to pass the first stage
import socket


def main():
    # You can use print statements as follows for debugging, they'll be visible when running tests.
    print("Logs from your program will appear here!")

    # Uncomment this to pass the first stage
    #
    server_socket = socket.create_server(("localhost", 4221), reuse_port=True)
    connection, response =  server_socket.accept() # wait for client
    response[0].sendall(b"HTTP/1.1 200 OK\r\n\r\n")

    while True:
        request = connection.recv(1500).decode()
        headers = request.split('\n')
        first_header_components = headers[0].split()

        path = first_header_components[1]

        if path == '/':
            return 'HTTP/1.1 200 OK\r\n\r\n'
        else:
            return 'HTTP/1.1 404 Not Found\r\n\r\n'

    


if __name__ == "__main__":
    main()
