#El siguiente Script realiza una configuracion inicial de un Router Cisco. La prueba se realizo con un router 1921.

import msvcrt

import serial #Si no tiene esta libreria instaladalo debe realizar con pip install pyserial para que reconozca el puerto COM

import time

#Inicializando el objeto de tipo Serial.
ser = serial.Serial(
    port = 'COM1', #En este item deben ingresar el número del puerto COM 
    baudrate=9600, 
    parity='N',    
    stopbits=1,
    bytesize=8,
    timeout=8      
    )

#Abre el objeto serial, en este caso COM1.
ser.isOpen()

#Imprime el puerto COM.
print(ser.name)

#En este punto se ingresan a la variable command los comandos de configuracion de ios cisco
#la expresion \r reemplaza al apretar el enter y \n es el salto de linea.
command = '\r\n' \
'enable' \
'\r\n' \
    'config t' \
    '\r\n' \
        'hostname R1' \
        '\r\n' \
        'enable secret cisco' \
        '\r\n' \
        'banner motd / \r\n' \
            '****************************************** \r\n' \
            'Solo personal autorizado puede ingresar \r\n' \
            '****************************************** /' \
            '\r\n' \
        'line console 0' \
        '\r\n' \
            'password cisco' \
            '\r\n' \
            'login' \
            '\r\n' \
            'exit' \
            '\r\n' \
        'line vty 0 4' \
        '\r\n' \
            'password cisco' \
            '\r\n' \
            'login' \
            '\r\n' \
            'exit' \
            '\r\n' \
        'int g0/0' \
        '\r\n' \
            'ip address 192.168.1.250 255.255.255.0' \
            '\r\n' \
            'no shutdown' \
            '\r\n' \
            'exit' \
            '\r\n' \
        'int g0/1' \
        '\r\n' \
            'ip address 192.168.2.1 255.255.255.0' \
            '\r\n' \
            'no shutdown' \
            '\r\n' \
            'exit' \
            '\r\n' \
        'ip dhcp pool DCHP-POOL-01' \
        '\r\n' \
            'default-router 192.168.2.1' \
            '\r\n' \
            'network 192.168.2.0 255.255.255.0' \
            '\r\n' \
            'dns-server 8.8.8.8' \
            '\r\n' \
            'exit' \
            '\r\n' \
        'ip domain-name cisco.com' \
        '\r\n' \
        'crypto key generate rsa modulus 1024' \
        '\r\n' \
        'line vty 0 4' \
        '\r\n' \
            'transport input ssh' \
            '\r\n' \
            'login local' \
            '\r\n' \
        'username admin privilege 15 secret cisco' \
        '\r\n' \
        'ip ssh version 2' \
        '\r\n' \
        'ip route 0.0.0.0 0.0.0.0 192.168.1.1' \
        '\r\n' \
        'ip domain lookup'\
        '\r\n' \
        'ip name-server 8.8.8.8' \
        '\r\n' \
        'access-list 1 permit 192.168.2.0 0.0.0.255' \
        '\r\n' \
        'ip nat inside source list 1 interface g0/0 overload' \
        '\r\n' \
        'interface g0/0' \
        '\r\n' \
            'ip nat outside' \
            '\r\n' \
        'interface g0/1' \
        '\r\n' \
            'ip nat inside' \
            '\r\n' \
            'exit' \
            '\r\n' \
    'exit' \
    '\r\n' \
    'copy running-config startup-config' \
    '\r\n' \
    'exit' \
    '\r\n' \

#Convierte la variable command de string a binario.
command = str.encode(command)

#Envia los comando al router.
ser.write(command)

#Tiempo de espera.
time.sleep(0.5)
ser.inWaiting()

#Obtiene la respuesta del router.
input_data = ser.read(15000) #el valor 15000 es la cantidad de caracteres que va a ver en pantalla.

#Convierte los valores enviados del router de binario a string.
input_data = input_data.decode("utf-8", "ignore")

#Imprime la respuesta.
print(input_data)

print("Presiona cualquier tecla para continuar...")
msvcrt.getch()


