import logging

import dns_service


if '__main__' == __name__:
    logging.basicConfig(level=logging.DEBUG)
    dns_service.clean()