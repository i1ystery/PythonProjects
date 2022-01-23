def log(message: str):
    """
    Logs message to file server_log.txt
    """
    with open("server_log.txt", 'a') as f:
        f.write(message + '\n')


def log_send(message: str, conn, addr):
    """
    Sends message to defined client and then logs it to file
    """
    conn.send(message.encode())
    log(f'{addr[0]}:{addr[1]} <- {message}')
