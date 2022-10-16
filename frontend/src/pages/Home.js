import Box from '@mui/material/Box';
import 'slick-carousel/slick/slick.css';
import 'slick-carousel/slick/slick-theme.css';
import CountdownTimer from '../components/CountdownTimer';
import useGetItems from '../hooks/useGetItems';
import ItemCardGrid from '../components/ItemCardGrid';
import CircularProgress from '@mui/material/CircularProgress';

function Home() {
	const { items, auction } = useGetItems();
	if (!items | !auction) return <CircularProgress />;

	return (
		<div>
			<Box sx={{ p: 3 }}>
				<CountdownTimer targetDate={auction.end_date} />
			</Box>
			<ItemCardGrid items={items} />
		</div>
	);
}

export default Home;
