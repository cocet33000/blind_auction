import ItemCard from "./components/ItemCard";
import Box from "@mui/material/Box";
import Stack from "@mui/material/Stack";
import { Button } from "@mui/material";
import ItemDetailDialog from "./components/ItemDetailDialog";
import "slick-carousel/slick/slick.css";
import "slick-carousel/slick/slick-theme.css";
import "./css/slider.css";
import "./css/slider.css";
import React, { useState, useEffect } from "react";
import axios from "axios";

function Home() {
  const [items, setItems] = useState([]);
  const [clickedItem, setClickedItem] = useState("");
  const [isOpen, setOpen] = useState(false);
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
    <main>
      <ItemDetailDialog
        isOpen={isOpen}
        handleClose={() => {
          setOpen(false);
        }}
        item={clickedItem}
      />
      <Box sx={{ p: 3 }}>
        <Box sx={{ width: "100%" }}>
          <Stack spacing={5}>
            {items.map((item) => {
              return (
                <Button
                  component="div"
                  textTransform="none"
                  onClick={() => {
                    setOpen(true);
                    setClickedItem(item);
                  }}
                  sx={{
                    "&.MuiButtonBase-root:hover": {
                      bgcolor: "transparent",
                    },
                  }}
                >
                  <ItemCard
                    id={item.id}
                    name={item.name}
                    image_src={item.image_src}
                    bid_num={item.bid_num}
                  />
                </Button>
              );
            })}
          </Stack>
        </Box>
      </Box>
    </main>
  );
}

export default Home;
