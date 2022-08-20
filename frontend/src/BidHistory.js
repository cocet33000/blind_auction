import { useAuthenticator } from '@aws-amplify/ui-react';
import { useState, useEffect } from 'react';
import { Typography } from '@mui/material';
import axios from 'axios';
import Box from '@mui/material/Box';
import Grid from '@mui/material/Grid';
import BidHistoryCard from './components/BidHistoryCard';

const BidHistory = () => {
	const { user } = useAuthenticator((context) => [context.user]);
	const { authStatus } = useAuthenticator((context) => [context.authStatus]);
	const [bidHistorys, setBidHistorys] = useState([]);

	useEffect(() => {
		if (authStatus === 'authenticated') {
			axios
				.get('https://api.blind-auction.com/dev/bids', {
					params: {
						user_name: user.username
					}
				})
				.then((response) => {
					setBidHistorys(response.data.bid_historys);
					console.log(response.data);
				})
				.catch((error) => {
					console.log('ERROR!! occurred in Backend.', error);
				});
		}
		return () => {};
	}, [authStatus]);
	return (
		<div>
			<Box sx={{ p: 3 }}>
				<Typography>
					Hello {authStatus !== 'authenticated' ? '' : user.username}
				</Typography>
				<Typography>入札済みアイテム：{bidHistorys.length}</Typography>

				<Box sx={{ px: { xs: 0, md: 5, xl: 8 }, py: { xs: 4, md: 5, xl: 8 } }}>
					<Grid
						container
						columnSpacing={{ xs: 4, md: 8, xl: 12 }}
						rowSpacing={{ xs: 4, md: 8, xl: 12 }}
					>
						{bidHistorys.map((bidHistory) => {
							return (
								<Grid item xs={12} md={6} key={bidHistory.item.id}>
									<BidHistoryCard bidHistory={bidHistory} />
								</Grid>
							);
						})}
					</Grid>
				</Box>
			</Box>
		</div>
	);
};
export default BidHistory;
