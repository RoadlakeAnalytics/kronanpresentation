import React, { Suspense, lazy, useRef } from "react";
import { Parallax, ParallaxLayer } from "@react-spring/parallax";
import "./styles/App.css";

const WelcomeSlide = lazy(() => import("./slides/WelcomeSlide"));
const EkonomiSlide = lazy(() => import("./slides/EkonomiSlide"));
const HRESlide = lazy(() => import("./slides/HRESlide"));
const TeknikSlide = lazy(() => import("./slides/TeknikSlide"));
const Topics = lazy(() => import("./components/Topics"));

// Ekonomi Slides
const EkonomiSlide1 = lazy(() => import("./slides/EkonomiSlide1"));
const EkonomiSlide2 = lazy(() => import("./slides/EkonomiSlide2"));

// HR Slides
const HRESlide1 = lazy(() => import("./slides/HRESlide1"));
const HRESlide2 = lazy(() => import("./slides/HRESlide2"));

// Teknik Slides
const TeknikSlide1 = lazy(() => import("./slides/TeknikSlide1"));

function App() {
	const parallaxRef = useRef();

	const handleNextView = () => {
		if (parallaxRef.current) {
			parallaxRef.current.scrollTo(parallaxRef.current.current + 1);
		}
	};

	const handlePrevView = () => {
		if (parallaxRef.current) {
			parallaxRef.current.scrollTo(parallaxRef.current.current - 1);
		}
	};

	return (
		<div className="App" onClick={handleNextView}>
			<Parallax
				pages={10}
				ref={parallaxRef}
			>
				<Suspense fallback={<div>Loading...</div>}>
					{/* Grundslides */}
					<ParallaxLayer
						offset={0}
						speed={0.5}
					>
						<WelcomeSlide />
					</ParallaxLayer>

					<ParallaxLayer
						offset={1}
						speed={0.5}
					>
						<EkonomiSlide />
					</ParallaxLayer>

					<ParallaxLayer
						offset={2}
						speed={0.5}
					>
						<HRESlide />
					</ParallaxLayer>

					<ParallaxLayer
						offset={3}
						speed={0.5}
					>
						<TeknikSlide />
					</ParallaxLayer>

					<ParallaxLayer
						offset={4}
						speed={0.5}
					>
						<Topics parallaxRef={parallaxRef} />
					</ParallaxLayer>

					{/* Ekonomi Slides */}
					<ParallaxLayer
						offset={5}
						speed={0.5}
					>
						<EkonomiSlide1 />
					</ParallaxLayer>
					<ParallaxLayer
						offset={6}
						speed={0.5}
					>
						<EkonomiSlide2 />
					</ParallaxLayer>

					{/* HR Slides */}
					<ParallaxLayer
						offset={7}
						speed={0.5}
					>
						<HRESlide1 />
					</ParallaxLayer>
					<ParallaxLayer
						offset={8}
						speed={0.5}
					>
						<HRESlide2 />
					</ParallaxLayer>

					{/* Teknik Slides */}
					<ParallaxLayer
						offset={9}
						speed={0.5}
					>
						<TeknikSlide1 />
					</ParallaxLayer>
				</Suspense>
			</Parallax>

			<div className="arrow arrow-left" onClick={handlePrevView}></div>
			<div className="arrow arrow-right" onClick={handleNextView}></div>
			<div className="hamburger-menu">
				<div></div>
				<div></div>
				<div></div>
			</div>
		</div>
	);
}

export default App;
