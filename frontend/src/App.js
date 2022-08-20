import './App.css';

import Home from './Home.js';
import AppBar from './components/AppBar.js';
import CognitoAuthenticator from './components/CognitoAuthenticator.js';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
// import { styled } from '@mui/system';
import Box from '@mui/material/Box';
import { ThemeProvider, createTheme } from '@mui/material/styles';
import { ReactNotifications } from 'react-notifications-component';
import 'react-notifications-component/dist/theme.css';
import BidHistory from './BidHistory';

function App() {
	// const StyledBox = styled(Box)(({ theme }) => ({
	// 	...theme.mixins.toolbar,
	// 	border: '1px solid'
	// }));

	const theme = createTheme({
		palette: {
			primary: {
				main: '#26262d'
			},
			authenticator: {
				background: {
					primary: '#f5f5f5',
					secondary: '#BFBBBA'
				},
				font: {
					interactive: '#000',
					focus: '#000',
					hover: '#000',
					active: '#000'
				},
				components: {
					button: {
						background: '#737272',
						hover: '#403F3F',
						focus: '#403F3F',
						active: '#403F3F'
					}
				}
			},
			card: {
				background: '#f5f5f5'
			}
		}
	});
	return (
		<ThemeProvider theme={theme}>
			<ReactNotifications />
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
					<Route path="/history" element={<BidHistory />} />
					<Route path="/" element={<Home />} />
				</Routes>
			</Router>
		</ThemeProvider>
	);
}

export default App;
