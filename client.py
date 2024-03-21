import socket
import sys

# TCPソケットの作成
sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)

#　サーバにソケットを接続
server_address = 'socket_file'
print('connecting to {}'.format(server_address))

#　サーバに接続を試みる
try:
    sock.connect(server_address)
except socket.error as err:
    print(err)
    sys.exit(1)

#　メッセージを送信する。ソケット通信では
#　データをバイト形式で送る必要がある
#　サーバからの応答待ち時間を２秒に設定 
#　ctrl+cで終了するまで無限ループ

try:
    while True:
# コマンドラインからメッセージを入力
        message = input("Enter your message: ")

# メッセージをエンコードして送信
        print('sending {!r}'.format(message))
        sock.sendall(message.encode('utf-8'))

        sock.settimeout(2)

# サーバからの応答を受信し、データがあればそれを表示
        data = sock.recv(1024)
        print('Received: {}'.format(data))

#　タイムアウトが発生した場合
except socket.timeout:
    print('No data received')

# ソケットを閉じる
finally:
    print('closing socket')
    sock.close()
