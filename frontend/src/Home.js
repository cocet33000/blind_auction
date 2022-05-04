import ImageCard from "./components/ImageCard";
import Box from "@mui/material/Box";
import Stack from "@mui/material/Stack";
import "slick-carousel/slick/slick.css";
import "slick-carousel/slick/slick-theme.css";
import "./css/slider.css";
import "./css/slider.css";
import React, { useState, useEffect } from "react";
import axios from "axios";

function Home() {
  const [items, setItems] = useState([]);
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
  useEffect(() => {
    // Update the document title using the browser API
    axios
      .get("https://api.blind-auction.com/dev/items")
      .then((response) => {
        setItems(response.data.items);
        console.log(response.data);
      })
      .catch((error) => {
        console.log("ERROR!! occurred in Backend.");
      });
  }, []);

  return (
    <Box sx={{ width: "100%" }}>
      <Stack spacing={5}>
        {items.map((item) => {
          return (
            <ImageCard
              name={item.name}
              image_src={item.image_src}
              bid_num={item.bid_num}
            />
          );
        })}
      </Stack>
    </Box>
  );
}

export default Home;
