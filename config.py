import socket
import time

#servIP = input("\nEnter Vision IP address : ")
#port = input("Enter port No. : ")
servIP = '192.168.0.10'
port = 8500
try:
    server = socket.socket()
    server.connect((servIP,port))
    status = True
    print(">>> Connected Success <<<")
except:
    print(">>> Connect failed <<<")
    status = False

 

#status = True


while status:
    try:
        print("\na = Send command to Vision")
        print("b = Recieve data from Vision")
        choice = input("\nEnter your choice : ")
        #def start():
           # print("\na = Send command to Vision")
           # print("b = Recieve data from Vision")
           # choice = input("\nEnter your choice : ")
        if choice == 'a':
            data = input('\nSend command >>>> ')
            data = data+'\r\n'

            server = socket.socket()
            server.connect((servIP,port))

            server.send(data.encode('utf-8'))
 

            data_server = server.recv(1024).decode('utf-8')
            print('Data recieve >>> ', data_server)
            print('###################')
            server.close()
            #start()
        elif choice == 'b':
            while True:
                time_start = time.perf_counter()
                print('wait data.....')
                server = socket.socket()
                server.connect((servIP,port))
                data_server = server.recv(1024).decode('utf-8')
                print('Data recieve >>> ', data_server)
                time_end = time.perf_counter()
                server.close()
                #print('time start ', tis)
                #print('time end ', tie)
                #print('time difference ', tie-tis)
                if time_end - time_start > 10:
                    break
                    #start()
    except Exception as e:
        print('Error: ', e)
        time.sleep(2)



print('.....exit loop.....')
#start()