/* --------------------------------------------------------------------------
 * SimpleOpenNI DepthImage Test
 * --------------------------------------------------------------------------
 * Processing Wrapper for the OpenNI/Kinect 2 library
 * http://code.google.com/p/simple-openni
 * --------------------------------------------------------------------------
 * prog:  Max Rheiner / Interaction Design / Zhdk / http://iad.zhdk.ch/
 * date:  12/12/2012 (m/d/y)
 * ----------------------------------------------------------------------------
 */

import SimpleOpenNI.*;
int shot_count = 1;

String time = "10";
int t;
int interval = 10;


SimpleOpenNI  context;

void setup()
{
  size(640, 480);
  context = new SimpleOpenNI(this);
  if (context.isInit() == false)
  {
    println("Can't init SimpleOpenNI, maybe the camera is not connected!"); 
    exit();
    return;
  }

  // mirror is by default enabled
  context.setMirror(true);

  // enable ir generation
  context.enableRGB();
}

void draw()
{
  // update the cam
  context.update();

  background(200, 0, 0);

  // draw irImageMap
  image(context.rgbImage(), 0, 0);
}


void countdown() {
  fill(255);
  textSize(150);

  t = interval-int(millis()/1000);
  time = nf(t, 3);
  if (t == -1) {
    PImage saveImage = get(0, 0, 640, 480);
    saveImage.save(System.getProperty("user.home") + "/Documents/中西研究会//UIST2018/System/img/img" + shot_count + ".jpg");
    shot_count++;
    interval+=10;
  }
  text(time, width/2-135, height/2);
}

void keyPressed(){
    int a = 1;
    if (a == 1) {
      countdown();
    }else{
      a = 0;
    }
  }
