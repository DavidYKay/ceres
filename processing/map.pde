/**
 * Load and Display 
 * 
 * Images can be loaded and displayed to the screen at their actual size
 * or any other size. 
 */
 
PImage a;  // Declare variable "a" of type PImage
PFont fontA;

color mouseOverColor;

color d1 = -11829731;
color d2 = -15117028;
color d3 = -14516218;
color d4 = -15037914;
color d5 = -14120168;
color d6 = -11304953;
color d7 = -8140800;
color d8 = -10190070;
color d9 = -8913152;
color d10 = -16288491;
color d11 = -9600759;
color d12 = -9463552;
color d13 = -10574848;
color d14 = -12756476;
color d15 = -13930235;
color d16 = -8001792;
color d17 = -3801344;

//var departmentColors = {
//  -11829731 : "Boaco",
//  -15117028 : "Carazo",
//  -14516218 : "Chinadega",
//  -15037914 : "Chontales",
//  -14120168 : "Estelí",
//  -11304953 : "Granada",
//  -8140800  : "Jinotega",
//  -10190070 : "León",
//  -8913152  : "Madriz",
//  -16288491 : "Managua",
//  -9600759  : "Masaya",
//  -9463552  : "Matagalpa",
//  -10574848 : "Nueva Segovia",
//  -12756476 : "Rivas",
//  -13930235 : "Río San Juan",
//  -8001792  : "N. Autonomous Region",
//  -3801344  : "S. Autonomous Region"
//};


HashMap departmentColors = new HashMap();
// Original colors
//departmentColors.put("-11829731" , "Boaco");
//departmentColors.put("-15117028" , "Carazo");
//departmentColors.put("-14516218" , "Chinadega");
//departmentColors.put("-15037914" , "Chontales");
//departmentColors.put("-14120168" , "Estelí");
//departmentColors.put("-11304953" , "Granada");
//departmentColors.put("-8140800"  , "Jinotega");
//departmentColors.put("-10190070" , "León");
//departmentColors.put("-8913152"  , "Madriz");
//departmentColors.put("-16288491" , "Managua");
//departmentColors.put("-9600759"  , "Masaya");
//departmentColors.put("-9463552"  , "Matagalpa");
//departmentColors.put("-10574848" , "Nueva Segovia");
//departmentColors.put("-12756476" , "Rivas");
//departmentColors.put("-13930235" , "Río San Juan");
//departmentColors.put("-8001792"  , "N. Autonomous Region");
//departmentColors.put("-3801344"  , "S. Autonomous Region");

departmentColors.put("-11829731" , "Boaco");
departmentColors.put("-15117028" , "Carazo");
departmentColors.put("-14516218" , "Chinadega");
departmentColors.put("-15037914" , "Chontales");
departmentColors.put("-14120168" , "Estelí");
departmentColors.put("-11304953" , "Granada");
departmentColors.put("-10190070" , "León");
departmentColors.put("-8913152"  , "Madriz");
departmentColors.put("-16288491" , "Managua");
departmentColors.put("-9600759"  , "Masaya");
departmentColors.put("-9463552"  , "Matagalpa");
departmentColors.put("-12756476" , "Rivas");

departmentColors.put("-10968270" , "Nueva Segovia");
departmentColors.put("-14454238" , "Río San Juan"); // Gradient!!
departmentColors.put("-8468672"  , "Jinotega");
departmentColors.put("-8526261"  , "N. Autonomous Region");
departmentColors.put("-4063660"  , "S. Autonomous Region");

boolean isPresent(object) {
  if (object) {
    return true;
  } else {
    return false;
  }
}

void logIsPresent(object) {
  if (object) {
    println("object present! " + object);
  } else {
    println("object missing!");
  }
}

void showText(message) 
{
  text(message, width-250, height-100);
}

void showTextAndLogIt(message) 
{
  showText(message);
  println("Showing message: " + message);
}

void showTextForColor(colorCode)
{

  String colorString = str(colorCode);
  String departmentString = departmentColors.get(colorString);
  if (departmentString) {
    showTextAndLogIt(departmentString);
  } else {
    println("department missing for color: " + colorString);
  }
}

void setup() {
  size(800, 550);
  println("Hello Setup!");
  // The file "jelly.jpg" must be in the data folder
  // of the current sketch to load successfully
  a = loadImage("nicaragua_dept_map.png");  // Load the image into the program  
  logIsPresent(a);
  fontA = loadFont("Swiss721BT-Roman-48.vlw");
  logIsPresent(fontA);
  textFont(fontA, 12);
}

void draw() {
  // Displays the image at its actual size at point (0,0)
  image(a, 0, 0); 
  
  mouseOverColor = get(mouseX, mouseY);

  showTextForColor(mouseOverColor);
  //if (mouseOverColor == d1)
  //{
  //  text("Boaco", width-250, height-100);
  //}
  //if (mouseOverColor == d2)
  //{
  //  text("Carazo", width-250, height-100);
  //}
  //if (mouseOverColor == d3)
  //{
  //  text("Chinandega", width-250, height-100);
  //}
  //if (mouseOverColor == d4)
  //{
  //  text("Chontales", width-250, height-100);
  //}
  //if (mouseOverColor == d5)
  //{
  //  text("Estelí", width-250, height-100);
  //}
  //if (mouseOverColor == d6)
  //{
  //  text("Granada", width-250, height-100);
  //}
  //if (mouseOverColor == d7)
  //{
  //  text("Jinotega", width-250, height-100);
  //}
  //if (mouseOverColor == d8)
  //{
  //  text("León", width-250, height-100);
  //}
  //if (mouseOverColor == d9)
  //{
  //  text("Madriz", width-250, height-100);
  //}
  //if (mouseOverColor == d10)
  //{
  //  text("Managua", width-250, height-100);
  //}
  //if (mouseOverColor == d11)
  //{
  //  text("Masaya", width-250, height-100);
  //}
  //if (mouseOverColor == d12)
  //{
  //  text("Matagalpa", width-250, height-100);
  //}
  //if (mouseOverColor == d13)
  //{
  //  text("Nueva Segovia", width-250, height-100);
  //}
  //if (mouseOverColor == d14)
  //{
  //  text("Rivas", width-250, height-100);
  //}
  //if (mouseOverColor == d15)
  //{
  //  text("Río San Juan", width-250, height-100);
  //}
  //if (mouseOverColor == d16)
  //{
  //  text("N. Autonomous Region", width-250, height-100);
  //}
  //if (mouseOverColor == d17)
  //{
  //  text("S. Autonomous Region", width-250, height-100);
  //}
  //print(mouseOverColor);
}
