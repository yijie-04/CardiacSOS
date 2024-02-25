
int Pin1 = 10;//IN1 is connected to 10 
int Pin2 = 11;//IN2 is connected to 11  
int Pin3 = 12;//IN3 is connected to 12  
int Pin4 = 13;//IN4 is connected to 13 
int switchSTOP =2;//define input pin for STOP push button
int switchCW   =3;//define input pin for CW push button
int switchCCW  =4;//define input pin for CCW push button

int speedFactor =1;//1=fastest, 2=slower or 3 more slower
long goToAngle = 90;


int correction_CW = 150;//watch video for details
int correction_CCW = 150;//watch video for details

const int CW =1;
const int CCW =2;
const int STOP =3;
int poleStep = 0; 
long stepVale =0;
const int SPR=64*64;

int pole1[] ={0,0,0,0, 0,1,1,1, 0};//pole1, 8 step values
int pole2[] ={0,0,0,1, 1,1,0,0, 0};//pole2, 8 step values
int pole3[] ={0,1,1,1, 0,0,0,0, 0};//pole3, 8 step values
int pole4[] ={1,1,0,0, 0,0,0,1, 0};//pole4, 8 step values





int count=0;
int  dirStatus = STOP;// stores direction status 3= stop (do not change)

void setup() 
{ 
  //Robojax.com Stepper Push button Any Angle STPB-4
  Serial.begin(9600);
  Serial.begin("Robojax Video for Stepper Motor STPB-2");  
 pinMode(Pin1, OUTPUT);//define pin for ULN2003 in1 
 pinMode(Pin2, OUTPUT);//define pin for ULN2003 in2   
 pinMode(Pin3, OUTPUT);//define pin for ULN2003 in3   
 pinMode(Pin4, OUTPUT);//define pin for ULN2003 in4   

 pinMode(switchSTOP,INPUT_PULLUP); 
 pinMode(switchCW,INPUT_PULLUP);
 pinMode(switchCCW,INPUT_PULLUP); 
 
} 
 void loop() 
{ 
    stepVale = (SPR * goToAngle)/360 ;
  //Robojax.com Stepper Push button Any Angle STPB-4
  if(digitalRead(switchCCW) == LOW) 
  {
    dirStatus =CCW;
    count =0;
  }else if(digitalRead(switchCW) == LOW)
  {
   dirStatus  = CW;  
    count =0;   
  }
  if(digitalRead(switchSTOP) == LOW)
  {
    dirStatus  = STOP;
    delay(200);
  }
 if(dirStatus ==CCW){ 
   poleStep++; 
   count++;   
   if(count+correction_CCW <= stepVale)
   {
    driveStepper(poleStep);      
   }else{
      driveStepper(8);  
   }
  //full explannation at Arduino Course on Udemy.com see link above
 }else if(dirStatus ==CW){ 
   poleStep--; 
   count++;   
   if(count+correction_CW <=stepVale)
   {
    driveStepper(poleStep);      
   }else{
      driveStepper(8);  
   }   
 }else{
  driveStepper(8);   
 }
 if(poleStep>7){ 
   poleStep=0;
 } 
 if(poleStep<0){ 
   poleStep=7; 
 } 
 delay(speedFactor); 
  //Robojax.com Stepper Push button Any Angle STPB-4

}// loop


/*
 * @brief moves motor to specific angle 
 * @param "angle" is integer representing the angle
 * @return does not return anything
 * 
 * www.Robojax.com code Ap1il 19 2020 at 01:22 in Ajax, Ontario, Canada
 */
void driveStepper(int c)
{
    //Robojax.com Stepper Push button Any Angle STPB-4
     digitalWrite(Pin1, pole1[c]);  
     digitalWrite(Pin2, pole2[c]); 
     digitalWrite(Pin3, pole3[c]); 
     digitalWrite(Pin4, pole4[c]);
     if(c ==8)
     {
      digitalWrite(switchCW, HIGH); 
      digitalWrite(switchCCW, HIGH);               
     }
}//driveStepper ends here
