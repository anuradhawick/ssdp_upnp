import sys
import colorlog
import socket

logger = None
def gen_logger(name, level='INFO'):
    global logger

    if logger is None:
        fmt = '%(log_color)s %(levelname)8s [%(asctime)s] %(name)s-%(threadName)-15s %(message)s'
        handler = colorlog.StreamHandler()
        handler.setFormatter(colorlog.ColoredFormatter(fmt))
        logger = colorlog.getLogger(name)
        logger.addHandler(handler)
        logger.setLevel(level)
        return logger
    return logger

def get_local_IP(): 
    '''
    get local host and ip address
    '''
    try: 
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.connect(("8.8.8.8", 80))
        host_ip = sock.getsockname()[0]
        sock.close()
        return host_ip
    except Exception as e:
        raise 'Unable to get Hostname and IP: {}'.format(e)
    
if __name__ == '__main__':
    assert len(sys.argv) == 2
    
    if sys.argv[1] == 'ip':
        print(get_local_IP())
    else:
        print('Command unknown')
        sys.exit(1)