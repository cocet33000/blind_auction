import * as React from "react";
import Stack from "@mui/material/Stack";
import { useTheme } from "@mui/material/styles";
import Box from "@mui/material/Box";
import Card from "@mui/material/Card";
import CardMedia from "@mui/material/CardMedia";
import Typography from "@mui/material/Typography";

export default function ImageCard(props) {
  const theme = useTheme();

  return (
    <Box>
      <Card
        sx={{
          display: "flex",
          padding: "20px",
          maxWidth: { xs: "350px", md: "550px" },
          margin: "auto",
        }}
      >
        <Stack spacing={3}>
          <Box sx={{ height: "10px" }}>
            <Typography sx={{ fontSize: { xs: 20, md: 25 } }}>
              {props.name}
            </Typography>
          </Box>
          <Box sx={{ display: "flex" }}>
            <CardMedia
              component="img"
              sx={{ maxWidth: { xs: "330px", md: "500px" } }}
              image={props.image_src}
              alt="Live from space album cover"
            />
          </Box>
          <Box
            sx={{
              display: "flex",
              flexDirection: "column",
              width: { xs: "5px", md: "30px" },
              padding: { xs: "3px", md: "10px" },
              zIndex: 0,
            }}
          >
            <Box sx={{ height: "35px" }}>
              <Typography sx={{ fontSize: { xs: 15, md: 20 } }}>
                {props.bid_num}
              </Typography>
            </Box>
          </Box>
        </Stack>
      </Card>
    </Box>
  );
}
