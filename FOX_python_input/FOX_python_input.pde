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
    break;
  case 1:
    background(255);
    break;
  case 2:
    background(255, 0, 0);
    break;
  case 3:
    background(0, 255, 0);
    break;
  case 4:
    background(0, 0, 255);
    break;
  }
}

void oscEvent(OscMessage theOscMessage) {
  print("### received an osc message.");
  if (theOscMessage.checkAddrPattern("/event_state") == true) {
    state = theOscMessage.get(0).intValue();
    println(" values: "+state);
  }
}

