# Klasyfikacja zaburzeń rytmu serca (EKG) – Machine Learning

## Opis projektu

Projekt ma na celu stworzenie zaawansowanego modelu klasyfikacyjnego opartego na uczeniu maszynowym, który potrafi automatycznie rozpoznawać typy uderzeń serca na podstawie sygnału EKG. Automatyzacja tego procesu stanowi kluczowe wsparcie dla diagnostyki kardiologicznej, umożliwiając szybką identyfikację stanów patologicznych.

Analiza została przeprowadzona na uznanym zbiorze danych MIT-BIH Arrhythmia Database.

## Klasyfikacja diagnostyczna

Model klasyfikuje sygnały do 5 głównych kategorii:

- Klasa 0: Rytm normalny (w tym bloki pęczka Hisa, pobudzenia ucieczkowe).

- Klasa 1: Przedwczesne pobudzenie przedsionkowe (nadkomorowe).

- Klasa 2: Przedwczesne skurcze komorowe oraz ucieczkowe pobudzenia komorowe.

- Klasa 3: Pobudzenie zlane (Fusion).

- Klasa 4: Pobudzenia stymulowane (rozruszniki) oraz nieklasyfikowalne.

## Technologie

Projekt został zrealizowany w języku Python przy użyciu następujących bibliotek:

- `pandas` & `numpy` – obróbka i analiza danych.

- `matplotlib` & `seaborn` – wizualizacja sygnałów EKG i wyników.

- `scikit-learn` – podział danych i ewaluacja modeli.

- `xgboost` – zaawansowane modelowanie klasyfikacyjne.

## Analiza danych i modelowanie

1. Zbiór danych: Wykorzystano dane z plików mitbih_train.csv (87 554 próbek) oraz mitbih_test.csv.

2. Preprocessing: Każdy sygnał składa się ze 187 znormalizowanych wartości amplitudy sygnału w czasie.

3. Wizualizacja: W notatniku zawarto analizę morfologii załamków, pozwalającą dostrzec różnice w zespole QRS dla poszczególnych schorzeń.

4. Raportowanie: System zawiera funkcję generate_patient_report, która automatyzuje proces diagnozy.

## Przykładowy raport diagnostyczny

Model generuje sformatowany raport dla personelu medycznego:

```plaintext
════════════════════════════════════════════════════════════════
DIAGNOZA
════════════════════════════════════════════════════════════════

Klasyfikacja:   Przedwczesne skurcze komorowe (Ventricular contraction)
Stopień:        UMIARKOWANE

ZALECENIA:      KONIECZNA pilna konsultacja kardiologiczna.
```

## Zastrzeżenie medyczne

Raporty generowane przez ten system są wynikiem działania modeli sztucznej inteligencji i służą wyłącznie jako narzędzie pomocnicze. Każda diagnoza wymaga ostatecznej weryfikacji przez wykwalifikowanego lekarza kardiologa.

---

Autorzy: Kubica Szymon, Siwirski Julian