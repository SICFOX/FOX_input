/* --------------------------------------------------------------------------
 * FOX Kinect System
 * --------------------------------------------------------------------------
 * prog:  Makoto Amano
 * date:  28/8/2018 (m/d/y)
 * ----------------------------------------------------------------------------
 */

import SimpleOpenNI.*;
int shot_count = 1;

String time = "10";
int t;
int interval = 10;

SimpleOpenNI  context;
color[]       userClr = new color[] { 
  color(255, 0, 0), 
  color(0, 255, 0), 
  color(0, 0, 255), 
  color(255, 255, 0), 
  color(255, 0, 255), 
  color(0, 255, 255)
};
PVector com = new PVector();                                   
PVector com2d = new PVector();                                   

void setup()
{
  size(640 *2, 480);

  context = new SimpleOpenNI(this);
  if (context.isInit() == false)
  {
    println("Can't init SimpleOpenNI, maybe the camera is not connected!"); 
    exit();
    return;
  }

  // enable depthMap generation 
  context.enableDepth();

  // enable skeleton generation for all joints
  context.enableUser();

  // enable ir generation
  context.enableRGB();

  background(200, 0, 0);

  stroke(0, 0, 255);
  strokeWeight(3);
  smooth();
}

void draw()
{
  // update the cam
  context.update();

  image(context.rgbImage(), 0, 0);
  //size(641, 480);
  // draw depthImageMap
  image(context.userImage(), context.depthWidth()+ 1, 0);

  // draw the skeleton if it's available
  int[] userList = context.getUsers();
  for (int i=0; i<userList.length; i++)
  {
    if (context.isTrackingSkeleton(userList[i]))
    {
      stroke(userClr[ (userList[i] - 1) % userClr.length ] );
      drawSkeleton(userList[i]);
    }      

    // draw the center of mass
    if (context.getCoM(userList[i], com))
    {
      context.convertRealWorldToProjective(com, com2d);
      stroke(100, 255, 0);
      strokeWeight(1);
      beginShape(LINES);
      vertex(com2d.x, com2d.y - 5);
      vertex(com2d.x, com2d.y + 5);

      vertex(com2d.x - 5, com2d.y);
      vertex(com2d.x + 5, com2d.y);
      endShape();

      fill(0, 255, 100);
      text(Integer.toString(userList[i]), com2d.x, com2d.y);
    }
  }
}

//void countdown() {
//  fill(255);
//  textSize(150);
//
//  t = interval-int(millis()/1000);
//  time = nf(t, 3);
//  if (t == -1) {
//    PImage saveImage = get(0, 0, 640, 480);
//    saveImage.save(System.getProperty("user.home") + "/Documents/中西研究会//UIST2018/System/img/img" + shot_count + ".jpg");
//    shot_count++;
//    interval+=10;
//  }
//  text(time, width/2-135, height/2);
//}

// draw the skeleton with the selected joints
void drawSkeleton(int userId)
{
  // to get the 3d joint data
  PVector rightHandPos = new PVector();
  PVector leftHandPos = new PVector();
  context.getJointPositionSkeleton(userId, SimpleOpenNI.SKEL_RIGHT_HAND, rightHandPos);
  context.getJointPositionSkeleton(userId, SimpleOpenNI.SKEL_LEFT_HAND, leftHandPos);
  //  println(rightHandPos.x,leftHandPos.x);
  float diff = rightHandPos.x - leftHandPos.x;
  println("Size of Cotton Candy = ", int(diff/10), "cm");
  //  float depth = (rightHandPos.z + leftHandPos.z)/2;
  //  println(int(depth));

  context.drawLimb(userId, SimpleOpenNI.SKEL_HEAD, SimpleOpenNI.SKEL_NECK);

  context.drawLimb(userId, SimpleOpenNI.SKEL_NECK, SimpleOpenNI.SKEL_LEFT_SHOULDER);
  context.drawLimb(userId, SimpleOpenNI.SKEL_LEFT_SHOULDER, SimpleOpenNI.SKEL_LEFT_ELBOW);
  context.drawLimb(userId, SimpleOpenNI.SKEL_LEFT_ELBOW, SimpleOpenNI.SKEL_LEFT_HAND);

  context.drawLimb(userId, SimpleOpenNI.SKEL_NECK, SimpleOpenNI.SKEL_RIGHT_SHOULDER);
  context.drawLimb(userId, SimpleOpenNI.SKEL_RIGHT_SHOULDER, SimpleOpenNI.SKEL_RIGHT_ELBOW);
  context.drawLimb(userId, SimpleOpenNI.SKEL_RIGHT_ELBOW, SimpleOpenNI.SKEL_RIGHT_HAND);

  context.drawLimb(userId, SimpleOpenNI.SKEL_LEFT_SHOULDER, SimpleOpenNI.SKEL_TORSO);
  context.drawLimb(userId, SimpleOpenNI.SKEL_RIGHT_SHOULDER, SimpleOpenNI.SKEL_TORSO);

  context.drawLimb(userId, SimpleOpenNI.SKEL_TORSO, SimpleOpenNI.SKEL_LEFT_HIP);
  context.drawLimb(userId, SimpleOpenNI.SKEL_LEFT_HIP, SimpleOpenNI.SKEL_LEFT_KNEE);
  context.drawLimb(userId, SimpleOpenNI.SKEL_LEFT_KNEE, SimpleOpenNI.SKEL_LEFT_FOOT);

  context.drawLimb(userId, SimpleOpenNI.SKEL_TORSO, SimpleOpenNI.SKEL_RIGHT_HIP);
  context.drawLimb(userId, SimpleOpenNI.SKEL_RIGHT_HIP, SimpleOpenNI.SKEL_RIGHT_KNEE);
  context.drawLimb(userId, SimpleOpenNI.SKEL_RIGHT_KNEE, SimpleOpenNI.SKEL_RIGHT_FOOT);
}

// -----------------------------------------------------------------
// SimpleOpenNI events

void onNewUser(SimpleOpenNI curContext, int userId)
{
  println("onNewUser - userId: " + userId);
  println("\tstart tracking skeleton");

  curContext.startTrackingSkeleton(userId);
}

void onLostUser(SimpleOpenNI curContext, int userId)
{
  println("onLostUser - userId: " + userId);
}

void onVisibleUser(SimpleOpenNI curContext, int userId)
{
  //println("onVisibleUser - userId: " + userId);
}

void keyPressed() {
  if (key == 'p') {
    PImage saveImage = get(0, 0, 640, 480);
    saveImage.save(System.getProperty("user.home") + "/Documents/中西研究会//UIST2018/System/img/test" + shot_count + ".jpg");
    println("test" + shot_count);
    shot_count++;
  }
}

