import "./App.css";
import A from "./A";
import B from "./B";
import Home from "./Home";
import ResponsiveAppBar from "./components/ResponsiveAppBar.js";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import {Container} from '@mui/material'

function App() {
  return (
    <div>
      <Router>
        <ResponsiveAppBar />
        <Container maxWidth="md">
          <Routes>
            <Route path="/a" element={<A />} />
            <Route path="/b" element={<B />} />
            <Route path="/" element={<Home />} />
          </Routes>
        </Container>
      </Router>
    </div>
  );
}

export default App;
