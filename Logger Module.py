# What is logging ?
'''
- It is very useful for keeping track of the logging records and displaying the appropriate message to the user.
- Logging is a Python module in the standard library that provides the facility to work with the framework for
  releasing log messages from the Python programs.
'''

# Levels of logging in Python
'''
1. CRITICAL(50) --> A serious error, indicating that the program itself may be unable to continue running.
2. ERROR(40) --> Due to a more serious problem, the software has not been able to perform some function.
3. WARNING(30) --> An indication that something unexpected happened, or indicative of some problem in the near future 
   (e.g. ‘disk space low’). The software is still working as expected.
4. INFO(20) --> Confirmation that things are working as expected.
5. DEBUG(10) --> Detailed information, typically of interest only when diagnosing problems.
'''

# EXAMPLE: 1 -SIMPLE
'''
import logging

logging.warning('Message')
logging.info('Whats the information')
'''

# EXPLANATION:
'''
- In above example, The INFO message doesn’t appear because the default level is WARNING.
- WARNING:root:This is warning message. In this output "WARNING" is the level, "root" is the logger and "Message" is the 
  simple message that we passed.
'''

# EXAMPLE: 2
'''
import logging

# logging.basicConfig()

logging.critical("Critical message")
logging.error("Error message")
logging.warning("Warning message")
logging.info("Info message")
logging.debug("Debug message")
'''

# NOTE:
'''
In above example, The INFO message and the DEBUG message doesn’t appear because the default level is WARNING.
'''

# Basic Configurations
'''
- The main task of logging is to store the records events in a file. The logging module provides the basicConfig(**kwarg), 
  used to configure the logging.
'''

# EXAMPLE: 1
'''
import logging

logging.basicConfig(level=logging.DEBUG)
logging.critical("Critical message")

logging.basicConfig(level=logging.DEBUG)
logging.debug("Debug message")

# logging.basicConfig(level = logging.DEBUG)
logging.basicConfig(level = logging.debug('This is debug message'))

logging.basicConfig(level = 10)
logging.debug("This is another debug message")
'''

# EXPLANATION:
'''
- Similarly from above example, we can log the message to a file instead of display on console, filename and filenode 
  can be used in the basicConfig() function and we can decide the format of the message using format attributes.
'''

# EXAMPLE: 2
'''
import logging

logging.basicConfig(filename = 'msg.log', filemode = 'w', format = '%(name)s - %(levelname)s - %(message)s')

logging.warning('This will get logged to a file')
logging.warning('This will get logged to a file')
'''

# EXPLANATION:
"""
- The above output will be displayed in the msg.log file instead of console. We opened the file in "w", which means 
  the file is opened in the "write mode". If the basicConfig() is called multiple times, then each run of the program 
  will rewrite the log file's output.

- level - The specified severity level is set by the root level.
- filename - It specifies a file.
- filemode - It opens a file in a specific mode. The default mode of the opening file is "a", which means we can append 
  the content.
- format - The format defines the format of the log message.
"""

# EXAMPLE: 1
'''
import logging

logging.basicConfig(filename = "nitin.log", format = "%(asctime)s %(message)s", filemode = "w" )

Logger = logging.getLogger()

Logger.setLevel(logging.DEBUG)

Logger.debug("This is a harmless debug Message")
Logger.info("This is just an information")
Logger.warning("It is a Warning. Please make changes")
Logger.error("You are trying to divide by zero")
Logger.critical("Internet is down")
'''

# EXAMPLE: 2
'''
import logging

logging.basicConfig(filename = 'kuch_bhi.log')

Logger = logging.getLogger('My')

Logger.setLevel(level=10)

Logger.debug("This is a harmless debug Message")
Logger.info("This is just an information")
Logger.warning("It is a Warning. Please make changes")
Logger.error("You are trying to divide by zero")
Logger.critical("Internet is down")
'''

# EXAMPLE: 3
'''
import logging

logging.basicConfig(format = '%(message)s - %(name)s - %(levelname)s')

Logger = logging.getLogger('My')

Logger.setLevel(level=10)

Logger.debug("This is a harmless debug Message")
Logger.info("This is just an information")
Logger.warning("It is a Warning. Please make changes")
Logger.error("You are trying to divide by zero")
Logger.critical("Internet is down")
'''

# EXAMPLE: 4
'''
import logging

logging.basicConfig(filename = 'okokok.log', format = '%(levelname)s - %(message)s - %(asctime)s', datefmt = '%d/%m/%y %H:%M:%S', filemode = 'w')

Logger1 = logging.getLogger('Mock')

Logger1.setLevel(level=10)

Logger1.debug("This is a harmless debug Message")
Logger1.info("This is just an information")
Logger1.warning("It is a Warning. Please make changes")
Logger1.error("You are trying to divide by zero")
Logger1.critical("Internet is down")
'''

# EXAMPLE: 5 -FORMATTING
'''
import logging

logging.basicConfig(format = '%(process)s - %(name)s - %(levelname)s - %(asctime)s -  %(message)s')

Logger = logging.getLogger('You')

Logger.setLevel(level = 10)

Logger.debug("This is a harmless debug Message")
Logger.info("This is just an information")
Logger.warning("It is a Warning. Please make changes")
Logger.error("You are trying to divide by zero")
Logger.critical("Internet is down")
'''

# LOGGING VARIABLE DATA
'''
- Sometimes, we want to include the dynamic information from the application in the log. The logging methods are 
  accepted a string as an argument
'''

# EXAMPLE: 1
'''
import logging

name = 'Nitin Patil'

logging.error('%s raised an error', name)
'''

# EXAMPLE: 2
'''
import logging

name = 'Nitin Patil'

logging.error(f'{name} raised an error')
'''

# EXCEPTION INFO
'''
- There is an exc_info parameter in the logging function; if we set it as True, it can capture the Exception information.
'''
# Example 1-
'''
import logging

a = 10
b = 0

try:
    c = a / b

except Exception as e:
    logging.error("Exception Occurred", exc_info = True)
'''

# EXPLANATION:
'''
- If we don't set True to exc_info, the output will not inform us about the exception. It would be hard to debug 
  an error in thousand lines of code, if it displays only the following output:

ERROR:root:Exception Occurred 
'''


# EXAMPLE: 2
'''
- There is also other option to get complete information about the exception. The logging module provides the exception() 
  method, which logs a message with ERROR and attaches the exception information. 
- To use it, call the logging.exception() method same as calling logging.error(exc_info = True).


import logging

a = 10
b = 0

try:
    c = a / b

except Exception as e:
    logging.exception("Exception Occurred", exc_info = True)
'''

# NOTE:
'''
We can use any of one option in error(), debug(), or critical() methods to get information about the exception.
'''



# Reference: https://www.javatpoint.com/logging-in-python#:~:text=Logging%20is%20a%20Python%20module,when%20they%20work%20to%20logging.