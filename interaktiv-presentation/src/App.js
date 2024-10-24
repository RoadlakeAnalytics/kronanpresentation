import React, { Suspense, lazy } from 'react';
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
