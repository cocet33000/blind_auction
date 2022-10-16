import { useState, useEffect } from 'react';
import axios from 'axios';

export default function useGetItems() {
	const [items, setItems] = useState([]);
	const [auction, setAuction] = useState('');
	const updateItemBidnum = (item_id, bid_num) => {
		setItems((items) => {
			const updateditems = items.map((item) => {
				if (item.id === item_id) {
					var new_item = item;
					new_item.bid_num = bid_num;
					return new_item;
				} else {
					return item;
				}
			});
			return updateditems;
		});
	};
	useEffect(() => {
		axios
			.get('https://api.blind-auction.com/dev/home')
			.then((response) => {
				setItems(response.data.items.items);
				setAuction(response.data.auction);
			})
			.catch((error) => {
				console.log('ERROR!! occurred in Backend.', error);
			});
		const socket = new WebSocket('wss://wss.blind-auction.com/deb');
		socket.onmessage = (event) => {
			const data = JSON.parse(event.data);
			updateItemBidnum(data.item_id, data.bid_num);
		};
		return () => {
			//画面が閉じられたらコネクションも閉じる
			socket.close();
		};
	}, []);
	return { items, auction };
}
