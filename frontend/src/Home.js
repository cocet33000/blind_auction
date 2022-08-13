import ItemCard from './components/ItemCard.js';
import Box from '@mui/material/Box';
import Grid from '@mui/material/Grid';
//import Stack from '@mui/material/Stack';
//import Container from '@mui/material/Container';
//import { Button } from '@mui/material';
// import { styled } from '@mui/system';
import 'slick-carousel/slick/slick.css';
import 'slick-carousel/slick/slick-theme.css';
import './css/slider.css';
import './css/slider.css';
import { useState, useEffect } from 'react';
import axios from 'axios';
import CountdownTimer from './components/CountdownTimer';

const socket = new WebSocket('wss://wss.blind-auction.com/deb');

function Home() {
	const [items, setItems] = useState([]);
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
			.get('https://api.blind-auction.com/dev/items')
			.then((response) => {
				setItems(response.data.items);
				console.log(response.data);
			})
			.catch((error) => {
				console.log('ERROR!! occurred in Backend.', error);
			});
		socket.onmessage = (event) => {
			const data = JSON.parse(event.data);
			updateItemBidnum(data.item_id, data.bid_num);
		};
		return () => {
			//画面が閉じられたらコネクションも閉じる
			socket.close();
		};
	}, []);

	//unix時間でカウントダウンを設定
	const THREE_DAYS_IN_MS = 3 * 24 * 60 * 60 * 1000;
	const NOW_IN_MS = new Date().getTime();
	const dateTimeAfterThreeDays = NOW_IN_MS + THREE_DAYS_IN_MS;

	return (
		<div>
			<Box sx={{ p: 3 }}>
				<CountdownTimer targetDate={dateTimeAfterThreeDays} />
			</Box>
			<Box sx={{ px: { xs: 0, md: 5, xl: 8 }, py: { xs: 4, md: 5, xl: 8 } }}>
				<Grid
					container
					columnSpacing={{ xs: 4, md: 8, xl: 12 }}
					rowSpacing={{ xs: 4, md: 8, xl: 12 }}
				>
					{items.map((item) => {
						return (
							<Grid item xs={12} md={6} lg={4} xl={3} key={item.id}>
								<ItemCard item={item} />
							</Grid>
						);
					})}
				</Grid>
			</Box>
		</div>
	);
}

export default Home;
