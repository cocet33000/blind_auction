import * as React from 'react';
import Button from '@mui/material/Button';
import DialogTitle from '@mui/material/DialogTitle';
import Dialog from '@mui/material/Dialog';
import DialogContent from '@mui/material/DialogContent';
import DialogContentText from '@mui/material/DialogContentText';
import { InputAdornment } from '@mui/material';
import { Input } from '@mui/material';
import { Stack, Box } from '@mui/material';
import { useAuthenticator } from '@aws-amplify/ui-react';
import axios from 'axios';
import { PropTypes } from 'prop-types';

export default function ItemDetailDialog(props) {
	const [price, setPrice] = React.useState('');
	const { authStatus } = useAuthenticator((context) => [context.authStatus]);
	const { user } = useAuthenticator((context) => [context.user]);

	const bid = () => {
		const data = {
			user_name: user.username,
			item_id: props.item.id,
			price: Number(price)
		};
		console.log(data);

		axios
			.post('https://api.blind-auction.com/dev/bids', data)
			.then((response) => {
				console.log(response.data);
			})
			.catch((error) => {
				console.log('ERROR!! occurred in Backend.', error);
			});

		props.handleClose();
	};

	return (
		<main>
			{props.item ? (
				<Dialog open={props.isOpen} onClose={props.handleClose}>
					<DialogTitle>{props.item.name}</DialogTitle>
					<DialogContent>
						<img
							style={{ maxWidth: '100%', maxHeight: 'calc(100vh - 64px)' }}
							src={props.item.image_src}
						/>
						<Box
							sx={{
								height: 150
							}}
						>
							<DialogContentText sx={{ fontSize: 24 }}>
								{props.item.description}
							</DialogContentText>
						</Box>
						<Stack
							direction="row"
							spacing={2}
							justifyContent="center"
							alignItems="center"
						>
							<Input
								placeholder={'初期価格：' + props.item.start_price}
								id="standard-adornment-amount"
								type="number"
								variant="standard"
								value={price}
								onChange={(event) => setPrice(event.target.value)}
								startAdornment={
									<InputAdornment position="start">¥</InputAdornment>
								}
							/>

							<Button
								variant="contained"
								onClick={bid}
								disabled={authStatus === 'authenticated' ? false : true}
							>
								{authStatus === 'authenticated' ? 'BID' : 'NEED SignIn'}
							</Button>
						</Stack>
					</DialogContent>
				</Dialog>
			) : (
				<main></main>
			)}
		</main>
	);
}

ItemDetailDialog.propTypes = {
	item: PropTypes.object.isRequired,
	isOpen: PropTypes.bool.isRequired,
	handleClose: PropTypes.func.isRequired
};
