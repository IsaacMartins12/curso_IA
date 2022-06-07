 int numeros[4];
  int teste[4] = {0,0,0,0};
  int pressionado1 = 0,pressionado2 = 0, pressionado3 = 0, pressionado4 = 0 ;
  int cont0 = 0,cont1 = 0, cont2 = 0, cont3 = 0, acerto=0, clicks=0 , i=-1;
  int time = 1500;

void setup()
{
  Serial.begin(9600);
  pinMode(2, INPUT_PULLUP); // botao 1
  pinMode(3, INPUT_PULLUP); // botao 2
  pinMode(4, INPUT_PULLUP); // botao 3
  pinMode(5, INPUT_PULLUP); // botao 4
  pinMode(6, OUTPUT); // Led 1
  pinMode(7, OUTPUT); // Led 2
  pinMode(8, OUTPUT); // Led 3
  pinMode(9, OUTPUT); // Led 4
  pinMode(10, OUTPUT); // Led de Acerto
  pinMode(11, OUTPUT); // Led de Erro
  
  randomSeed(analogRead(0));
  numeros[0] = random(6, 10);
  numeros[1] = random(6, 10);
  numeros[2] = random(6, 10);
  numeros[3] = random(6, 10);
  Serial.println("Sorteei os numeros : ");
  Serial.println(numeros[0]);
  Serial.println(numeros[1]);		
  Serial.println(numeros[2]);
  Serial.println(numeros[3]);
  Serial.println("Aguardando pra iniciar : ");
  delay(3000);
  
}

void loop()
{          
  if(cont0==0){
    mostrafase1();
    cont0=1;
  }
  if(cont0==1 && cont1==0){
  while(1){
  
  clicks = lerbotoes();
  
   if(clicks==1){
     
      if (teste[0] == (numeros[0]-4)) {acerto++;}
     
     if (acerto == 1){
       certo();
       cont1=1;
       config();
       mostrafase2();
       break;
     }
   
    if(acerto!=1){
    errado();
    mostrafase1();
    config();
   }
   }
  }
 }
  
  if (cont1==1){
  
  while(1){
  
  clicks = lerbotoes();
  
   if(clicks==2){
     int j;
     
      if (teste[0] == (numeros[0]-4)){acerto++;}
      if (teste[1] == (numeros[1]-4)){acerto++;}

     if (acerto == 2){
       certo();
       cont1=0;
       cont2=1;
       config();
       mostrafase3();
       break;
     }
   
   if(acerto!=2){
    errado();
    mostrafase2();
    config();
   }
   }
  }
  }

  if (cont2==1){
  
  while(1){
  clicks = lerbotoes();
  
   if(clicks==3){
     int j;
      
     for (j=0;j<3;j++){
      
     if (teste[j] == (numeros[j]-4)){ acerto++;}
     
     }
     
     
     if (acerto == 3){
       certo();
       cont2=0;
       cont3=1;
       config();
       mostrafase4();
       break;
     }
   
    if(acerto!=3){
    errado();
    mostrafase3();
    config();
   }
   }
  }
  }
  
  
  // Acertou os da fase4 e finaliza o jogo
  
  if (cont3==1){
  
  while(1){
  clicks = lerbotoes();
  
   if(clicks==4){
     Serial.println("blaa");
     int j;
     
     for (j=0;j<4;j++){
      if (teste[j] == (numeros[j]-4)){acerto++;}
     }
     
     if (acerto == 4){
       certo();
       delay(2000);
       cont0=0;
       cont1=0;
       cont2=0;
       cont3=0;
       config();
       setup();
       break;
     }
   
   if(acerto!=4){
    errado();
    mostrafase4();
    config();
   }
   }
  }
  }
  }

// Procedimentos e funcoes

void config(){
    Serial.println("Configuracoes de operacao");
    acerto=0;
    clicks=0;
    i=-1;
    int teste[4] = {0,0,0,0};
}
void certo(){
  Serial.println("Resposta certa !");
  digitalWrite(10,1);
  delay(2000);
  digitalWrite(10,0);
  delay(1000);
}

void errado(){
    Serial.println("Resposta errada !");
    digitalWrite(11,1);
    delay(1000);
    digitalWrite(11,0);
    delay(1000);
}

void mostrafase1(){
    Serial.println("Mostrando a fase 1");
    delay(time);
    digitalWrite(numeros[0],1);
    delay(time);
    digitalWrite(numeros[0],0);
    delay(time);
}

void mostrafase2(){
    Serial.println("Mostrando a fase 2");
    digitalWrite(numeros[0],1);
    delay(time);
    digitalWrite(numeros[0],0);
    delay(time);
    digitalWrite(numeros[1],1);
    delay(time);
    digitalWrite(numeros[1],0);
}

void mostrafase3(){
  Serial.println("Mostrando a fase 3");
  digitalWrite(numeros[0],1);
  delay(time);
  digitalWrite(numeros[0],0);
  delay(time);
  digitalWrite(numeros[1],1);
  delay(time);
  digitalWrite(numeros[1],0);
  delay(time);
  digitalWrite(numeros[2],1);
  delay(time);
  digitalWrite(numeros[2],0);
}

void mostrafase4(){
  Serial.println("Mostrando a fase 4");
  digitalWrite(numeros[0],1);
  delay(time);
  digitalWrite(numeros[0],0);
  delay(time);
  digitalWrite(numeros[1],1);
  delay(time);
  digitalWrite(numeros[1],0);
  delay(time);
  digitalWrite(numeros[2],1);
  delay(time);
  digitalWrite(numeros[2],0);
  delay(time);
  digitalWrite(numeros[3],1);
  delay(time);
  digitalWrite(numeros[3],0);
}

int lerbotoes(){
  if (digitalRead(2)==1){
    i++;
    teste[i] = 2 ;
    pressionado1=1;
    delay(500);
    clicks+=1;
    pressionado1=0;
  }
  
  if (digitalRead(3)==1){
    i++;
    teste[i] = 3 ;
    pressionado2=1;
    delay(500);
    clicks+=1;
    pressionado2=0;
  }
  
  if (digitalRead(4)==1){
    i++;
    teste[i] = 4 ;
    pressionado3=1;
    delay(500);
    clicks+=1;
    pressionado3=0;
  }
    if (digitalRead(5)==1){
     i++;
     teste[i] = 5 ;
     pressionado4=1;
     delay(500);
     clicks+=1;
     pressionado4=0;
  }
  Serial.println(clicks);
  return clicks;
}
