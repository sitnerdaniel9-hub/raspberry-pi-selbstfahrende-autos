# Autonome Roboter-Autos mit Raspberry Pi

Erstes Semester-Projekt (Modul "Startprojekt")
Programmierung autonomer Fahrzeuge mit dem PiCar-X Roboter (Gruppenarbeit)

## Projektbeschreibung

Entwicklung verschiedener autonomer Fahrfunktionen für einen PiCar-X Roboter auf Basis eines Raspberry Pi. Das Projekt umfasste grundlegende Motorsteuerung, Sensordatenverarbeitung, Computer Vision und eigenständige Entscheidungsfindung.

## Mein Beitrag

Hauptverantwortung für die Entwicklung der Steuerungslogik und Sensordatenverarbeitung über alle Aufgaben hinweg.

## Technologien

- **Hardware:** Raspberry Pi, PiCar-X Roboter-Kit
- **Programmierung:** Python 3.9
- **Sensoren:** Infrarot-Liniensensor (Grayscale), Ultraschall-Distanzsensor, Kamera
- **Bibliotheken:** GPIO-Steuerung, PWM, I2C, ADC

## Aufgaben & Features

### Aufgabe 1: Grundlegende Motorsteuerung
- Geradeausfahrt über definierte Distanz (1 Meter)
- Präzises Stoppen
- *Herausforderung: Hardware-Kalibrierung*

### Aufgabe 2: Komplexe Fahrmanöver
- Fahren einer Acht-Kurve
- Autonomes Zurückparken am Startpunkt
- *Herausforderung: Präzise Lenkung ohne Sensorfeedback*

### Aufgabe 3: Linienverfolgung (Basis)
- Autonomes Folgen einer schwarzen Bodenlinie
- Selbstständige Kurskorrektur bei Abweichungen
- Verwendung von Infrarot-Liniensensoren

### Aufgabe 4: Linienverfolgung (Fortgeschritten)
Optimierte Version von Aufgabe 3 mit verbesserter Regelungstechnik:
- **Sanfte Lenkbewegungen:** Schrittweises Erhöhen des Lenkwinkels statt abrupter Richtungsänderungen
- **Adaptive Geschwindigkeit:** Automatische Geschwindigkeitsreduktion in Kurven
- **Intelligente Linienwiederfindung:** Rückwärtsfahrt mit Lenkung zur Liniensuche bei Verlust
- **Zustandsbasierte Steuerung:** Speicherung des letzten Fahrzustands für vorausschauende Entscheidungen

### Aufgabe 5: Hinderniserkennung & Spurwechsel
- Automatisches Anhalten bei Objekten in definierter Distanz
- Autonomer Spurwechsel auf Parallelfahrbahn
- Ultraschall-basierte Distanzmessung

### Aufgabe 6: Verkehrszeichenerkennung
- Erweiterung der Linienverfolgung um Schildererkennung
- Automatisches Stoppen bei Stoppschildern
- **Technische Lösung:** Farbbasierte Erkennung (Lila als Stoppfarbe, da am seltensten im Raum vorkommend)
- *Hinweis: ML-basierte Schildererkennung war hinter Paywall - daher pragmatischer Ansatz über Farbfilterung*

## Projektstruktur
```
├── aufgabe1.py          # Grundlegende Motorsteuerung
├── aufgabe2.py          # Komplexe Fahrmanöver
├── aufgabe3.py          # Linienverfolgung (Basis)
├── aufgabe4.py          # Linienverfolgung (Optimiert)
├── aufgabe5.py          # Hinderniserkennung & Spurwechsel
├── chechSings.py        # Schildererkennung (Farbfilter)
└── Testverzeichnis/     # PiCar-X Bibliotheken
    ├── picarx.py        # Haupt-API für Roboter
    └── unterprogramme/  # Motor, Servo, Sensor-Module
```

## Technische Highlights

- **Regelungstechnik:** Implementierung eines zustandsbasierten Controllers mit Feedback-Loop
- **Sensor-Fusion:** Verarbeitung von 3-fach Grayscale-Sensor-Daten zur Positionsbestimmung
- **Adaptive Algorithmen:** Dynamische Anpassung von Lenkwinkel und Geschwindigkeit basierend auf Fahrsituation

## Learnings

- Hardware-Integration und -Kalibrierung in der Praxis
- Sensordatenverarbeitung und Regelungstechnik
- Iterative Optimierung von Steuerungsalgorithmen (Aufgabe 3 → 4)
- Pragmatische Lösungsfindung bei technischen Einschränkungen
- Teamarbeit in der Hardwareentwicklung

## Hardware-Herausforderungen

Das Projekt war teilweise durch instabile Hardware erschwert (insbesondere in Aufgaben 1-2).

---

*Entwickelt im Wintersemester 2024/25 als Teil des Moduls "Startprojekt" (1. Semester). Der Fokus lag auf praktischer Hardware-Programmierung - fortgeschrittene Software-Engineering-Prinzipien wurden in späteren Projekten angewendet.*