import React from 'react'
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom'
import MapView from './pages/MapView'
import './App.css'

function App() {
  return (
    <Router>
      <div className="App">
        <Routes>
          <Route path="/" element={<MapView />} />
        </Routes>
      </div>
    </Router>
  )
}

export default App

