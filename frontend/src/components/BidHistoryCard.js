import Grid from '@mui/material/Grid';
import Box from '@mui/material/Box';
// import Card from '@mui/material/Card';
import CardMedia from '@mui/material/CardMedia';
import Typography from '@mui/material/Typography';
import PropTypes from 'prop-types';
import Paper from '@mui/material/Paper';

export default function BidHistoryCard(props) {
	return (
		<Box>
			<Paper
				elevation={0}
				sx={{
					display: 'flex',
					padding: { xs: '20px', md: '30px' },
					maxWidth: { xs: '350px', md: '530px', lg: '800px' },
					margin: 'auto'
				}}
			>
				<Grid container spacing={2}>
					<Grid item xs={8}>
						<CardMedia
							component="img"
							sx={{ maxWidth: { xs: '180px', md: '360px' } }}
							image={props.bidHistory.item.image_src}
						/>
					</Grid>
					<Grid item xs={4} container>
						<Grid item xs container direction="column" spacing={2}>
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
									入札日：{props.bidHistory.bid.bided_at}
								</Typography>
							</Grid>
						</Grid>
					</Grid>
				</Grid>
			</Paper>
		</Box>
	);
}

BidHistoryCard.propTypes = {
	bidHistory: PropTypes.any.isRequired
};
