# Cithara

<p align="center">
  <img alt="Live Site" src="https://img.shields.io/badge/site-live-green?style=for-the-badge&logo=vercel">
  <img alt="CI Status" src="https://img.shields.io/github/actions/workflow/status/ralphmettle/Cithara/ci.yaml?style=for-the-badge&label=CI&logo=github">
  <img alt="Last Commit" src="https://img.shields.io/github/last-commit/ralphmettle/Cithara?style=for-the-badge">
  <img alt="Built with Next.js" src="https://img.shields.io/badge/frontend-Next.js-black?style=for-the-badge&logo=next.js">
  <img alt="Built with Django" src="https://img.shields.io/badge/backend-Django-092E20?style=for-the-badge&logo=django">
  <img alt="Python version" src="https://img.shields.io/badge/python-3.12+-blue?style=for-the-badge&logo=python">
  <img alt="TypeScript version" src="https://img.shields.io/badge/typescript-5.8.3-3178C6?style=for-the-badge&logo=typescript&logoColor=white">
  <img alt="License" src="https://img.shields.io/github/license/ralphmettle/Cithara?style=for-the-badge">
</p>

Cithara is a comprehensive music theory toolkit and exploration platform designed to help users understand and interact with musical concepts such as notes, intervals, scales, and chords. The project combines a Python core library, a Django REST API backend, and a React/Next.js frontend to provide an interactive and educational experience.


---

## Table of Contents

- [Cithara](#cithara)
  - [Table of Contents](#table-of-contents)
  - [Overview](#overview)
  - [Project Structure](#project-structure)
  - [Core Features](#core-features)
  - [Getting Started](#getting-started)
    - [Prerequisites](#prerequisites)
    - [Backend Setup](#backend-setup)
    - [Frontend Setup](#frontend-setup)
  - [Usage](#usage)
  - [Development](#development)
  - [Technologies Used](#technologies-used)
  - [Contributing](#contributing)
  - [Roadmap / To Be Completed](#roadmap--to-be-completed)
  - [License](#license)

---

## Overview

The Cithara Project consists of three main parts:

- **Core Library (`cithara/core`)**: A Python library implementing music theory logic — notes, intervals, scales, chords, and related utilities. This is designed to be robust, type-annotated, and modular for easy reuse.
  
- **Backend API (`backend`)**: A Django REST Framework-based API that exposes the core library functionalities through HTTP endpoints. This enables external clients, such as the frontend, to query and interact with musical data.
  
- **Frontend Application (`frontend`)**: A React/Next.js web application that provides a user-friendly, mobile-first interface for exploring musical scales, chords, and theory relationships, powered by the backend API.

---

## Project Structure

```txt
cithara-project/
├── cithara/              # Core Python music theory library
│   ├── core/
│   └── utils/
├── backend/              # Django REST API backend
│   ├── apps/
│   ├── config/
│   └── manage.py
├── frontend/             # Next.js frontend
│   ├── app/
│   ├── components/
│   └── public/
├── README.md
├── requirements.txt
└── package.json
```

---

## Core Features

- **Note and Interval Representation**: Precise handling of musical notes, accidentals, pitch classes, and intervals.
- **Scale and Chord Generation**: Ability to create major, minor, diminished, augmented scales and chords.
- **Diatonic and Chromatic Relationships**: Supports exploring relationships between notes and chords within scales.
- **API Access**: Exposes music theory computations as RESTful endpoints.
- **Interactive Demo**: Allows users to select notes, accidentals, and scales/chords to explore their structure dynamically.

---

## Getting Started

### Prerequisites

- Python 3.12+
- Node.js (for frontend)
- pnpm or npm/yarn package manager

### Backend Setup

```bash
cd .
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

### Frontend Setup

```bash
cd frontend
pnpm install
pnpm dev
```

---

## Usage

- Visit the frontend at <http://localhost:3000> (or your deployed URL).
- Use the interface to select root notes, accidentals, and scale types.
- Submit selections to fetch scale data dynamically from the backend.
- Explore generated scales and chords with interactive visual components.

---

## Development

- Follow test-driven development practices; tests live primarily in the backend tests/ directory.
- Backend API is built with Django REST Framework.
- Frontend uses React with Next.js and Tailwind CSS for styling.
- Core library is standalone Python code designed for reuse or extension.
- Use GitHub Actions for CI/CD including linting and type checks.

---

## Technologies Used

- Python 3.12, Django, Django REST Framework
- TypeScript, React, Next.js, Tailwind CSS
- Docker (planned)
- GitHub Actions for CI/CD

---

## Contributing

Contributions are welcome! Please fork the repository and submit pull requests with clear descriptions and tests where applicable :3

---

## Roadmap / To Be Completed
  
- *Core Library:* Add more scale and chord types, refine enharmonic logic, improve documentation (documentation webpage, library docstrings), MIDI support.
- *Backend API:* Build a web API for data retrieval.
- *Frontend:* Build comprehensive UI with more interactive components, better error handling and display, mobile optimisation, and potential user onboarding for full online Cithara app.
- *Deployment:* Set up CI/CD for backend and make backend deployment for site interactivity.
- *CLI Tool: (Planned)* Add a command-line interface for users to interact with the library directly.
- *Documentation Site:* Develop detailed user and developer documentation, tutorials, and example projects.

---

## License

This project is licensed under the **GNU General Public License v3.0 (GNU GPLv3)**.

---

***Created and maintained by Ralph Mettle***
