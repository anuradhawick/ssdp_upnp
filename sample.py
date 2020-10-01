import sys
from ssdp_upnp.ssdp import Server, Client, Nat
from ssdp_upnp.ssdp import gen_logger
from queue import Queue

logger = gen_logger('ssdp_upnp')

if __name__ == '__main__':
    try:
        if sys.argv[1] == 'server':
            if len(sys.argv) != 3:
                logger.warning('need param for server name')
                sys.exit()
            service_name = sys.argv[1]
            upnpServer  = Server(8048, 'anuradhawick-discovery', 'main', service_name)
            upnpServer.start()
        elif sys.argv[1] == 'client':
            queue = Queue()
            upnpClient = Client('anuradhawick-discovery', 'main', queue)
            upnpClient.start()
            # logger.info(queue.get())
        elif sys.argv[1] == 'nat':
            nat = Nat()
            print(nat.addPortForward(8011, 8015))
        else:
            logger.warning('need params server or client')
    except Exception as e:
        logger.error(e)
