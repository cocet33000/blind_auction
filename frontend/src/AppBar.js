import { useState, useEffect } from 'react';
import * as React from 'react';
import AppBar from '@mui/material/AppBar';
import Box from '@mui/material/Box';
import Toolbar from '@mui/material/Toolbar';
import Typography from '@mui/material/Typography';
import Container from '@mui/material/Container';
import { ThemeProvider, createTheme } from '@mui/material/styles';
import Snackbar from '@mui/material/Snackbar';
import MuiAlert from '@mui/material/Alert';
import { useNavigate } from 'react-router-dom';
import { useAuthenticator } from '@aws-amplify/ui-react';

import MenuButton from './components/MenuButton';
const Alert = React.forwardRef(function Alert(props, ref) {
	return <MuiAlert elevation={6} ref={ref} variant="filled" {...props} />;
});

const darkTheme = createTheme({
	palette: {
		mode: 'dark',
		primary: {
			main: '#000000'
		}
	}
});

const ResponsiveAppBar = () => {
	let navigate = useNavigate();
	const { authStatus } = useAuthenticator((context) => [context.authStatus]);
	const { user, signOut } = useAuthenticator((context) => [context.user]);
	const [isNotification, setNotification] = useState('');

	useEffect(() => {
		setNotification(true);
		console.log('auth status is changed!');
	}, [authStatus]);

	const handleClose = (event, reason) => {
		setNotification(false);
	};

	return (
		<ThemeProvider theme={darkTheme}>
			<AppBar position="static" color="primary" enableColorOnDark>
				<Container maxWidth="xl">
					<Toolbar disableGutters>
						<Typography
							onClick={() => {
								navigate('/');
							}}
							variant="h6"
							noWrap
							component="div"
							sx={{ mr: 2, display: { xs: 'none', md: 'flex' } }}
						>
							BLIND AUCTION
						</Typography>

						<Typography
							onClick={() => {
								navigate('/');
							}}
							variant="h6"
							noWrap
							component="div"
							sx={{ flexGrow: 1, display: { xs: 'flex', md: 'none' } }}
						>
							BLIND AUCTION
						</Typography>
						<Box sx={{ flexGrow: 1, display: { xs: 'none', md: 'flex' } }}>
							{/* パティングの為 */}
						</Box>

						<Box sx={{ flexGrow: 0 }}>
							<MenuButton anchor="right" />
							{/* <IconButton onClick={handleOpenUserMenu} sx={{ p: 0 }}>
                {authStatus !== "authenticated" ? (
                  <LoginIcon fontSize="large" />
                ) : (
                  <AccountCircleIcon fontSize="large" />
                )}
              </IconButton>
              <Menu
                sx={{ mt: "45px" }}
                id="menu-appbar"
                anchorEl={anchorElUser}
                anchorOrigin={{
                  vertical: "top",
                  horizontal: "right",
                }}
                keepMounted
                transformOrigin={{
                  vertical: "top",
                  horizontal: "right",
                }}
                open={Boolean(anchorElUser)}
                onClose={handleCloseUserMenu}
              >
                {(authStatus !== "authenticated"
                  ? notAuthenticatedMenu
                  : authenticatedMenu
                ).map((setting) => (
                  <MenuItem key={setting.text} onClick={handleCloseUserMenu}>
                    <Typography textAlign="center" onClick={setting.onClick}>
                      {setting.text}
                    </Typography>
                  </MenuItem>
                ))}
              </Menu> */}
						</Box>
					</Toolbar>
				</Container>
			</AppBar>
			<Snackbar
				open={isNotification && authStatus === 'authenticated'}
				autoHideDuration={6000}
				onClose={handleClose}
				anchorOrigin={{ vertical: 'top', horizontal: 'right' }}
			>
				<Alert onClose={handleClose} severity="success" sx={{ width: '100%' }}>
					{authStatus !== 'authenticated'
						? ''
						: 'You are signed in as ' + user.username}
				</Alert>
			</Snackbar>
		</ThemeProvider>
	);
};
export default ResponsiveAppBar;
