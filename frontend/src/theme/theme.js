import { createTheme } from '@mui/material/styles';

const theme = createTheme({
  palette: {
    primary: {
      main: '#f5e3e6',
      contrastText: '#403f3f',
    },
    secondary: {
      main: '#6d6c6c',
      contrastText: '#403f3f',
    },
    background: {
      default: '#f5e3e6',
    },
    text: { primary: '#6d6c6c' },
  },
});

export default theme;
