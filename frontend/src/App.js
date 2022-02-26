import "./App.css";
import A from "./A";
import B from "./B";
import ResponsiveAppBar from "./component/ResponsiveAppBar.js";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";

function App() {
  return (
    <div>
      <Router>
        <ResponsiveAppBar />
        <Routes>
          <Route path="/a" element={<A />} />
          <Route path="/b" element={<B />} />
        </Routes>
      </Router>
    </div>
  );
}

export default App;
