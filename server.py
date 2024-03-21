import socket
import os
from faker import Faker

fake = Faker()
sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)

server_address = 'socket_file'

# 以前の接続が残っていた場合に備えて、サーバアドレスをアンリンク(削除)する
try:
    os.unlink(server_address)
except FileNotFoundError:
    pass

# サーバのアドレスをソケットに紐付けます
sock.bind(server_address)

# 接続待ち状態
sock.listen(1)

#　無限ループでクライアントからの接続を待つ
while True:
    print('waiting for a connection')
    connection, client_address = sock.accept()
    try:
        print('connection from', client_address)

        #ループしてデータを受信して表示
        while True:
            data = connection.recv(1024)
            data_str = data.decode('utf-8')
            print('Received: {}'.format(data_str))
            #データがあれば返信
            if data:
                fake_txt = fake.text()
                connection.sendall(fake_txt.encode('utf-8'))
            else:
                print('no data from', client_address)
                break
    finally:
        connection.close()

