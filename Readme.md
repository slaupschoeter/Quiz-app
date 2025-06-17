# Quiz App

Dit is een eenvoudige webapplicatie die gebruik maakt van **Flask** voor de backend, **React** voor de frontend en **SQLAlchemy** voor de database. De applicatie is ontworpen om quizzen te beheren en deelnemers te laten deelnemen.

## Inhoudsopgave

- [Vereisten](#vereisten)
- [Installatie](#installatie)
- [Backend (Flask)](#backend-flask)
- [Frontend (React)](#frontend-react)
- [Bijdragen](#bijdragen)
- [Licentie](#licentie)

## Vereisten

Zorg ervoor dat je de volgende software hebt geïnstalleerd:

- [Python 3.x](https://www.python.org/downloads/)
- [Node.js](https://nodejs.org/en/)
- [npm](https://www.npmjs.com/get-npm) (meestal geïnstalleerd met Node.js)
- [Git](https://git-scm.com/)

## Installatie

Volg de onderstaande stappen om de applicatie lokaal te draaien.

### Backend (Flask)

1. **Maak een virtuele omgeving aan**:
   Dit is aanbevolen om afhankelijkheden gescheiden te houden van je systeeminstellingen.
   
   ```bash
   cd backend
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
