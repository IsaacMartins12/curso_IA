#include <Ultrasonic.h>  //Biblioteca responsável pelo funcionamento do sensor ultrassonico
#include <MD_YX5300.h> // Biblioteca responsável pelo módulo mp3
#include <SoftwareSerial.h>

#define pino_trigger 2
#define pino_echo 3
#define ARDUINO_RX 5  //should connect to TX of the Serial MP3 Player module
#define ARDUINO_TX 6  //connect to RX of the module

SoftwareSerial mp3(ARDUINO_RX, ARDUINO_TX); // Inicia serial do modulo YX

Ultrasonic ultrasonic(pino_trigger, pino_echo); // Instancia um objeto da classe Ultrasonic

static int8_t Send_buf[8] = {0}; //Buffer para enviar comandos para o modulo MP3
static uint8_t ansbuf[10] = {0}; //Buffer para receber a resposta do modulo MP3

String mp3Answer;           //String para resposta do modulo MP3

String sanswer(void); //Prototipo de funcao
String sbyte2hex(uint8_t b); //Prototipo de funcao

/************ Command byte **************************/
#define CMD_NEXT_SONG     0X01  // Play next song.
#define CMD_PREV_SONG     0X02  // Play previous song.
#define CMD_PLAY_W_INDEX  0X03
#define CMD_VOLUME_UP     0X04
#define CMD_VOLUME_DOWN   0X05
#define CMD_SET_VOLUME    0X06

#define CMD_SNG_CYCL_PLAY 0X08  // Single Cycle Play.
#define CMD_SEL_DEV       0X09
#define CMD_SLEEP_MODE    0X0A
#define CMD_WAKE_UP       0X0B
#define CMD_RESET         0X0C
#define CMD_PLAY          0X0D
#define CMD_PAUSE         0X0E
#define CMD_PLAY_FOLDER_FILE 0X0F

#define CMD_STOP_PLAY     0X16  // Stop playing continuously. 
#define CMD_FOLDER_CYCLE  0X17
#define CMD_SHUFFLE_PLAY  0x18 //
#define CMD_SET_SNGL_CYCL 0X19 // Set single cycle.

#define CMD_SET_DAC 0X1A
#define DAC_ON  0X00
#define DAC_OFF 0X01

#define CMD_PLAY_W_VOL    0X22
#define CMD_PLAYING_N     0x4C
#define CMD_QUERY_STATUS      0x42
#define CMD_QUERY_VOLUME      0x43
#define CMD_QUERY_FLDR_TRACKS 0x4e
#define CMD_QUERY_TOT_TRACKS  0x48
#define CMD_QUERY_FLDR_COUNT  0x4f

/************ Opitons **************************/
#define DEV_TF            0X02

/*********************************************************************/

char c = ' ';

void setup()
{
  pinMode(pino_trigger, OUTPUT);
  pinMode(pino_echo,INPUT);
  pinMode(4,OUTPUT); // Led indicador
  Serial.begin(9600);
  mp3.begin(9600);
  sendCommand(CMD_SEL_DEV, 0, DEV_TF);
  delay(500);
}
 
void loop()
{  
  long microsec = ultrasonic.timing();
  float cmMsec, inMsec;
 
  // Check for the answer.
  if (mp3.available())
  {
    Serial.println(decodeMP3Answer());
  }
  
  delay(100);

  cmMsec = ultrasonic.convert(microsec, Ultrasonic::CM);
  
   if(cmMsec < 40){
      Serial.println(cmMsec);
      Serial.println("Tocando ! ...");
      sendCommand(CMD_PLAY);
   }
   else{
     sendCommand(CMD_STOP_PLAY);
     Serial.println(cmMsec);
   }
  delay(300);
}


/********************************************************************************/
//Menu de controles do Modulo MP3

void sendMP3Command(char c) {
  
  switch (c) {
    case '?':
    case 'h':
      Serial.println("HELP  ");
      Serial.println(" p = Play");
      Serial.println(" P = Pause");
      Serial.println(" > = Next");
      Serial.println(" &lt; = Previous");
      Serial.println(" s = Stop Play"); 
      Serial.println(" + = Volume UP");
      Serial.println(" - = Volume DOWN");
      Serial.println(" f = Play folder 1.");
      Serial.println(" S = Sleep");
      Serial.println(" W = Wake up");
      Serial.println(" r = Reset");
      break;


    case 'p':
      Serial.println("Play ");
      sendCommand(CMD_PLAY);
      break;

    case 'P':
      Serial.println("Pause");
      sendCommand(CMD_PAUSE);
      break;

    case '>':
      Serial.println("Next");
      sendCommand(CMD_NEXT_SONG);
      sendCommand(CMD_PLAYING_N); // ask for the number of file is playing
      break;

    case '&lt;':
      Serial.println("Previous");
      sendCommand(CMD_PREV_SONG);
      sendCommand(CMD_PLAYING_N); // ask for the number of file is playing
      break;

    case 's':
      Serial.println("Stop Play");
      sendCommand(CMD_STOP_PLAY);
      break;


    case '+':
      Serial.println("Volume Up");
      sendCommand(CMD_VOLUME_UP);
      break;

    case '-':
      Serial.println("Volume Down");
      sendCommand(CMD_VOLUME_DOWN);
      break;

    case 'f':
      Serial.println("Playing folder 1");
      sendCommand(CMD_FOLDER_CYCLE, 1, 0);
      break;

    case 'S':
      Serial.println("Sleep");
      sendCommand(CMD_SLEEP_MODE);
      break;

    case 'W':
      Serial.println("Wake up");
      sendCommand(CMD_WAKE_UP);
      break;

    case 'r':
      Serial.println("Reset");
      sendCommand(CMD_RESET);
      break;
  }
}


//Funcao para decodificar a resposta do modulo MP3

String decodeMP3Answer() {
  String decodedMP3Answer = "";

  decodedMP3Answer += sanswer();

  switch (ansbuf[3]) {
    case 0x3A:
      decodedMP3Answer += " -> Cartao de Memoria inserido.";
      break;

    case 0x3D:
      decodedMP3Answer += " -> Musica tocada completamente " + String(ansbuf[6], DEC);
      break;

    case 0x40:
      decodedMP3Answer += " -> Erro!";
      break;

    case 0x41:
      decodedMP3Answer += " -> Dados recebidos corretamente. ";
      break;

    case 0x42:
      decodedMP3Answer += " -> Estado de Toque: " + String(ansbuf[6], DEC);
      break;

    case 0x4C:
      decodedMP3Answer += " -> Tocando: " + String(ansbuf[6], DEC);
      break;
  }

  return decodedMP3Answer;
}

/********************************************************************************/
//Funcao para enviar um comando para o modulo MP3

void sendCommand(byte command){
  sendCommand(command, 0, 0);
}

void sendCommand(byte command, byte dat1, byte dat2){
  delay(20);
  Send_buf[0] = 0x7E;    //
  Send_buf[1] = 0xFF;    //
  Send_buf[2] = 0x06;    // Len
  Send_buf[3] = command; //
  Send_buf[4] = 0x01;    // 0x00 NO, 0x01 feedback
  Send_buf[5] = dat1;    // datah
  Send_buf[6] = dat2;    // datal
  Send_buf[7] = 0xEF;    //
  Serial.print("Sending: ");
  for (uint8_t i = 0; i < 8; i++)
  {
    mp3.write(Send_buf[i]) ;
    Serial.print(sbyte2hex(Send_buf[i]));
  }
  Serial.println();
}



/********************************************************************************/
//Funcao para retornar um byte em formato hexadecimal


String sbyte2hex(uint8_t b)
{
  String shex;

  shex = "0X";

  if (b < 16) shex += "0";
  shex += String(b, HEX);
  shex += " ";
  return shex;
}

/********************************************************************************/
//Funcao de conversao de hexadecimal

int shex2int(char *s, int n){
  int r = 0;
  for (int i=0; i<n; i++){
     if(s[i]>='0' && s[i]<='9'){
      r *= 16; 
      r +=s[i]-'0';
     }else if(s[i]>='A' && s[i]<='F'){
      r *= 16;
      r += (s[i] - 'A') + 10;
     }
  }
  return r;
}


/********************************************************************************/
//Funcao que retorna uma string como resposta do módulo MP3

String sanswer(void)
{
  uint8_t i = 0;
  String mp3answer = "";

  // Get only 10 Bytes
  while (mp3.available())
  {
    uint8_t b = mp3.read();
    ansbuf[i] = b;
    i++;

    mp3answer += sbyte2hex(b);
  }

  // if the answer format is correct.
  if ((ansbuf[0] == 0x7E) && (ansbuf[9] == 0xEF))
  {
    return mp3answer;
  }

  return "???: " + mp3answer;
}
