import './App.css';
import React from 'react';
import AppBar from './components/Sidebar';
import ToggleColorMode from './components/ToggleColorMode';
import Card from './components/Card';

function App() {
  return (
    <div className='App'>
      <AppBar />
      {/*<ToggleColorMode />*/}
      <Card />
    </div>
  );
}

export default App;
