import Grid from '@mui/material/Grid';
import Box from '@mui/material/Box';
// import Card from '@mui/material/Card';
import CardMedia from '@mui/material/CardMedia';
import Typography from '@mui/material/Typography';
import PropTypes from 'prop-types';
//import Paper from '@mui/material/Paper';
import { useState } from 'react';
import Skeleton from '@mui/material/Skeleton';

export default function BidHistoryCard(props) {
	const formatDate = (bided_at, format) => {
		const bided_at_date = new Date(bided_at);
		format = format.replace(/yyyy/g, bided_at_date.getFullYear());
		format = format.replace(
			/MM/g,
			('0' + (bided_at_date.getMonth() + 1)).slice(-2)
		);
		format = format.replace(/dd/g, ('0' + bided_at_date.getDate()).slice(-2));
		format = format.replace(/HH/g, ('0' + bided_at_date.getHours()).slice(-2));
		format = format.replace(
			/mm/g,
			('0' + bided_at_date.getMinutes()).slice(-2)
		);
		format = format.replace(
			/ss/g,
			('0' + bided_at_date.getSeconds()).slice(-2)
		);
		format = format.replace(
			/SSS/g,
			('00' + bided_at_date.getMilliseconds()).slice(-3)
		);
		return format;
	};

	const [loading, setLoading] = useState(true);
	const img = new Image();
	img.src = props.bidHistory.item.image_src; // preload
	img.onload = () => {
		setLoading(false);
	};
	return (
		<Box
			elevation={0}
			sx={{
				padding: { xs: '20px', md: '30px' },
				maxWidth: { xs: '350px', md: '530px', lg: '800px' },
				margin: 'auto'
			}}
		>
			<Grid container spacing={0} wrap="nowrap">
				<Grid
					container
					item
					xs={8}
					alignItems="center"
					justifyContent="center"
					wrap="nowrap"
				>
					{loading ? (
						<Box width={{ xs: '180px', md: '360px' }}>
							<Skeleton
								variant="rectangular"
								width={{ xs: '180px', md: '360px' }}
								height={118}
							/>
						</Box>
					) : (
						<CardMedia
							component="img"
							sx={{
								maxWidth: { xs: '180px', md: '360px' },
								borderRadius: '20px'
							}}
							image={props.bidHistory.item.image_src}
						/>
					)}
				</Grid>

				<Grid item xs={4} container sx={{ pl: 0 }}>
					<Grid
						item
						xs
						container
						direction="column"
						columnSpacing={{ xs: 1, sm: 2, md: 3 }}
						rowSpacing={1}
					>
						<Grid item>
							<Typography sx={{ fontSize: { xs: 15, md: 20 } }}>
								{props.bidHistory.item.name}
							</Typography>
						</Grid>
						<Grid item>
							<Typography sx={{ fontSize: { xs: 10, md: 20 } }}>
								入札金額：{props.bidHistory.bid.price}
							</Typography>
						</Grid>
						<Grid item>
							<Typography sx={{ fontSize: { xs: 10, md: 20 } }}>
								入札日：
								{formatDate(props.bidHistory.bid.bided_at, 'yyyy/MM/dd')}
							</Typography>
						</Grid>
					</Grid>
				</Grid>
			</Grid>
		</Box>
	);
}

BidHistoryCard.propTypes = {
	bidHistory: PropTypes.any.isRequired
};
