import os
import logging
import time
import signal

CAMERA_ID = os.getenv("CAMERA_ID", "camera_unkown")
ZONE = os.getenv("ZONE", "zone_unkown")
FOG_URL = os.getenv("FOG_URL", "http://fog:8000")

logging.basicConfig(
    level=logging.INFO,
    format= "%(asctime)s [%(levelname)s] %(message)s"
)

running = True

def shutdown_handler(signum, frame):
    global running
    logging.info("%s shutting down...", CAMERA_ID)
    running = False

signal.signal(signal.SIGTERM, shutdown_handler)
signal.signal(signal.SIGINT, shutdown_handler)

def main():
    #Reads the camera, zone and fod noge from the environment variables and prints
    #the stratup information in the Docker logs.
    logging.info("Starting the camera client: %s", CAMERA_ID)
    logging.info("Zone %s", ZONE)
    logging.info("Assigned fog node is: %s", FOG_URL)
    logging.info("Camera: %s is ready.", CAMERA_ID)

    while running:
        time.sleep(10)

if __name__ == "__main__":
    main()