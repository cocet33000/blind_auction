import * as React from "react";
import Box from "@mui/material/Box";
import Drawer from "@mui/material/Drawer";
import Button from "@mui/material/Button";
import Divider from "@mui/material/Divider";
import IconButton from "@mui/material/IconButton";
import MenuIcon from "@mui/icons-material/Menu";
import Typography from "@mui/material/Typography";
import Stack from "@mui/material/Stack";
import { Link, useNavigate } from "react-router-dom";

import { useAuthenticator } from "@aws-amplify/ui-react";

export default function MenuButton(props) {
  let navigate = useNavigate();
  const [isOpen, setOpen] = React.useState(false);
  const { authStatus } = useAuthenticator((context) => [context.authStatus]);
  const { user, signOut } = useAuthenticator((context) => [context.user]);

  const toggleDrawer = (open) => (event) => {
    if (
      event.type === "keydown" &&
      (event.key === "Tab" || event.key === "Shift")
    ) {
      return;
    }

    setOpen(open);
  };
  const handleSignIn = () => {
    navigate("/auth");
  };
  const handleSignUp = () => {
    navigate("/auth");
  };
  const unAuthenticatedList = [
    { name: "Sign in", onClick: handleSignIn },
    { name: "Sign up", onClick: handleSignUp },
  ];

  const authenticatedList = [
    { name: "profile", onClick: handleSignIn },
    { name: "mypage", onClick: handleSignIn },
    { name: "sign out", onClick: signOut },
  ];

  const list = (anchor) => (
    <Box
      sx={{ width: anchor === "top" || anchor === "bottom" ? "auto" : 250 }}
      role="presentation"
      onClick={toggleDrawer(false)}
      onKeyDown={toggleDrawer(false)}
    >
      <Box
        sx={{
          display: "flex",
          justifyContent: "center",
          p: 1,
          m: 1,
        }}
      >
        <Typography variant="h6" noWrap component="div" sx={{ mr: 2 }}>
          Menu
        </Typography>
      </Box>

      <Box
        sx={{
          display: "flex",
          justifyContent: "center",
          p: 1,
          m: 1,
        }}
      >
        <Stack
          direction="column"
          spacing={2}
          divider={<Divider orientation="vertical" flexItem />}
        >
          {(authStatus !== "authenticated"
            ? unAuthenticatedList
            : authenticatedList
          ).map((item) => {
            return (
              <Button variant="outlined" onClick={item.onClick}>
                {item.name}
              </Button>
            );
          })}
        </Stack>
      </Box>
    </Box>
  );

  return (
    <div>
      <IconButton
        size="large"
        aria-label="account of current user"
        aria-controls="menu-appbar"
        aria-haspopup="true"
        onClick={toggleDrawer(true)}
        color="inherit"
      >
        <MenuIcon />
      </IconButton>
      <Drawer
        anchor={"right"}
        open={isOpen}
        onClose={toggleDrawer(false)}
        color={"primary.main"}
      >
        {list(props.anchor)}
      </Drawer>
    </div>
  );
}
