import ItemCard from './components/ItemCard.js';
import Box from '@mui/material/Box';
import Stack from '@mui/material/Stack';
//import Container from '@mui/material/Container';
import { Button } from '@mui/material';
// import { styled } from '@mui/system';
import ItemDetailDialog from './components/ItemDetailDialog';
import 'slick-carousel/slick/slick.css';
import 'slick-carousel/slick/slick-theme.css';
import './css/slider.css';
import './css/slider.css';
import { useState, useEffect } from 'react';
import axios from 'axios';
import CountdownTimer from './components/CountDown';

const socket = new WebSocket('wss://wss.blind-auction.com/deb');

function Home() {
	const [items, setItems] = useState([]);
	const [clickedItem, setClickedItem] = useState('');
	const [isOpen, setOpen] = useState(false);
	const updateItemBidnum = (item_id, bid_num) => {
		console.log(item_id);
		console.log(bid_num);
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
		// Update the document title using the browser API
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

	// const StyledContainer = styled(Box)(({ theme }) => ({
	// 	...theme.mixins.toolbar
	// }));

	//unix時間でカウントダウンを設定
	const THREE_DAYS_IN_MS = 3 * 24 * 60 * 60 * 1000;
	const NOW_IN_MS = new Date().getTime();
	const dateTimeAfterThreeDays = NOW_IN_MS + THREE_DAYS_IN_MS;

	return (
		<div>
			<Box sx={{ p: 3 }}>
				<CountdownTimer targetDate={dateTimeAfterThreeDays} />
			</Box>
			<ItemDetailDialog
				isOpen={isOpen}
				handleClose={() => {
					setOpen(false);
				}}
				item={clickedItem}
			/>
			<Box sx={{ p: 3 }}>
				<Box sx={{ width: '100%' }}>
					<Stack spacing={5}>
						{items.map((item) => {
							return (
								<Button
									key={item.id}
									component="div"
									textTransform="none"
									onClick={() => {
										setOpen(true);
										setClickedItem(item);
									}}
									sx={{
										'&.MuiButtonBase-root:hover': {
											bgcolor: 'transparent'
										}
									}}
								>
									<ItemCard
										id={item.id}
										name={item.name}
										image_src={item.image_src}
										bid_num={item.bid_num}
									/>
								</Button>
							);
						})}
					</Stack>
				</Box>
			</Box>
		</div>
	);
}

export default Home;
