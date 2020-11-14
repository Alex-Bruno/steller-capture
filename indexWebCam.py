from imutils.video import VideoStream
import imagezmq
import argparse
import socket
import time

ap = argparse.ArgumentParser()
ap.add_argument("-s", "--ip", required=True, help="Ip do servidor")
args = vars(ap.parse_args())

sender = imagezmq.ImageSender(connect_to="tcp://{}:5555".format(args["ip"]))

rpiName = socket.gethostname()
vs = VideoStream(src=0).start()
time.sleep(2.0)
while True:
    frame = vs.read()
    sender.send_image('pi-client', frame)
