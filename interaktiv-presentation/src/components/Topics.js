import React from "react";
import "./Topics.css";

const Topics = ({ parallaxRef }) => {
	const navigateTo = (page) => {
		if (parallaxRef.current) {
			parallaxRef.current.scrollTo(page);
		}
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

