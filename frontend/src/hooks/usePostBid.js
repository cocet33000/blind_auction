import axios from 'axios';
import { Store } from 'react-notifications-component';

export default function usePostBid(username, item_id, price) {
	const data = {
		user_name: username,
		item_id: item_id,
		price: Number(price)
	};
	console.log(data);
	axios
		.post('https://api.blind-auction.com/dev/bids', data)
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

	return;
}
