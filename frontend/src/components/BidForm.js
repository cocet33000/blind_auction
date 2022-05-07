import * as React from "react";
import Button from "@mui/material/Button";
import TextField from "@mui/material/TextField";
import Dialog from "@mui/material/Dialog";
import DialogActions from "@mui/material/DialogActions";
import DialogContent from "@mui/material/DialogContent";
import DialogContentText from "@mui/material/DialogContentText";
import DialogTitle from "@mui/material/DialogTitle";
import axios from "axios";
import { useAuthenticator } from "@aws-amplify/ui-react";

export default function BidForm(props) {
  const [price, setPrice] = React.useState("");
  const [open, setOpen] = React.useState(false);
  const { authStatus } = useAuthenticator((context) => [context.authStatus]);
  const { user } = useAuthenticator((context) => [context.user]);

  const handleClickOpen = () => {
    setOpen(true);
  };

  const handleClose = () => {
    setOpen(false);
  };

  const bid = () => {
    const data = {
      user_name: user.username,
      item_id: props.item_id,
      price: Number(price),
    };

    console.log(data);

    axios
      .post("https://api.blind-auction.com/dev/bids", data)
      .then((response) => {
        console.log(response.data);
      })
      .catch((error) => {
        console.log("ERROR!! occurred in Backend.");
      });

    setOpen(false);
  };

  return (
    <div>
      <Button
        disabled={authStatus === "authenticated" ? false : true}
        variant="outlined"
        onClick={handleClickOpen}
      >
        BID
      </Button>
      <Dialog open={open} onClose={handleClose}>
        <DialogTitle>BID</DialogTitle>
        <DialogContent>
          <DialogContentText>入札</DialogContentText>
          <TextField
            autoFocus
            margin="dense"
            id="price"
            label="PRICE"
            type="number"
            value={price}
            onChange={(event) => setPrice(event.target.value)}
            fullWidth
            variant="standard"
          />
        </DialogContent>
        <DialogActions>
          <Button onClick={handleClose}>CANCEL</Button>
          <Button onClick={bid}>BID</Button>
        </DialogActions>
      </Dialog>
    </div>
  );
}
