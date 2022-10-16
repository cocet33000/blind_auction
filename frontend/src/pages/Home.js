import Box from '@mui/material/Box';
import 'slick-carousel/slick/slick.css';
import 'slick-carousel/slick/slick-theme.css';
import CountdownTimer from '../components/CountdownTimer';
import useGetItems from '../hooks/useGetItems';
import ItemCardGrid from '../components/ItemCardGrid';

function Home() {
	//unix時間でカウントダウンを設定
	//const THREE_DAYS_IN_MS = 3 * 24 * 60 * 60 * 1000;
	//const NOW_IN_MS = new Date().getTime();
	//const dateTimeAfterThreeDays = NOW_IN_MS + THREE_DAYS_IN_MS;

	const { items, auction } = useGetItems();
	console.log(auction);

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
