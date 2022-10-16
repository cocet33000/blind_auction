import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import reportWebVitals from './reportWebVitals';
import { Authenticator } from '@aws-amplify/ui-react';
import Home from './pages/Home.js';
import AppBar from './components/AppBar.js';
import Login from './pages/Login.js';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Box from '@mui/material/Box';
import { ThemeProvider, createTheme } from '@mui/material/styles';
import { ReactNotifications } from 'react-notifications-component';
import 'react-notifications-component/dist/theme.css';
import BidHistory from './pages/BidHistory';

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

ReactDOM.render(
	<React.StrictMode>
		<Authenticator.Provider>
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
						<Route path="/auth" element={<Login />} />
						<Route path="/history" element={<BidHistory />} />
						<Route path="/" element={<Home />} />
					</Routes>
				</Router>
			</ThemeProvider>
		</Authenticator.Provider>
	</React.StrictMode>,
	document.getElementById('root')
);

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
reportWebVitals();
