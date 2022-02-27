import ImageCard from "./components/ImageCard";
import Slider from "react-slick";
import {Stack, Box} from '@mui/material'
import "slick-carousel/slick/slick.css";
import "slick-carousel/slick/slick-theme.css";
import "./css/slider.css"

function Home() {
  const settings = {
    className: "slider",
    centerMode: true,
    dots: true,
    infinite: true,
    slidesToShow: 1,
    centerPadding: "30%",
    arrows: false,
    autoplay: true,
    speed: 500,
  };
  return (
      <Stack>
        <Box sx={{height: 60}}/>
        <Box>
          <Slider {...settings}>
            <ImageCard />
            <ImageCard />
            <ImageCard />
            <ImageCard />
            <ImageCard />
          </Slider>
        </Box>
      </Stack>
  );
}

export default Home;
