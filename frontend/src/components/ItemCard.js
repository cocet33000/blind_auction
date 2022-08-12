import Stack from '@mui/material/Stack';
import Box from '@mui/material/Box';
import Card from '@mui/material/Card';
import CardMedia from '@mui/material/CardMedia';
import Typography from '@mui/material/Typography';
import PropTypes from 'prop-types';

export default function ItemCard(props) {
	return (
		<Box>
			<Card
				sx={{
					display: 'flex',
					padding: { xs: '20px', md: '30px' },
					maxWidth: { xs: '350px', md: '530px' },
					margin: 'auto',
					bgcolor: 'card.background',
					boxShadow: 3
				}}
			>
				<Stack spacing={3}>
					<Typography sx={{ fontSize: { xs: 25, md: 30 }, mb: 0 }}>
						{props.name}
					</Typography>
					<Box sx={{ display: 'flex' }}>
						<CardMedia
							component="img"
							sx={{ maxWidth: { xs: '330px', md: '500px' } }}
							image={props.image_src}
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
								{props.bid_num}
							</Typography>
						</Box>
					</Box>
				</Stack>
			</Card>
		</Box>
	);
}

ItemCard.propTypes = {
	name: PropTypes.string.isRequired,
	image_src: PropTypes.string.isRequired,
	bid_num: PropTypes.number.isRequired
};
