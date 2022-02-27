import {
    Card,
    CardMedia
} from '@mui/material';

import {styled} from '@mui/material/styles'

const CustomCard = styled(Card)(({ theme }) => ({
    marginLeft: 'auto',
    marginRight: 'auto',
    [theme.breakpoints.up('md')]:
    {
        width: '200px',
        height: '160px'
    },
    [theme.breakpoints.down('md')]:
    {
        width: '133px',
        height: '107px'
    },
}));

const CustomCardMedia = styled(CardMedia)(({theme}) => ({
    component: 'img',
    [theme.breakpoints.up('md')]:
    {
        width: '150px',
        paddingTop: '150px'
    },
    [theme.breakpoints.down('md')]:
    {
        width: '100px',
        paddingTop: '100px'
    },
    marginTop: '2%',
    marginBottom: '2%',
    marginLeft: '2%',
    marginRight: '15%',
}))

function ImageCard() {
  return (
      <CustomCard>
        <CustomCardMedia
            image="https://placehold.jp/00db75/ffffff/500x500.png"
        />
      </CustomCard>
  );
}

export default ImageCard;
