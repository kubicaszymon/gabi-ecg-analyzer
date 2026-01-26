# Klasyfikacja zaburzeń rytmu serca (EKG) – Machine Learning

## Opis projektu

Projekt ma na celu stworzenie modelu klasyfikacyjnego opartego na uczeniu maszynowym, który automatycznie rozpoznaje typy uderzeń serca na podstawie sygnału EKG. Automatyzacja tego procesu wspiera diagnostykę kardiologiczną poprzez szybką identyfikację stanów patologicznych.

## Źródło danych

Analiza wykorzystuje **MIT-BIH Arrhythmia Database** — referencyjny zbiór danych opracowany przez Massachusetts Institute of Technology i Boston's Beth Israel Hospital (Moody & Mark, 2001). Dane w formacie przetworzonym pochodzą z repozytorium [Kaggle ECG Heartbeat Categorization Dataset](https://www.kaggle.com/datasets/shayanfazeli/heartbeat), przygotowane zgodnie z metodologią Kachuee et al. (2018).

- Zbiór treningowy: `mitbih_train.csv` (87 554 próbek)
- Zbiór testowy: `mitbih_test.csv` (21 892 próbki)
- Każda próbka: 187 znormalizowanych wartości amplitudy sygnału EKG

## Klasyfikacja diagnostyczna (AAMI)

Zgodnie z rekomendacjami Association for the Advancement of Medical Instrumentation, sygnały klasyfikowane są do 5 kategorii:

| Klasa | Symbol | Opis |
|-------|--------|------|
| 0 | N | Rytm normalny, bloki odnogi pęczka Hisa, pobudzenia ucieczkowe |
| 1 | S | Przedwczesne pobudzenia przedsionkowe i nadkomorowe |
| 2 | V | Przedwczesne skurcze komorowe, pobudzenia ucieczkowe komorowe |
| 3 | F | Pobudzenia zlane (fuzja) |
| 4 | Q | Pobudzenia stymulowane, nieklasyfikowalne |

## Metodologia

### Przetwarzanie sygnału
- Filtracja gaussowska (redukcja szumu wysokoczęstotliwościowego)
- Inżynieria cech: pierwsza i druga pochodna sygnału

### Modele
1. **Regresja logistyczna (OvR)** — interpretowalny baseline z ważeniem klas
2. **Sieć neuronowa MLP** — architektura 561→64→32→5 z ReLU

### Ewaluacja
- Macierz pomyłek z analizą błędów per klasa
- Metryki: accuracy, precision, recall, F1 (macro/weighted)
- 5-krotna walidacja krzyżowa ze stratyfikacją

## Wyniki

| Model | Accuracy | F1 (macro) | F1 (weighted) |
|-------|----------|------------|---------------|
| Regresja logistyczna | ~94% | ~0.65 | ~0.93 |
| Sieć neuronowa (MLP) | ~95% | ~0.68 | ~0.94 |

Wyniki są zgodne z literaturą — Kachuee et al. (2018) raportowali 93.4% accuracy dla CNN na tym samym zbiorze.

## Technologie

- `pandas`, `numpy` — przetwarzanie danych
- `matplotlib`, `seaborn` — wizualizacja
- `scikit-learn` — modelowanie i ewaluacja
- `PyTorch` — sieć neuronowa
- `scipy` — filtracja sygnału

---

**Autorzy:** Kubica Szymon, Siwirski Julian
