import ItemCard from './ItemCard.js';
import Box from '@mui/material/Box';
import Grid from '@mui/material/Grid';
import PropTypes from 'prop-types';

const ItemCardGrid = (props) => {
	return (
		<Box sx={{ px: { xs: 0, md: 5, xl: 8 }, py: { xs: 4, md: 5, xl: 8 } }}>
			<Grid
				container
				columnSpacing={{ xs: 4, md: 8, xl: 12 }}
				rowSpacing={{ xs: 4, md: 8, xl: 12 }}
			>
				{props.items.map((item) => {
					return (
						<Grid item xs={12} md={6} lg={4} xl={3} key={item.id}>
							<ItemCard item={item} />
						</Grid>
					);
				})}
			</Grid>
		</Box>
	);
};
ItemCardGrid.propTypes = {
	items: PropTypes.any.isRequired
};
export default ItemCardGrid;
