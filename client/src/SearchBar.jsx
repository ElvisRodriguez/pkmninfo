import { useState } from 'react';

const SearchBar = ({ onSearch }) => {
  const [inputText, setInputText] = useState("");

  const inputHandler = (e) => {
    // Convert input to lower case for case-insensitive searching
    const lowerCaseInput = e.target.value.toLowerCase();
    setInputText(lowerCaseInput);
    // Pass the input to a parent component for filtering
    onSearch(lowerCaseInput); 
  };

  return (
    <div className="search">
      <input
        type="text"
        placeholder="Search Pokemon"
        onChange={inputHandler}
        value={inputText}
        style={{ padding: '10px', width: '300px', fontSize: '16px' }}
      />
    </div>
  );
};

export default SearchBar;