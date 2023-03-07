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
import { Store } from 'react-notifications-component';
//import usePostBid from '../hooks/usePostBid.js';
import { urlContext } from '../context/urlContext';
import { useContext } from 'react';
export default function ItemDetailDialog(props) {
	const [price, setPrice] = React.useState('');
	const { authStatus } = useAuthenticator((context) => [context.authStatus]);
	const { user } = useAuthenticator((context) => [context.user]);
	const url = useContext(urlContext);
	const bid = () => {
		//usePostBid(user.username, props.item.id, Number(price));
		const data = {
			user_name: user.username,
			item_id: props.item.id,
			price: Number(price)
		};
		console.log(data);

		axios
			.post(url + '/bids', data)
			.then((response) => {
				console.log(response.data);
				Store.addNotification({
					title: 'SUCCESS',
					message: 'Your bid has completed successfully',
					type: 'success',
					insert: 'top',
					container: 'top-right',
					dismiss: {
						duration: 3000
					}
				});
			})
			.catch((error) => {
				Store.addNotification({
					title: 'ERROR',
					message: 'ERROR occurred in Backend',
					type: 'danger',
					insert: 'top',
					container: 'top-right',
					dismiss: {
						duration: 3000
					}
				});
				console.log('ERROR!! occurred in Backend.', error);
			});

		props.handleClose();
	};

	return (
		<main>
			{props.item ? (
				<Dialog
					open={props.isOpen}
					onClose={props.handleClose}
					fullWidth={true}
					maxWidth={'lg'}
					scroll={'body'}
				>
					<DialogTitle sx={{ fontSize: { xs: 24, md: 36 } }}>
						{props.item.name}
					</DialogTitle>
					<DialogContent>
						<Box display="flex" alignItems="center" justifyContent="center">
							<img
								style={{ maxWidth: '100%', maxHeight: 'calc(100vh - 18px)' }}
								//style={{ maxWidth: '100%', maxHeight: '100%' }}
								src={props.item.image_src}
							/>
						</Box>
						<Box
							sx={{
								height: 150
							}}
						>
							<DialogContentText sx={{ fontSize: { xs: 24, md: 36, lg: 48 } }}>
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
								size="normal"
								id="standard-adornment-amount"
								type="number"
								variant="standard"
								value={price}
								onChange={(event) => setPrice(event.target.value)}
								startAdornment={
									<InputAdornment position="start">¥</InputAdornment>
								}
								sx={{
									fontSize: { fontSize: { xs: 24, md: 36, lg: 48 } }
								}}
							/>

							<Button
								variant="contained"
								onClick={bid}
								disabled={authStatus === 'authenticated' ? false : true}
							>
								BID
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
