import { Card, CardMedia } from "@mui/material";
import Typography from "@mui/material/Typography";
import Box from "@mui/material/Box";

import { styled } from "@mui/material/styles";

const CustomCard = styled(Card)({
  marginLeft: "auto",
  marginRight: "auto",
  width: "200px",
  height: "160px",
});

const CustomCardMedia = styled(CardMedia)({
  component: "img",
  width: "150px",
  paddingTop: "150px", // square
  marginTop: "2%",
  marginBottom: "2%",
  marginLeft: "2%",
  marginRight: "15%",
});

function ImageCard() {
  return (
    <CustomCard>
      <CustomCardMedia image="https://placehold.jp/00db75/ffffff/500x500.png" />
    </CustomCard>
  );
}

export default ImageCard;
