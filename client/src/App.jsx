'use strict';
import { useEffect, useState } from 'react'
import './App.css'
import axios from 'axios'

import AudioPlayer from './AudioPlayer';
import ImageViewer from './ImageViewer';
import SearchBar from './SearchBar';


function App() {

  const [pokemonObject, setObject] = useState([]);

  const handleSearch = async (input) => {
    const response = await axios.post(
      "http://localhost:8080/api/pokemon", 
      {"pokemon_name": input}
    );
    setObject(response.data);
  }

  return (
    <>
      <SearchBar onSearch={handleSearch} />
      <div className="card">
          <p>#{pokemonObject.pokedex_number}: {pokemonObject.name}</p>
      </div>
      <div className="sprites">
        <ImageViewer url={pokemonObject.sprite_front_default}/>
        <ImageViewer url={pokemonObject.sprite_back_default}/>
        <ImageViewer url={pokemonObject.sprite_front_shiny}/>
        <ImageViewer url={pokemonObject.sprite_back_shiny}/>
      </div>
      <div className="audio">
        <p>Cry (Current):</p>
        <AudioPlayer url={pokemonObject.cry_latest}/>
      </div>
      <div className="audio">
        <p>Cry (Original):</p>
        <AudioPlayer url={pokemonObject.cry_legacy}/>
      </div>
    </>
  )
}

export default App
