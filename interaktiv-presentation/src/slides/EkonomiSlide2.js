import React from 'react';
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
