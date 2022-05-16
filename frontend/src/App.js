import "./App.css";
import A from "./A";
import B from "./B";

import Home from "./Home";
import AppBar from "./AppBar.js";
import CognitoAuthenticator from "./components/CognitoAuthenticator.js";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import { Container } from "@mui/material";

function App() {
  return (
    <div>
      <Router>
        <AppBar />
        <Container maxWidth="md">
          <Routes>
            <Route path="/a" element={<A />} />
            <Route path="/b" element={<B />} />
            <Route path="/auth" element={<CognitoAuthenticator />} />
            <Route path="/" element={<Home />} />
          </Routes>
        </Container>
      </Router>
    </div>
  );
}

export default App;
