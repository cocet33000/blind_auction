import ImageCard from "./components/ImageCard";
import Slider from "react-slick";
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
    arrows: true,
    // autoplay: true,
    speed: 500,
  };
  return (
      <Slider {...settings}>
        <ImageCard />
        <ImageCard />
        <ImageCard />
        <ImageCard />
        <ImageCard />
      </Slider>
  );
}

export default Home;
