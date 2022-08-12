import './App.css';

import Home from './Home.js';
import AppBar from './components/AppBar.js';
import CognitoAuthenticator from './components/CognitoAuthenticator.js';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import { Container } from '@mui/material';

function App() {
	// const StyledBox = styled(Box)(({ theme }) => ({
	// 	...theme.mixins.toolbar,
	// 	border: '1px solid'
	// }));

	const theme = createTheme({
		palette: {
			primary: {
				main: '#26262d',
				secondary: '#26262d'
			},
			card: {
				background: '#f5f5f5'
			}
		}
	});
	return (
		<div>
			<Router>
				<AppBar />
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
