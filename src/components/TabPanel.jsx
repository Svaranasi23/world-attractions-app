import React from 'react'
import StatisticsPanel from './StatisticsPanel'
import FilterPanel from './FilterPanel'
import './TabPanel.css'

function TabPanel({ activeTab, setActiveTab, parks, regions, visibleRegions, toggleRegion, toggleAllUSRegions, areAllUSRegionsVisible, toggleAllIndiaRegions, areAllIndiaRegionsVisible, toggleAllNepalRegions, areAllNepalRegionsVisible, toggleAllSriLankaRegions, areAllSriLankaRegionsVisible, showAirports, setShowAirports }) {
  return (
    <div className="tabbed-panel">
      <div className="tab-headers">
        <button
          className={`tab-button ${activeTab === 'filters' ? 'active' : ''}`}
          onClick={() => setActiveTab('filters')}
        >
          🔍 Filters
        </button>
        <button
          className={`tab-button ${activeTab === 'stats' ? 'active' : ''}`}
          onClick={() => setActiveTab('stats')}
        >
          📊 Statistics
        </button>
      </div>

      <div className="tab-content">
        {activeTab === 'stats' && (
          <StatisticsPanel
            parks={parks}
            regions={regions}
            activeTab={activeTab}
            setActiveTab={setActiveTab}
          />
        )}
        {activeTab === 'filters' && (
          <FilterPanel
            regions={regions}
            visibleRegions={visibleRegions}
            toggleRegion={toggleRegion}
            toggleAllUSRegions={toggleAllUSRegions}
            areAllUSRegionsVisible={areAllUSRegionsVisible}
            activeTab={activeTab}
            setActiveTab={setActiveTab}
            showAirports={showAirports}
            setShowAirports={setShowAirports}
            toggleAllIndiaRegions={toggleAllIndiaRegions}
            areAllIndiaRegionsVisible={areAllIndiaRegionsVisible}
            toggleAllNepalRegions={toggleAllNepalRegions}
            areAllNepalRegionsVisible={areAllNepalRegionsVisible}
            toggleAllSriLankaRegions={toggleAllSriLankaRegions}
            areAllSriLankaRegionsVisible={areAllSriLankaRegionsVisible}
          />
        )}
      </div>
    </div>
  )
}

export default TabPanel

