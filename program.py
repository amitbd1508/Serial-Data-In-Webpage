import serial
import time
import webbrowser

file_name = "serial.html" 

serial_port = '/dev/ttyACM0'
baudrate = 9600

page_title = "Serial Data"

def write_page(data):
    fo = open(file_name,"w+")
    # Start of HTML page.
    fo.write("<!DOCTYPE HTML PUBLIC '-//W3C//DTD HTML 4.01//EN' 'http://www.w3.org/TR/html4/strict.dtd'>")
    fo.write("<html><head><title>"+page_title+"</title>") # Page & Head begin.
    fo.write("<meta http-equiv='refresh' content='1'>")
    fo.write("<meta http-equiv='Content-Type' content='text/html; charset=UTF-8'>")
    fo.write("<link rel='shortcut icon' href='favicon.ico' />")
    fo.write("<link rel='icon' type='image/x-icon' href='favicon.ico' />")
    fo.write("<link rel='icon' type='image/png' href='favicon.png' />")
    fo.write("</head><body><center><p style=\"color:black;font-size:200px;\">"+page_title+"</p>") # Head end, body begin.

    fo.write("<h1 style=\"color:red;font-size:200px;\">"+str(data)+"</h1>")

    fo.write("</body>") 
    fo.write("</html>")
    fo.close()

s = serial.Serial(serial_port,baudrate)
s.dtr = 0 
s.dtr = 1
print("Waiting for data...")
time.sleep(2)
s.reset_input_buffer()


webbrowser.open_new_tab("serial.html")

while 1:
    data = s.readline().decode()
    write_page(i)

    time.sleep(3)