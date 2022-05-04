import * as React from "react";
import { useTheme } from "@mui/material/styles";
import Box from "@mui/material/Box";
import Card from "@mui/material/Card";
import CardMedia from "@mui/material/CardMedia";
import Typography from "@mui/material/Typography";

export default function ImageCard(props) {
    const theme = useTheme();

    return (
        <Card
            sx={{
                display: "flex",
                padding: "5px",
                maxWidth: { xs: "150px", md: "200px" },
                margin: "auto",
            }}
        >
            <Box sx={{ display: "flex" }}>
                <CardMedia
                    component="img"
                    sx={{ maxWidth: { xs: "100px", md: "150px" } }}
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
                }}
            >
                <Typography sx={{ fontSize: { xs: 5, md: 15 } }}>
                    {props.bid_num}
                </Typography>
            </Box>
        </Card>
    );
}
