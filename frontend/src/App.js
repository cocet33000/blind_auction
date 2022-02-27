import "./css/App.css";
import A from "./A";
import B from "./B";
import Home from "./Home";
import ResponsiveAppBar from "./components/ResponsiveAppBar.js";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import {Container} from '@mui/material'
import { ThemeProvider } from "@mui/material/styles";
import theme from "./theme/theme"

function App() {
  return (
    <div>
      <Router>
      <ThemeProvider theme={theme}>
        <ResponsiveAppBar />
          <Container maxWidth="md">
            <Routes>
              <Route path="/a" element={<A />} />
              <Route path="/b" element={<B />} />
              <Route path="/" element={<Home />} />
            </Routes>
          </Container>
      </ThemeProvider>
      </Router>
    </div>
  );
}

export default App;
