import React, { useState, useEffect, useRef } from 'react'
import './AttractionSearch.css'

function AttractionSearch({ parks, onSearch, onSelectAttraction }) {
  const [searchQuery, setSearchQuery] = useState('')
  const [isOpen, setIsOpen] = useState(false)
  const [filteredResults, setFilteredResults] = useState([])
  const searchRef = useRef(null)
  const inputRef = useRef(null)

  useEffect(() => {
    if (searchQuery.trim() === '') {
      setFilteredResults([])
      onSearch('')
      return
    }

    const query = searchQuery.toLowerCase().trim()
    const results = parks
      .filter(park => {
        const name = (park.Name || '').toLowerCase()
        const description = (park.Description || '').toLowerCase()
        const country = (park.Country || '').toLowerCase()
        const states = (park.States || '').toLowerCase()
        
        return name.includes(query) || 
               description.includes(query) || 
               country.includes(query) ||
               states.includes(query)
      })
      .slice(0, 10) // Limit to top 10 results
    
    setFilteredResults(results)
    onSearch(searchQuery)
  }, [searchQuery, parks, onSearch])

  const handleSelect = (park) => {
    setSearchQuery(park.Name || '')
    setIsOpen(false)
    onSelectAttraction(park)
  }

  const handleClear = () => {
    setSearchQuery('')
    setFilteredResults([])
    setIsOpen(false)
    onSearch('')
  }

  // Close dropdown when clicking outside
  useEffect(() => {
    const handleClickOutside = (event) => {
      if (searchRef.current && !searchRef.current.contains(event.target)) {
        setIsOpen(false)
      }
    }

    if (isOpen) {
      document.addEventListener('mousedown', handleClickOutside)
      return () => {
        document.removeEventListener('mousedown', handleClickOutside)
      }
    }
  }, [isOpen])

  return (
    <div className="attraction-search-container" ref={searchRef}>
      <div className="attraction-search-input-wrapper">
        <span className="search-icon">🔍</span>
        <input
          ref={inputRef}
          type="text"
          className="attraction-search-input"
          placeholder="Search attractions..."
          value={searchQuery}
          autoComplete="off"
          data-lpignore="true"
          data-form-type="other"
          onChange={(e) => {
            setSearchQuery(e.target.value)
            setIsOpen(true)
          }}
          onFocus={() => setIsOpen(true)}
        />
        {searchQuery && (
          <button
            className="search-clear-button"
            onClick={handleClear}
            aria-label="Clear search"
          >
            ×
          </button>
        )}
      </div>
      
      {isOpen && filteredResults.length > 0 && (
        <div className="attraction-search-results">
          {filteredResults.map((park, index) => (
            <button
              key={park.id || index}
              className="search-result-item"
              onClick={() => handleSelect(park)}
            >
              <div className="search-result-name">{park.Name}</div>
              <div className="search-result-info">
                {park.Country}
                {park.States && ` • ${park.States}`}
              </div>
            </button>
          ))}
        </div>
      )}
      
      {isOpen && searchQuery && filteredResults.length === 0 && (
        <div className="attraction-search-results">
          <div className="search-no-results">No attractions found</div>
        </div>
      )}
    </div>
  )
}

export default AttractionSearch

