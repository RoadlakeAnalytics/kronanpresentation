#import NySlide from './slides/NySlide'
import os

# Definiera projektets filstruktur och innehåll med platshållare
files = {
    "public/index.html": """<!DOCTYPE html>
<html lang="sv">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Interaktiv Presentation</title>
  </head>
  <body>
    <div id="root"></div>
  </body>
</html>
""",
    "src/index.js": """import React from 'react';
import ReactDOM from 'react-dom';
import App from './App';
import './styles/App.css';

ReactDOM.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>,
  document.getElementById('root')
);
""",
    "src/App.js": """import React, { Suspense, lazy } from 'react';
import { Parallax } from '@react-spring/parallax';
import './styles/App.css';

const WelcomeSlide = lazy(() => import('./slides/WelcomeSlide'));
const EkonomiSlide = lazy(() => import('./slides/EkonomiSlide'));
const HRESlide = lazy(() => import('./slides/HRESlide'));
const TeknikSlide = lazy(() => import('./slides/TeknikSlide'));
const Topics = lazy(() => import('./components/Topics'));

# Ekonomi Slides
const EkonomiSlide1 = lazy(() => import('./slides/EkonomiSlide1'));
const EkonomiSlide2 = lazy(() => import('./slides/EkonomiSlide2'));

# HR Slides
const HRESlide1 = lazy(() => import('./slides/HRESlide1'));
const HRESlide2 = lazy(() => import('./slides/HRESlide2'));

# Teknik Slides
const TeknikSlide1 = lazy(() => import('./slides/TeknikSlide1'));

function App() {
  return (
    <div className="App">
      <Parallax pages={10}>
        <Suspense fallback={<div>Loading...</div>}>
          {/* Grundslides */}
          <Parallax.Layer offset={0} speed={0.5}>
            <WelcomeSlide />
          </Parallax.Layer>

          <Parallax.Layer offset={1} speed={0.5}>
            <EkonomiSlide />
          </Parallax.Layer>

          <Parallax.Layer offset={2} speed={0.5}>
            <HRESlide />
          </Parallax.Layer>

          <Parallax.Layer offset={3} speed={0.5}>
            <TeknikSlide />
          </Parallax.Layer>

          <Parallax.Layer offset={4} speed={0.5}>
            <Topics />
          </Parallax.Layer>

          {/* Ekonomi Slides */}
          <Parallax.Layer offset={5} speed={0.5}>
            <EkonomiSlide1 />
          </Parallax.Layer>
          <Parallax.Layer offset={6} speed={0.5}>
            <EkonomiSlide2 />
          </Parallax.Layer>

          {/* HR Slides */}
          <Parallax.Layer offset={7} speed={0.5}>
            <HRESlide1 />
          </Parallax.Layer>
          <Parallax.Layer offset={8} speed={0.5}>
            <HRESlide2 />
          </Parallax.Layer>

          {/* Teknik Slides */}
          <Parallax.Layer offset={9} speed={0.5}>
            <TeknikSlide1 />
          </Parallax.Layer>
        </Suspense>
      </Parallax>
    </div>
  );
}

export default App;
""",
    "src/components/Topics.js": """import React from 'react';
import { useParallax } from '@react-spring/parallax';
import './Topics.css';

const Topics = () => {
  const parallax = useParallax();

  const navigateTo = (page) => {
    parallax.scrollTo(page);
  };

  return (
    <div className="topics">
      <h2>Välj ett Ämne</h2>
      <div className="buttons">
        <button onClick={() => navigateTo(5)}>Ekonomi</button>
        <button onClick={() => navigateTo(7)}>HR</button>
        <button onClick={() => navigateTo(9)}>Teknik</button>
      </div>
    </div>
  );
};

export default Topics;
""",
    "src/components/Topics.css": """/* src/components/Topics.css */
.topics {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  height: 100vh;
}

.buttons {
  display: flex;
  gap: 20px;
  margin-top: 20px;
}

button {
  padding: 10px 20px;
  font-size: 16px;
  cursor: pointer;
}
""",
    "src/slides/WelcomeSlide.js": """import React from 'react';
import './Slide.css';

const WelcomeSlide = () => {
  return (
    <div className="slide">
      <h1>Välkommen till Vår Presentation</h1>
      <p>Utforska våra ämnen genom att scrolla eller klicka.</p>
    </div>
  );
};

export default WelcomeSlide;
""",
    "src/slides/EkonomiSlide.js": """import React from 'react';
import { useSpring, animated } from '@react-spring/web';
import './Slide.css';

const EkonomiSlide = () => {
  const props = useSpring({
    opacity: 1,
    transform: 'scale(1)',
    from: { opacity: 0, transform: 'scale(0.8)' },
    config: { duration: 1000 },
  });

  return (
    <animated.div style={props} className="slide">
      <h1>Ekonomi</h1>
      <p>Här är några ekonomiska insikter...</p>
    </animated.div>
  );
};

export default EkonomiSlide;
""",
    "src/slides/EkonomiSlide1.js": """import React from 'react';
import { useSpring, animated } from '@react-spring/web';
import './Slide.css';

const EkonomiSlide1 = () => {
  const props = useSpring({
    opacity: 1,
    transform: 'scale(1)',
    from: { opacity: 0, transform: 'scale(0.8)' },
    config: { duration: 1000 },
  });

  return (
    <animated.div style={props} className="slide">
      <h1>Ekonomi Slide 1</h1>
      <p>Innehåll för Ekonomi Slide 1.</p>
    </animated.div>
  );
};

export default EkonomiSlide1;
""",
    "src/slides/EkonomiSlide2.js": """import React from 'react';
import { useSpring, animated } from '@react-spring/web';
import './Slide.css';

const EkonomiSlide2 = () => {
  const props = useSpring({
    opacity: 1,
    transform: 'scale(1)',
    from: { opacity: 0, transform: 'scale(0.8)' },
    config: { duration: 1000 },
  });

  return (
    <animated.div style={props} className="slide">
      <h1>Ekonomi Slide 2</h1>
      <p>Innehåll för Ekonomi Slide 2.</p>
    </animated.div>
  );
};

export default EkonomiSlide2;
""",
    "src/slides/HRESlide.js": """import React from 'react';
import { useSpring, animated } from '@react-spring/web';
import './Slide.css';

const HRESlide = () => {
  const props = useSpring({
    opacity: 1,
    transform: 'scale(1)',
    from: { opacity: 0, transform: 'scale(0.8)' },
    config: { duration: 1000 },
  });

  return (
    <animated.div style={props} className="slide">
      <h1>HR</h1>
      <p>Här är några HR-relaterade insikter...</p>
    </animated.div>
  );
};

export default HRESlide;
""",
    "src/slides/HRESlide1.js": """import React from 'react';
import { useSpring, animated } from '@react-spring/web';
import './Slide.css';

const HRESlide1 = () => {
  const props = useSpring({
    opacity: 1,
    transform: 'scale(1)',
    from: { opacity: 0, transform: 'scale(0.8)' },
    config: { duration: 1000 },
  });

  return (
    <animated.div style={props} className="slide">
      <h1>HR Slide 1</h1>
      <p>Innehåll för HR Slide 1.</p>
    </animated.div>
  );
};

export default HRESlide1;
""",
    "src/slides/HRESlide2.js": """import React from 'react';
import { useSpring, animated } from '@react-spring/web';
import './Slide.css';

const HRESlide2 = () => {
  const props = useSpring({
    opacity: 1,
    transform: 'scale(1)',
    from: { opacity: 0, transform: 'scale(0.8)' },
    config: { duration: 1000 },
  });

  return (
    <animated.div style={props} className="slide">
      <h1>HR Slide 2</h1>
      <p>Innehåll för HR Slide 2.</p>
    </animated.div>
  );
};

export default HRESlide2;
""",
    "src/slides/TeknikSlide.js": """import React from 'react';
import { useSpring, animated } from '@react-spring/web';
import './Slide.css';

const TeknikSlide = () => {
  const props = useSpring({
    opacity: 1,
    transform: 'scale(1)',
    from: { opacity: 0, transform: 'scale(0.8)' },
    config: { duration: 1000 },
  });

  return (
    <animated.div style={props} className="slide">
      <h1>Teknik</h1>
      <p>Här är några tekniska insikter...</p>
    </animated.div>
  );
};

export default TeknikSlide;
""",
    "src/slides/TeknikSlide1.js": """import React from 'react';
import { useSpring, animated } from '@react-spring/web';
import './Slide.css';

const TeknikSlide1 = () => {
  const props = useSpring({
    opacity: 1,
    transform: 'scale(1)',
    from: { opacity: 0, transform: 'scale(0.8)' },
    config: { duration: 1000 },
  });

  return (
    <animated.div style={props} className="slide">
      <h1>Teknik Slide 1</h1>
      <p>Innehåll för Teknik Slide 1.</p>
    </animated.div>
  );
};

export default TeknikSlide1;
""",
    "src/slides/Slide.css": """/* src/slides/Slide.css */
.slide {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  height: 100vh;
  padding: 20px;
  background-color: #f5f5f5;
  text-align: center;
}

@media (max-width: 768px) {
  .slide h1 {
    font-size: 24px;
  }

  .slide p {
    font-size: 16px;
  }
}
""",
    "src/styles/App.css": """/* src/styles/App.css */
.App {
  font-family: Arial, sans-serif;
  height: 100vh;
  overflow: hidden;
}
""",
    ".gitignore": """node_modules
build
.DS_Store
.env
""",
    "package.json": """{
  "name": "interaktiv-presentation",
  "version": "1.0.0",
  "private": true,
  "homepage": "https://<username>.github.io/<repository-name>",
  "dependencies": {
    "@react-spring/parallax": "^9.4.5",
    "react": "^18.2.0",
    "react-dom": "^18.2.0",
    "react-scripts": "5.0.1"
  },
  "scripts": {
    "start": "react-scripts start",
    "build": "react-scripts build",
    "predeploy": "npm run build",
    "deploy": "gh-pages -d build"
  },
  "devDependencies": {
    "gh-pages": "^4.0.0"
  }
}
""",
    "README.md": """# Interaktiv Presentation

## Projektbeskrivning
En interaktiv webbplats byggd med React och React Spring för att presentera ett animerat flöde med zoom- och pan-effekter.

## Installation

1. Klona repositoryt:

   git clone https://github.com/<username>/<repository-name>.git
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
-   GitHub Actions """,
    ".github/workflows/deploy.yml": """name: Deploy to GitHub Pages

on: push: branches: - master # eller main, beroende på din branch

jobs: build-deploy: runs-on: ubuntu-latest

steps:
  - name: Checkout Repository
    uses: actions/checkout@v3

  - name: Setup Node.js
    uses: actions/setup-node@v3
    with:
      node-version: '16'

  - name: Install Dependencies
    run: npm install

  - name: Build Project
    run: npm run build

  - name: Deploy to GitHub Pages
    uses: peaceiris/actions-gh-pages@v3
    with:
      github_token: ${{ secrets.GITHUB_TOKEN }}
      publish_dir: ./build
""", }


# Funktion för att skapa filer och mappar med dynamisk ersättning
def create_files(base_path, files_dict, username, repo_name):
    for path, content in files_dict.items():
        # Ersätt platshållare i innehåll
        content = content.replace("<username>", username).replace("<repository-name>", repo_name)
        full_path = os.path.join(base_path, path)
        dir_name = os.path.dirname(full_path)
        if not os.path.exists(dir_name):
            os.makedirs(dir_name)
            print(f"Skapade mapp: {dir_name}")
        with open(full_path, 'w', encoding='utf-8') as f:
            f.write(content)
            print(f"Skapade fil: {full_path}")

def main():
    project_name = "interaktiv-presentation"
    base_path = os.path.join(os.getcwd(), project_name)

    if os.path.exists(base_path):
        print(f"Projektmappen '{project_name}' finns redan. Avslutar för att undvika överskrivning.")
        return

    # Be användaren om GitHub-användarnamn och repository-namn
    username = input("Ange ditt GitHub-användarnamn: ").strip()
    repo_name = input("Ange ditt GitHub repository-namn: ").strip()

    os.makedirs(base_path)
    print(f"Skapade projektmapp: {base_path}")

    create_files(base_path, files, username, repo_name)

    print("\nProjektet har skapats framgångsrikt!")
    print("Följ instruktionerna nedan för att slutföra installationen och distributionen.")

if __name__ == "__main__":
    main()