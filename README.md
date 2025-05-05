# Quadled Controller

**QuadLED Controller** is a modular, high-power tabletop controller designed to operate up to four LED panels simultaneously. It features embedded control with a local interface and remote access via a desktop application.

This repository contains the full stack of the project including:

- **Hardware design**
- **Embedded firmware**
- **Desktop application for production configuration**
- **Technical documentation**


## 🔧 Project Structure

```
quadled-controller/
├── hardware/ # Schematics, PCB design files
├── firmware/ # MCU firmware source
├── desktop-app/ # desktop app  source
├── docs/ # Sphinx documentation (specs, risks, milestones)
├── README.md
└── LICENSE.md
```

## 📌 Key Features

### LED Controller

- 4 independent high-power channels (186.5W each)
- Custom waveform control (sin/square, 0.001–10 kHz)
- Arm/fire safety logic per channel
- Display panel with encoder dial and button controls
- Audio feedback for safety warnings
- Headless operation via serial protocol

### Desktop Application

- EEPROM configuration read/write tool for production
- Manual assignment of LED panel parameters
- Simple, production-focused GUI


## 📚Documentation

All specifications, requirements, risks, and system architecture are maintained in the `docs/` folder using [Sphinx](https://www.sphinx-doc.org/) and [`sphinx-needs`](https://sphinx-needs.readthedocs.io/)

### Build HTML Documentation

From the `root` directory:

```
make html
```
Then open the generated documentation in your browser: [build/html/index.html](build/html/index.html)

### Build PDF Documentation

From the `root` directory:

```
make latexpdf
```
Then open the generated documentation in your browser: [build/latex/refmanual.pdf](build/latex/refmanual.pdf)


## ⚙️ Build & Run

Instructions for each component are located in their respective folders:

- [hardware/README.md](hardware/README.md) – PCB design notes, tools used

- [firmware/README.md](firmware/README.md) – toolchain setup, build commands

- [desktop-app/README.md](desktop-app/README.md) – prerequisites and how to run

### Add your files

- [Create](https://docs.gitlab.com/ee/user/project/repository/web_editor.html#create-a-file) or [upload](https://docs.gitlab.com/ee/user/project/repository/web_editor.html#upload-a-file) files
- [Add files using the command line](https://docs.gitlab.com/topics/git/add_files/#add-files-to-a-git-repository) or push an existing Git repository with the following command:


## 🛡️ License

This project is licensed under the MIT License – see the LICENSE file for detail.