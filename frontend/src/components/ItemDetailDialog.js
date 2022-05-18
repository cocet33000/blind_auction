import * as React from "react";
import Button from "@mui/material/Button";
import DialogTitle from "@mui/material/DialogTitle";
import Dialog from "@mui/material/Dialog";
import DialogActions from "@mui/material/DialogActions";
import DialogContent from "@mui/material/DialogContent";
import DialogContentText from "@mui/material/DialogContentText";
import { TextField } from "@mui/material";
import { InputAdornment } from "@mui/material";
import { Input } from "@mui/material";

export default function ItemDetailDialog(props) {
  return (
    <main>
      {props.item ? (
        <Dialog open={props.isOpen}>
          <DialogTitle>{props.item.name}</DialogTitle>
          <DialogContent>
            <img
              style={{ maxWidth: "100%", maxHeight: "calc(100vh - 64px)" }}
              src={props.item.image_src}
            />
            <DialogContentText sx={{ fontSize: 24 }}>
              {props.item.description}
            </DialogContentText>
            <Input
              fullWidth={true}
              placeholder={"初期価格：" + props.item.start_price}
              id="standard-adornment-amount"
              type="number"
              variant="standard"
              startAdornment={
                <InputAdornment position="start">¥</InputAdornment>
              }
            />
            <DialogActions>
              <Button onClick={props.handleClose}>Cancel</Button>
            </DialogActions>
          </DialogContent>
        </Dialog>
      ) : (
        <main></main>
      )}
    </main>
  );
}
