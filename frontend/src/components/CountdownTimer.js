import { useEffect, useState } from 'react';
import Grid from '@mui/material/Grid';
import Paper from '@mui/material/Paper';
import Typography from '@mui/material/Typography';
import Stack from '@mui/material/Stack';
import PropTypes from 'prop-types';

const ExpiredNotice = () => {
	return (
		<div className="expired-notice">
			<span>Expired!!!</span>
		</div>
	);
};
const DateTimeDisplay = ({ value, type }) => {
	var unit = '';
	switch (type) {
		case 0:
			unit = 'Days';
			break;
		case 1:
			unit = 'Hours';
			break;
		case 2:
			unit = 'Minutes';
			break;
		case 3:
			unit = 'Seconds';
			break;
	}
	return (
		<Paper
			sx={{
				width: { xs: 60, md: 100 },
				height: { xs: 75, md: 150 },
				textAlign: 'center'
			}}
			elevation={0}
		>
			<Stack spacing={0}>
				<Typography
					component="div"
					gutterBottom
					sx={{
						pb: 0,
						mb: 0,
						fontSize: { xs: 54, md: 96 }
					}}
				>
					{value}
				</Typography>
				<Typography
					component="div"
					gutterBottom
					sx={{
						pt: -1,
						mt: 0,
						fontSize: { xs: 20, md: 24 }
					}}
				>
					{unit}
				</Typography>
			</Stack>
		</Paper>
	);
};
DateTimeDisplay.propTypes = {
	value: PropTypes.string,
	type: PropTypes.string
};

const useCountdown = (targetDate) => {
	const countDownDate = new Date(targetDate).getTime();

	const [countDown, setCountDown] = useState(
		countDownDate - new Date().getTime()
	);
	const getReturnValues = (countDown) => {
		// calculate time left
		const days = Math.floor(countDown / (1000 * 60 * 60 * 24));
		const hours = Math.floor(
			(countDown % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60)
		);
		const minutes = Math.floor((countDown % (1000 * 60 * 60)) / (1000 * 60));
		const seconds = Math.floor((countDown % (1000 * 60)) / 1000);

		return [days, hours, minutes, seconds];
	};
	useEffect(() => {
		const interval = setInterval(() => {
			setCountDown(countDownDate - new Date().getTime());
		}, 1000);

		return () => clearInterval(interval);
	}, [countDownDate]);

	return getReturnValues(countDown);
};

const CountdownTimer = ({ targetDate }) => {
	const [days, hours, minutes, seconds] = useCountdown(targetDate);
	if (days + hours + minutes + seconds <= 0) {
		return <ExpiredNotice />;
	} else {
		return (
			<main>
				<Grid sx={{ flexGrow: 1 }} container spacing={1}>
					<Grid item xs={12}>
						<Grid container justifyContent="center" spacing={3}>
							<Grid key={'day'} item>
								<DateTimeDisplay value={days} type={0} />
							</Grid>
							<Grid key={'hours'} item>
								<DateTimeDisplay value={hours} type={1} />
							</Grid>
							<Grid key={'minutes'} item>
								<DateTimeDisplay value={minutes} type={2} />
							</Grid>
							<Grid key={'seconds'} item>
								<DateTimeDisplay value={seconds} type={3} />
							</Grid>
						</Grid>
					</Grid>
				</Grid>
			</main>
		);
	}
};
CountdownTimer.propTypes = {
	targetDate: PropTypes.any
};

export default CountdownTimer;
