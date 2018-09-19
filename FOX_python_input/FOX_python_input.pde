import oscP5.*;
import netP5.*;

OscP5 oscP5;
NetAddress myRemoteLocation;

int receivePort = 12345;
String sendIP = "127.0.0.1";

int state = 0;

void setup() {
  size(400, 400);
  oscP5 = new OscP5(this, receivePort);
  myRemoteLocation = new NetAddress(sendIP, receivePort);
}

void draw() {
  switch(state) {
  case 0:
    background(0);
    OscMessage msg = new OscMessage("/state_receive");
    msg.add(1);
    oscP5.send(msg, myRemoteLocation);
    break;
  case 1:
    background(255);
    OscMessage msg2 = new OscMessage("/state_receive");
    msg2.add(2);
    oscP5.send(msg2, myRemoteLocation);
    break;
  case 2:
    background(255, 0, 0);
    OscMessage msg3 = new OscMessage("/state_receive");
    msg3.add(3);
    oscP5.send(msg3, myRemoteLocation);
    break;
  case 3:
    background(0, 255, 0);
    OscMessage msg4 = new OscMessage("/state_receive");
    msg4.add(4);
    oscP5.send(msg4, myRemoteLocation);
    break;
  case 4:
    background(0, 0, 255);
    break;
  }
}

void oscEvent(OscMessage theOscMessage) {
  if (theOscMessage.checkAddrPattern("/event_state") == true) {
    state = theOscMessage.get(0).intValue();
  }
}