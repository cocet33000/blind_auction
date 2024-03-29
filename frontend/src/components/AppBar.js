import AppBar from '@mui/material/AppBar';
import Box from '@mui/material/Box';
import Toolbar from '@mui/material/Toolbar';
import Typography from '@mui/material/Typography';
import { useNavigate } from 'react-router-dom';

import MenuButton from './MenuButton';

const ResponsiveAppBar = () => {
	let navigate = useNavigate();

	return (
		<AppBar position="fixed" color="primary" enableColorOnDark="true">
			<Box sx={{ px: { xs: 2, md: 5 } }}>
				<Toolbar disableGutters>
					<Typography
						onClick={() => {
							navigate('/');
						}}
						variant="h6"
						noWrap
						component="div"
						sx={{ mr: 2, display: { xs: 'none', md: 'flex' } }}
					>
						BLIND AUCTION
					</Typography>

					<Typography
						onClick={() => {
							navigate('/');
						}}
						variant="h6"
						noWrap
						component="div"
						sx={{ flexGrow: 1, display: { xs: 'flex', md: 'none' } }}
					>
						BLIND AUCTION
					</Typography>
					<Box sx={{ flexGrow: 1, display: { xs: 'none', md: 'flex' } }}>
						{/* パティングの為 */}
					</Box>

					<Box sx={{ flexGrow: 0 }}>
						<MenuButton anchor="right" />
					</Box>
				</Toolbar>
			</Box>
		</AppBar>
	);
};
export default ResponsiveAppBar;
