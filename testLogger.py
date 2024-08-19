from errorLogger import LogTheError
import os
import setup

def main():
    try:
        # Your main script logic here
        # If an exception occurs, call log_exception() passing the exception object
        print ('lol')
        eval('x===y')
    except Exception as e:
        print('logging error')
        # Log the exception
        LogTheError(e, os.path.basename(__file__))


if __name__ == "__main__":
    main()