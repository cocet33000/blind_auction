import "./App.css";

import Home from "./Home";
import ResponsiveAppBar from "./components/ResponsiveAppBar.js";
import CognitoAuthenticator from "./components/CognitoAuthenticator.js"
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import { Container } from '@mui/material'

function App() {
  return (
    <div>
      <Router>
        <ResponsiveAppBar />
        <Container maxWidth="md">
          <Routes>
            <Route path="/auth" element={<CognitoAuthenticator />} />
            <Route path="/" element={<Home />} />
          </Routes>
        </Container>
      </Router>
    </div>
  );
}

export default App;
