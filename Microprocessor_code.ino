
// Variables usadas
int adc = A0;
int planox = 0;
int planoz = 0;
int planoy = 0;
int index = 0;
float xn1 = 0;
float yn1 = 0;
const int num_samples = 5;
int sample_index = 0;

// Arreglo para almacenar muestras
float samples[num_samples];

void setup() {
  Serial.begin(115200);
  pinMode(A8, OUTPUT);
  pinMode(A9, OUTPUT);
  pinMode(A14, OUTPUT);
  pinMode(A15, OUTPUT);
}

void loop() {
  float pr = analogRead(adc);
  float xn = (pr * 5 * 100.0) / 1023.0;

  // Aplicar filtro IIR
  float yn = 0.9792 * yn1 + 0.0104 * xn + 0.0104 * xn1;

  xn1 = xn;
  yn1 = yn;

  // Aplicar filtro de media móvil
  samples[sample_index] = yn;
  sample_index = (sample_index + 1) % num_samples;
  float filteredValue = 0;
  for (int i = 0; i < num_samples; i++) {
    filteredValue += samples[i];
  }
  filteredValue /= num_samples;

  float finalValue = filteredValue - 80;
  Serial.println(finalValue);

  if (index == 0) {
    digitalWrite(A8, LOW);
    digitalWrite(A9, LOW);
    digitalWrite(A14, LOW);
    digitalWrite(A15, LOW);
    delay(2.5);
  }
  else if (index == 1) {
    digitalWrite(A8, HIGH);
    digitalWrite(A9, LOW);
    digitalWrite(A14, HIGH);
    digitalWrite(A15, LOW);
    delay(2.5);
  }
  else if (index == 2) {
    digitalWrite(A8, LOW);
    digitalWrite(A9, HIGH);
    digitalWrite(A14, LOW);
    digitalWrite(A15, HIGH);
    delay(2.5);
  }
}