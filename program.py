import serial
import time
import webbrowser

file_name = "serial.html" 

serial_port = '/dev/ttyACM0'
baudrate = 9600

page_title = "Serial Data Monitor"

def write_page(data):
    fo = open(file_name,"w+")

    fo.write("<!DOCTYPE HTML PUBLIC '-//W3C//DTD HTML 4.01//EN' 'http://www.w3.org/TR/html4/strict.dtd'>")
    fo.write("<html><head><title>"+page_title+"</title>")
    fo.write("<meta http-equiv='refresh' content='1'>")
    fo.write("<meta http-equiv='Content-Type' content='text/html; charset=UTF-8'>")
    fo.write("<link rel='shortcut icon' href='favicon.ico' />")
    fo.write("<link rel='icon' type='image/x-icon' href='favicon.ico' />")
    fo.write("<link rel='icon' type='image/png' href='favicon.png' />")
    fo.write("</head><body><center><p style=\"color:black;font-size:100px;\">"+page_title+"</p>")

    fo.write("<h1 style=\"color:red;font-size:150px;\">"+str(data)+"</h1>")

    fo.write("</body>") 
    fo.write("</html>")
    fo.close()

try:
    s = serial.Serial(serial_port,baudrate)
    print("Waiting for data...")
    time.sleep(2)

    webbrowser.open_new_tab("serial.html")

    while 1:
        data = s.readline().decode()
        write_page(data)
        print(data)

        time.sleep(3)
except :
    err = "Cannot start the application\nMake sure device is connected in "+serial_port
    print(err)
    