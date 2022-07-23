import ItemCard from './components/ItemCard.js';
import Box from '@mui/material/Box';
import Stack from '@mui/material/Stack';
import { Button } from '@mui/material';
import ItemDetailDialog from './components/ItemDetailDialog';
import 'slick-carousel/slick/slick.css';
import 'slick-carousel/slick/slick-theme.css';
import './css/slider.css';
import './css/slider.css';
import { useState } from 'react';
import useSWR from 'swr';
import blindAuctionFetcher from './utils/blindAuctionFetcher.js';

function Home() {
	const [clickedItem, setClickedItem] = useState('');
	const [isOpen, setOpen] = useState(false);
	const { data, error } = useSWR('items', blindAuctionFetcher);

	if (error) return <div>failed to load</div>;
	if (!data) return <div>loading...</div>;
	return (
		<main>
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
						{data.items.map((item) => {
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
		</main>
	);
}

export default Home;
