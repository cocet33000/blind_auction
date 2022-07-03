import * as React from 'react';
import Box from '@mui/material/Box';
import Drawer from '@mui/material/Drawer';
import Button from '@mui/material/Button';
import Divider from '@mui/material/Divider';
import IconButton from '@mui/material/IconButton';
import MenuIcon from '@mui/icons-material/Menu';
import Typography from '@mui/material/Typography';
import Stack from '@mui/material/Stack';
import { useNavigate } from 'react-router-dom';
import { makeStyles } from '@mui/styles';
import { PropTypes } from 'prop-types';

import { useAuthenticator } from '@aws-amplify/ui-react';

const useStyles = makeStyles({
	list: {
		width: 250
	},
	fullList: {
		width: 'auto'
	},
	paper: {
		background: 'white'
	}
});

export default function MenuButton(props) {
	let navigate = useNavigate();
	const [isOpen, setOpen] = React.useState(false);
	const { authStatus } = useAuthenticator((context) => [context.authStatus]);
	// eslint-disable-next-line no-unused-vars
	const { user, signOut } = useAuthenticator((context) => [context.user]);

	const classes = useStyles();
	const toggleDrawer = (open) => (event) => {
		if (
			event.type === 'keydown' &&
			(event.key === 'Tab' || event.key === 'Shift')
		) {
			return;
		}

		setOpen(open);
	};
	const handleSignIn = () => {
		navigate('/auth');
	};
	const handleSignUp = () => {
		navigate('/auth');
	};
	const unAuthenticatedList = [
		{ name: 'Sign in', onClick: handleSignIn, variant: 'text' },
		{ name: 'Sign up', onClick: handleSignUp, variant: 'contained' }
	];

	const authenticatedList = [
		{ name: 'profile', onClick: handleSignIn },
		{ name: 'Biding Item', onClick: handleSignIn },
		{ name: 'sign out', onClick: signOut }
	];

	const list = (anchor) => (
		<Box
			sx={{ width: anchor === 'top' || anchor === 'bottom' ? 'auto' : 250 }}
			role="presentation"
			onClick={toggleDrawer(false)}
			onKeyDown={toggleDrawer(false)}
		>
			<Box
				sx={{
					display: 'flex',
					justifyContent: 'center',
					p: 1,
					m: 1
				}}
			>
				<Typography
					variant="h6"
					noWrap
					component="div"
					sx={{ mr: 2, color: 'black' }}
				>
					Menu
				</Typography>
			</Box>
			<Divider variant="middle" sx={{ bgcolor: 'gray' }} />
			<Box
				sx={{
					height: 30,
					backgroundColor: 'transparent'
				}}
			/>
			<Box
				sx={{
					display: 'flex',
					justifyContent: 'center',
					p: 1,
					m: 1
				}}
			>
				<Stack direction="column" spacing={2}>
					{(authStatus !== 'authenticated'
						? unAuthenticatedList
						: authenticatedList
					).map(({ item }) => {
						return (
							<Button
								key={item.id}
								variant={item.variant}
								size="large"
								onClick={item.onClick}
							>
								{item.name}
							</Button>
						);
					})}
				</Stack>
			</Box>
		</Box>
	);

	return (
		<div>
			<IconButton
				size="large"
				aria-label="account of current user"
				aria-controls="menu-appbar"
				aria-haspopup="true"
				onClick={toggleDrawer(true)}
				color="inherit"
			>
				<MenuIcon />
			</IconButton>
			<Drawer
				classes={{ paper: classes.paper }}
				anchor={'right'}
				open={isOpen}
				onClose={toggleDrawer(false)}
			>
				{list(props.anchor)}
			</Drawer>
		</div>
	);
}

MenuButton.propTypes = {
	anchor: PropTypes.oneOf(['top', 'left', 'bottom', 'right']).isRequired
};
