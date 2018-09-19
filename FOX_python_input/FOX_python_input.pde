import oscP5.*;
import netP5.*;

OscP5 oscP5;
OscP5 oscP5Send;
NetAddress myRemoteLocation;

int receivePort = 12345;
int sendPort = 56789;
String sendIP = "127.0.0.1";

int state = 0;

void setup() {
  size(400, 400);
  oscP5 = new OscP5(this, receivePort);
  oscP5Send = new OscP5(this, sendPort);
  myRemoteLocation = new NetAddress(sendIP, sendPort);
}

void draw() {
  OscMessage msg = new OscMessage("/state_receive");
  switch(state) {
  case 0:
    background(0);
    msg.add(1);
    oscP5Send.send(msg, myRemoteLocation);
    break;
  case 1:
    background(255);
    msg.add(2);
    oscP5Send.send(msg, myRemoteLocation);
    break;
  case 2:
    background(255, 0, 0);
    msg.add(3);
    oscP5Send.send(msg, myRemoteLocation);
    break;
  case 3:
    background(0, 255, 0);
    msg.add(4);
    oscP5Send.send(msg, myRemoteLocation);
    break;
  case 4:
    background(0, 0, 255);
    break;
  }
}

void oscEvent(OscMessage theOscMessage) {
  if (theOscMessage.checkAddrPattern("/event_state") == true) {
    state = theOscMessage.get(0).intValue();
    print(state);
  }
}