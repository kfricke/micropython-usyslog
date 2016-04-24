try:
    import network
    _NETWORK_MODULE_LOADED = True
    WLAN_SSID = 'some name'
    WLAN_PSK = 'something secret'
except:
    _NETWORK_MODULE_LOADED = False
import utime
import usyslog

SYSLOG_SERVER_IP = '127.0.0.1'

if _NETWORK_MODULE_LOADED:
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    if not wlan.isconnected():
        print('Connecting to WLAN...')
        wlan.connect(WLAN_SSID, WLAN_PSK)
        while not wlan.isconnected():
            time.sleep_ms(500)
            print('  Waiting for WLAN to connect...')
    print('WLAN Connected:')
    print('  Network configuration:', wlan.ifconfig())
    print('Starting syslog tests...')

# Test non-default facility
s = usyslog.UDPClient(ip=SYSLOG_SERVER_IP, facility=usyslog.F_LOCAL4)
s.info('LOCAL4:Info!')

# Test other methods
s = usyslog.UDPClient(ip=SYSLOG_SERVER_IP)
s.alert('Testing a message with alert severity')
s.critical('This is a non critical test message!')
s.error('In case of an error, you can use this severity.')
s.debug('Debug messages can get annoying in production environments!')
s.info('Informational messages are just slightly more "unsevere" as debug messages')
s.notice('Noticed this? Nevermind!')
s.warning('This is my last warning!')
s.log(usyslog.S_EMERG, 'This is an emergency! Lets hope all prior tests did pass succesfully!')
