# Handheld-Musical-Instrument-App

A Kivy/KivyMD-based piano octave application that works on **Android** using the device's accelerometer to change octaves, and on **PC** using a slider and keyboard key bindings.

## Features
- **Android:** Uses the accelerometer to adjust the octave in real-time.
- **PC:** Mimics accelerometer values using a slider.
- **Keyboard Bindings:** Use `Q W E R T Y U` keys to play notes `C D E F G A B`.
- Displays the **current note** being played.
- Color-coded note buttons with responsive layout.

---
## Android Functionality (Tilt to Change Octave)

When running on **Android** (via [Pydroid 3](https://play.google.com/store/apps/details?id=ru.iiec.pydroid3) or any Kivy-compatible environment), the app uses your device’s **accelerometer** to detect tilt:

- **Tilt Forward / Backward** → Changes the `y` acceleration value.
- The app maps the `y` value to an **octave number** (2–7) using predefined ranges.
- The current octave is shown vertically on the **right-hand side** of the screen under the label **"OCTAVE"**.
- Tap any note button (**C, D, E, F, G, A, B**) to play that note in the current octave.

This creates a **realistic octave shift** effect by simply tilting your phone!

---

## PC Functionality (Testing Mode)

If you run this on your PC:

- Use the **slider** at the bottom to mimic the accelerometer tilt.
- Use **keyboard keys** to play notes:
  - `Q` → C  
  - `W` → D  
  - `E` → E  
  - `R` → F  
  - `T` → G  
  - `Y` → A  
  - `U` → B  

---
## Installation

### 1. Clone the repository
```bash
git clone https://github.com/djboi07/piano-octave-app.git
cd piano-octave-app
```

### 2. Install dependencies (PC)
It is recommended to use a **virtual environment**:
```bash
pip install -r requirements.txt
```

### 3. Running on PC
```bash
python main.py
```
You can:
- Use the **slider** to mimic accelerometer changes.
- Press **Q W E R T Y U** keys to play notes.

---

## Running on Android 

1. Install **Pydroid 3** from the Google Play Store.
2. Open Pydroid 3, then install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Place the `notes_files` folder in the same directory as `main.py` on your device.
4. Run `main.py` from Pydroid.

**Note:** On Android, the slider is still visible but the accelerometer takes priority in controlling the octave.

---

## Project Structure
```
.
├── main.py
├── notes_files/
│   ├── c2.mp3
│   ├── d2.mp3
│   └── ...
├── requirements.txt
├── README.md
└── HBD_sample.mp4
```

---

## Dependencies
- **Kivy**
- **KivyMD**
- **Pygame**
- **Plyer** (for accelerometer access)
  
<img width="345" height="594" alt="SampleScreenshot" src="https://github.com/user-attachments/assets/17af1bf0-8db7-4e13-9954-2027104372e9" />


