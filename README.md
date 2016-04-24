# micropython-usyslog
This python module does implement a simple remote syslog client for MicroPython. Currently only UDP based remote logging is implemented.

## Dependencies
In order to use this module one also needs an syslog server which is enabled to accept remote messages.
This modules has been tested with the following syslog servers:
 * rsyslog
 * syslog-ng

Please consult the documentation of your syslog server for details on how to enable receptionof remote messages.
