import './App.css';

import Home from './Home.js';
import AppBar from './components/AppBar.js';
import CognitoAuthenticator from './components/CognitoAuthenticator.js';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
// import { styled } from '@mui/system';
import Box from '@mui/material/Box';
// import { Container } from '@mui/material';
import { ThemeProvider, createTheme } from '@mui/material/styles';

function App() {
	// const StyledBox = styled(Box)(({ theme }) => ({
	// 	...theme.mixins.toolbar,
	// 	border: '1px solid'
	// }));

	const theme = createTheme();
	return (
		<ThemeProvider theme={theme}>
			<Router>
				<AppBar />
				{/* appbarと重なる為、余白用のBoxをおく */}
				<Box
					sx={{
						width: 300,
						height: theme.mixins.toolbar
					}}
				/>
				<Routes>
					<Route path="/auth" element={<CognitoAuthenticator />} />
					<Route path="/" element={<Home />} />
				</Routes>
			</Router>
		</ThemeProvider>
	);
}

export default App;
