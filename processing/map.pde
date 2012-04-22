/**
 * Load and Display 
 * 
 * Images can be loaded and displayed to the screen at their actual size
 * or any other size. 
 */
 
PImage d_map;  // Declare variable "a" of type PImage
PFont fontA;

color mouseOverColor;

//Crops
String crop1 = "Maize";
String crop2 = "Mango";
String crop3 = "Pineapple";
String crop4 = "Yucca";
String crop5 = "Papaya";

PImage crop_img1;
PImage crop_img2;
PImage crop_img3;
PImage crop_img4;
PImage crop_img5;

//Crop Prices

int price1;
int price2;
int price3;
int price4;
int price5;

//Crop Price Arrays by Dept
String [][]prices = new String[17][6];



//Dept Colors for Hover Detection
color d1 = #4a7e1c;
color d2 = #19551c;
color d3 = #228005;
color d4 = #168824;
color d5 = #278a17;
color d6 = #538007;
color d7 = #83c800;
color d8 = #64830a;
color d9 = #77ff00;
color d10 = #107b1b;
color d11 = #6d8109;
color d12 = #6f9900;
color d13 = #5ea400;
color d14 = #3d5a04;
color d15 = #2b7206;
color d16 = #85e700;
color d17 = #c5ff00;


void setup() {
  size(750, 500);
  //colorMode(RGB, 100);
  // The file "jelly.jpg" must be in the data folder
  // of the current sketch to load successfully
  d_map     = loadImage("data/nicaragua_dept_map2.png");  // Load the image into the program 
  crop_img1 = loadImage("data/crop1.png");
  crop_img2 = loadImage("data/crop2.png");
  crop_img3 = loadImage("data/crop3.png");
  crop_img4 = loadImage("data/crop4.png");
  crop_img5 = loadImage("data/crop5.png");
  fontA     =  loadFont("data/Swiss721BT-Bold-48.vlw");
  textFont(fontA, 20);
  
  prices[0][0] = "Boaco";
  prices[1][0] = "Carazo";
  prices[2][0] = "Chinandega";
  prices[3][0] = "Chontales";
  prices[4][0] = "Esteli";
  prices[5][0] = "Granada";
  prices[6][0] = "Jinotega";
  prices[7][0] = "Leon";
  prices[8][0] = "Madriz";
  prices[9][0] = "Managua";
  prices[10][0] = "Masaya";
  prices[11][0] = "Matagalpa";
  prices[12][0] = "Nueva Segovia";
  prices[13][0] = "Rivas";
  prices[14][0] = "Rio San Juan";
  prices[15][0] = "Region Autonoma del Atlantico Norte";
  prices[16][0] = "Region Autonoma del Atlantico Sur";
  
  
  for (int j = 0; j < 17; j++)
  {
    for (int i = 1; i < 6; i++)
    {
      int randomN = int(random(0, 200));
      prices[j][i] = ""+randomN;
      print(prices[j][i]);
    }
  }
}

void draw() {
  // Displays the image at its actual size at point (0,0)
  image(d_map, 0, 0); 
  //crop images
  
  image(crop_img1, width-92, 20);
  image(crop_img2, width-92, 112);
  image(crop_img3, width-92, 204);
  image(crop_img4, width-92, 296);
  image(crop_img5, width-92, 388);
  
  textAlign(RIGHT);
  fill(#2c2c2c);
  //currency markers
  for (int i = 0; i < 5; i++)
  {
    text("C$", width-63, 98+(92*i));
  }
  
  fill(#FFFFFF);
  
  //Ugly-ass code but works this shit should probably be a function
  textAlign(LEFT);
  mouseOverColor = get(mouseX, mouseY);
  if (mouseOverColor == d1)
  {
    text(prices[0][0], 50, height-50);
    fill(#2c2c2c);
    textAlign(RIGHT);
    for (int i = 1; i < 6; i++)
    {
      text(prices[0][i], width-13, 6+(92*i));
      barGraphs(int(prices[0][i]), i);
    }
    fill(#FFFFFF);
  }
  if (mouseOverColor == d2)
  {
    text(prices[1][0], 50, height-50);
    fill(#2c2c2c);
    textAlign(RIGHT);
    for (int i = 1; i < 6; i++)
    {
      text(prices[1][i], width-13, 6+(92*i));
      barGraphs(int(prices[1][i]), i);
    }
    fill(#FFFFFF);
  }
  if (mouseOverColor == d3)
  {
    text(prices[2][0], 50, height-50);
    fill(#2c2c2c);
    textAlign(RIGHT);
    for (int i = 1; i < 6; i++)
    {
      text(prices[2][i], width-13, 6+(92*i));
      barGraphs(int(prices[2][i]), i);
    }
    fill(#FFFFFF);
  }
  if (mouseOverColor == d4)
  {
    text(prices[3][0], 50, height-50);

    fill(#2c2c2c);
    textAlign(RIGHT);
    for (int i = 1; i < 6; i++)
    {
      text(prices[3][i], width-13, 6+(92*i));
      barGraphs(int(prices[3][i]), i);
    }
    fill(#FFFFFF);
  }
  if (mouseOverColor == d5)
  {
    text(prices[4][0], 50, height-50);
    fill(#2c2c2c);
    textAlign(RIGHT);
    for (int i = 1; i < 6; i++)
    {
      text(prices[4][i], width-13, 6+(92*i));
      barGraphs(int(prices[4][i]), i);
    }
    fill(#FFFFFF);
  }
  if (mouseOverColor == d6)
  {
    text(prices[5][0], 50, height-50);
    fill(#2c2c2c);
    textAlign(RIGHT);
    for (int i = 1; i < 6; i++)
    {
      text(prices[5][i], width-13, 6+(92*i));
      barGraphs(int(prices[5][i]), i);
    }
    fill(#FFFFFF);
  }
  if (mouseOverColor == d7)
  {
    text(prices[6][0], 50, height-50);
    fill(#2c2c2c);
    textAlign(RIGHT);
    for (int i = 1; i < 6; i++)
    {
      text(prices[6][i], width-13, 6+(92*i));
      barGraphs(int(prices[6][i]), i);
    }
    fill(#FFFFFF);
  }
  if (mouseOverColor == d8)
  {
    text(prices[7][0], 50, height-50);
    fill(#2c2c2c);
    textAlign(RIGHT);
    for (int i = 1; i < 6; i++)
    {
      text(prices[7][i], width-13, 6+(92*i));
      barGraphs(int(prices[7][i]), i);
    }
    fill(#FFFFFF);
  }
  if (mouseOverColor == d9)
  {
    text(prices[8][0], 50, height-50);
    fill(#2c2c2c);
    textAlign(RIGHT);
    for (int i = 1; i < 6; i++)
    {
      text(prices[8][i], width-13, 6+(92*i));
      barGraphs(int(prices[8][i]), i);
    }
    fill(#FFFFFF);
  }
  if (mouseOverColor == d10)
  {
    text(prices[9][0], 50, height-50);
    fill(#2c2c2c);
    textAlign(RIGHT);
    for (int i = 1; i < 6; i++)
    {
      text(prices[9][i], width-13, 6+(92*i));
      barGraphs(int(prices[9][i]), i);
    }
    fill(#FFFFFF);
  }
  if (mouseOverColor == d11)
  {
    text(prices[10][0], 50, height-50);
    fill(#2c2c2c);
    textAlign(RIGHT);
    for (int i = 1; i < 6; i++)
    {
      text(prices[10][i], width-13, 6+(92*i));
      barGraphs(int(prices[10][i]), i);
    }
    fill(#FFFFFF);
  }
  if (mouseOverColor == d12)
  {
    text(prices[11][0], 50, height-50);
    fill(#2c2c2c);
    textAlign(RIGHT);
    for (int i = 1; i < 6; i++)
    {
      text(prices[11][i], width-13, 6+(92*i));
      barGraphs(int(prices[11][i]), i);
    }
    fill(#FFFFFF);
  }
  if (mouseOverColor == d13)
  {
    text(prices[12][0], 50, height-50);
    fill(#2c2c2c);
    textAlign(RIGHT);
    for (int i = 1; i < 6; i++)
    {
      text(prices[12][i], width-13, 6+(92*i));
      barGraphs(int(prices[12][i]), i);
    }
    fill(#FFFFFF);
  }
  if (mouseOverColor == d14)
  {
    text(prices[13][0], 50, height-50);
    fill(#2c2c2c);
    textAlign(RIGHT);
    for (int i = 1; i < 6; i++)
    {
      text(prices[13][i], width-13, 6+(92*i));
      barGraphs(int(prices[13][i]), i);
    }
    fill(#FFFFFF);
  }
  if (mouseOverColor == d15)
  {
    text(prices[14][0], 50, height-50);
    fill(#2c2c2c);
    textAlign(RIGHT);
    for (int i = 1; i < 6; i++)
    {
      text(prices[14][i], width-13, 6+(92*i));
      barGraphs(int(prices[14][i]), i);
    }
    fill(#FFFFFF);
  }
  if (mouseOverColor == d16)
  {
    text(prices[15][0], 50, height-50);
    fill(#2c2c2c);
    textAlign(RIGHT);
    for (int i = 1; i < 6; i++)
    {
      text(prices[15][i], width-13, 6+(92*i));
      barGraphs(int(prices[15][i]), i);
    }
    fill(#FFFFFF);
  }
  if (mouseOverColor == d17)
  {
    text(prices[16][0], 50, height-50);
    fill(#2c2c2c);
    textAlign(RIGHT);
    for (int i = 1; i < 6; i++)
    {
      text(prices[16][i], width-13, 6+(92*i));
      barGraphs(int(prices[16][i]), i);
    }
    fill(#FFFFFF);
  }
  
}

void barGraphs(int price, int q)
{ 
  //price bar graph vis
  int xBar = width-92;
  noStroke();
  q--;

  fill(#ffea00, price);
  quad(xBar, 20+(q*92), xBar, 75+(q*92), xBar-price, 75+(q*92), xBar-price, 20+(q*92));
  fill(#2c2c2c);
}
