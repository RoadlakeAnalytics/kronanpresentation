# Instruktioner för att Använda Python-skriptet

# 1. Installera Python
Se till att du har Python installerat på din dator. Du kan ladda ner det från[python.org](https: // www.python.org/downloads /) .

# 2. Spara Skriptet
Spara ovanstående kod i en fil med namnet `setup_project.py`.

# 3. Kör Skriptet
Öppna terminalen(eller kommandoprompten) och navigera till den mapp där du sparade `setup_project.py`. Kör sedan följande kommando:
python setup_project.py

Du kommer att bli ombedd att ange ditt GitHub-användarnamn och repository-namn. Detta kommer att ersätta platshållarna i `package.json` och andra filer automatiskt.

# 4. Följ Steg-för-Steg Instruktioner Efter Python-skriptet

Efter att ha kört Python-skriptet, följ dessa steg för att slutföra projektuppsättningen:

    # a. Navigera till Projektmappen
Kör följande kommando för att gå in i projektmappen:
cd interaktiv-presentation

# b. Initiera Git Repository
Om du inte redan har ett Git-repository, initiera ett nytt och lägg till fjärranslutningen till GitHub:
git init git remote add origin https://github.com/roadlakeanalytics/kronanpresentation.git

Byt ut `< username >` och `< repository-name >` med ditt faktiska GitHub-användarnamn och repository-namn.

# c. Lägg till och Commit Filer
Lägg till alla filer och gör en commit:
git add . git commit - m "Initial commit"

# d. Byt till `master` eller `main` Branch
GitHub använder ofta `main` som standardbranch. Om ditt repository använder `main`, byt till den:
git branch - M main git push -u origin main

Om du föredrar att använda `master`, ändra ovanstående kommandon till `master`.

# e. Installera Node.js och NPM
Se till att du har Node.js och npm installerade. Ladda ner från[nodejs.org](https: // nodejs.org /) .

# f. Installera Projektberoenden
Kör följande kommando för att installera alla beroenden:
npm install

# g. Hantera Deprecated Paket och Sårbarheter
För att åtgärda deprecated-varningar och sårbarheter, kör:
npm audit fix - -force

**Obs: ** Använd `- -force` endast om du är medveten om att det kan introducera brytande förändringar.

# h. Starta Projektet Lokalt
Efter att ha installerat beroenden, starta projektet:
npm start

Öppna din webbläsare och navigera till `http: // localhost: 3000` för att se din interaktiva presentation.

# i. Konfigurera GitHub Pages
För att GitHub Actions ska kunna deploya till GitHub Pages behöver du:

1. ** Aktivera GitHub Pages: **
- Gå till ditt repository på GitHub.
- Navigera till `Settings` > `Pages`.
- Under "Source", välj `gh-pages` branch eller den branch som workflowen deployar till.
- Spara inställningarna.

2. ** Lägg till `gh-pages` som Dev Dependency: **
Detta har redan lagts till i `package.json`. Om du behöver justera versioner kan du göra det här.

# j. Push Till GitHub för Deployment
När du pushar dina ändringar till GitHub, kommer GitHub Actions att bygga och deploya din webbplats automatiskt:
git push origin main

**Observera: ** Första gången du pushar kan det ta några minuter innan GitHub Actions körs och din webbplats blir tillgänglig på `https: // <username > .github.io/<repository-name >`.

# 5. Verifiera Deployment
Efter några minuter, besök din GitHub Pages URL för att se den deployade webbplatsen.

# Ytterligare Anpassningar

# Lägga till Nya Slides

1. ** Skapa en Ny Slide-Komponent: **
Skapa en ny fil i `src/slides /`, till exempel `NySlide.js`:

   ```jsx
   import React from 'react'
   import {useSpring
           import animated} from '@react-spring/web'
   import './Slide.css'

   const NySlide = () = > {
       const props = useSpring({
           opacity: 1,
           transform: 'scale(1)',
           from: {opacity: 0, transform: 'scale(0.8)'},
           config: {duration: 1000},
       })

       return (
           < animated.div style={props} className="slide" >
           < h1 > Ny Slide < /h1 >
           < p > Innehåll för den nya sliden. < /p >
           < / animated.div >
       )
   }

   export default NySlide
# 2. Importera och Inkludera i App.js: Lägg till den nya sliden i App.js med en ny Parallax.Layer:

// Inom Parallax-komponenten
<Parallax.Layer offset = {10} speed = {0.5} >
<NySlide / >
</Parallax.Layer >
# 3. Uppdatera Parallax pages Prop: Öka antalet sidor i Parallax komponenten för att inkludera den nya sliden:
<Parallax pages = {11} >
# Uppdatera package.json för GitHub Pages
#Se till att homepage i package.json är korrekt inställd:
#"homepage": "https://<username>.github.io/<repository-name>",
