#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Even

import logging

logging.basicConfig(filename="test.log",
                    level=logging.INFO,
                    format='%(asctime)s %(filename)s:%(lineno)s-%(levelname)s %(message)s',
                    datefmt='%Y-%m-%d %I:%M:%S %p')
logging.info("123")
logging.debug("234")
logging.error("345")
logging.warning("456")
logging.critical("567")
