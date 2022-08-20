import { useState } from "react";
import LandingPage from "./Routes/LandingPage";
import { BrowserRouter } from "react-router-dom";

function App() {
  const [isLoggedIn, setIsLoggedIn] = useState(true)
  const [userType, setUserType] = useState("school")
  return (
    <div className="App">
      <BrowserRouter>
        <LandingPage userType={userType} isLoggedIn={isLoggedIn} />
      </BrowserRouter>
    </div>
  );
}

export default App;  
