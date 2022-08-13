import Stack from '@mui/material/Stack';
import Box from '@mui/material/Box';
import Card from '@mui/material/Card';
import CardMedia from '@mui/material/CardMedia';
import Typography from '@mui/material/Typography';
import PropTypes from 'prop-types';
import ItemDetailDialog from './ItemDetailDialog';
import { useState } from 'react';

export default function ItemCard(props) {
	const [clickedItem, setClickedItem] = useState('');
	const [isOpen, setOpen] = useState(false);

	return (
		<Box>
			<ItemDetailDialog
				isOpen={isOpen}
				handleClose={() => {
					setOpen(false);
				}}
				item={clickedItem}
			/>
			<Card
				onClick={() => {
					setOpen(true);
					setClickedItem(props.item);
				}}
				sx={{
					display: 'flex',
					padding: { xs: '20px', md: '30px' },
					maxWidth: { xs: '350px', md: '530px', lg: '800px' },
					margin: 'auto',
					bgcolor: 'card.background',
					boxShadow: 3
				}}
			>
				<Stack spacing={3}>
					<Typography sx={{ fontSize: { xs: 25, md: 30 }, mb: 0 }}>
						{props.item.name}
					</Typography>
					<Box sx={{ display: 'flex' }}>
						<CardMedia
							component="img"
							sx={{ maxWidth: { xs: '360px', md: '500px', lg: '800px' } }}
							image={props.item.image_src}
						/>
					</Box>
					<Box
						sx={{
							display: 'flex',
							flexDirection: 'column',
							width: { xs: '5px', md: '30px' },
							padding: { xs: '3px', md: '10px' },
							zIndex: 0
						}}
					>
						<Box sx={{ height: '35px' }}>
							<Typography sx={{ fontSize: { xs: 15, md: 20 } }}>
								{props.item.bid_num}
							</Typography>
						</Box>
					</Box>
				</Stack>
			</Card>
		</Box>
	);
}

ItemCard.propTypes = {
	item: PropTypes.any.isRequired,
	bid_num: PropTypes.number.isRequired,
	onClick: PropTypes.any
};
