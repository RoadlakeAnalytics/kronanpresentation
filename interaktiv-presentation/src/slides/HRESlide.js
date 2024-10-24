import React from 'react';
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
