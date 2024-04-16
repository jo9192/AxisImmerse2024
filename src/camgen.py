from configparser import RawConfigParser
from datetime import datetime
import time
import logging
import sys
import json

cfg = RawConfigParser()

def currentDayStr():
    return time.strftime("%Y%m%d")

def currentTimeStr():
    return time.strftime("%H:%M:%S")

def initLog(rightNow, logConfig):
    logger = logging.getLogger(logConfig["log name"])
    hdlr = logging.FileHandler(logConfig["log path"]+rightNow+logConfig["log filename"])
    formatter = logging.Formatter(logConfig["log format"],logConfig["log time format"])
    hdlr.setFormatter(formatter)
    logger.addHandler(hdlr) 
    logger.setLevel(logging.INFO)
    return logger

# Test this more
def getCmdLineParser():
    import argparse
    desc = 'Execute camgen'
    parser = argparse.ArgumentParser(description=desc)

    parser.add_argument('-c', '--config_file', default='./config/camgen.json',
                        help='path+filename to configuration file')

    return parser

def main(argv):

	# Overhead to manage command line opts and config file
    p = getCmdLineParser()
    args = p.parse_args()
    with open(args.config_file) as json_file:
        config = json.load(json_file)

    print(json.dumps(config, indent=4))
	
    # Get the logger going
    logger = initLog(time.strftime("%Y%m%d%H%M%S"), config["logging"])
    logger.info('Starting Camgen Run: '+time.strftime("%Y%m%d%H%M%S"))



if __name__ == "__main__":
    main(sys.argv[1:])