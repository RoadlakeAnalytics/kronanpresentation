# Interaktiv Presentation

## Projektbeskrivning
En interaktiv webbplats byggd med React och React Spring för att presentera ett animerat flöde med zoom- och pan-effekter.

## Installation

1. Klona repositoryt:

   git clone https://github.com/RoadlakeAnalytics/kronanpresentation.git
   cd interaktiv-presentation

2. Installera beroenden:
   npm install

3. Kör projektet lokalt:
npm start

## Deployment
Deployment sker automatiskt via GitHub Actions till GitHub Pages vid varje push till master branch.

## Uppdatera Innehåll

1.  Skapa nya slides genom att lägga till nya komponenter i `src/slides/`.
2.  Importera och inkludera dem i `App.js` med `ParallaxLayer`.
3.  För ämnesspecifika frågor, uppdatera `Topics.js` och skapa relevanta slides.

## Teknisk Specifikation

-   React
-   React Spring
-   CSS Flexbox/Grid
-   GitHub Pages
-   GitHub Actions 