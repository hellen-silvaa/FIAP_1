
void setup() {
  //configuração de pinos e variáveis.
  //Será executado só uma vez:
  pinMode(8, OUTPUT);
}

void loop () {
  //código que será repetido constantemente:
  digitalWrite(8, HIGH);
  delay(500); //espera 500 millisecond (s)
  digitalWrite(8, LOW);
  delay(500); //espera 500 millisecond (s)
}
