import React from 'react'
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom'
import MapView from './pages/MapView'
import './App.css'

function App() {
  return (
    <Router
      future={{
        v7_startTransition: true,
        v7_relativeSplatPath: true
      }}
    >
      <div className="App">
        <Routes>
          <Route path="/" element={<MapView />} />
        </Routes>
      </div>
    </Router>
  )
}

export default App

