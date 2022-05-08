import { useState, useEffect } from "react";
import * as React from "react";
import AppBar from "@mui/material/AppBar";
import Box from "@mui/material/Box";
import Toolbar from "@mui/material/Toolbar";
import IconButton from "@mui/material/IconButton";
import Typography from "@mui/material/Typography";
import Menu from "@mui/material/Menu";
import MenuIcon from "@mui/icons-material/Menu";
import Container from "@mui/material/Container";
import Button from "@mui/material/Button";
import MenuItem from "@mui/material/MenuItem";
import { ThemeProvider, createTheme } from "@mui/material/styles";
import AccountCircleIcon from "@mui/icons-material/AccountCircle";
import LoginIcon from "@mui/icons-material/Login";
import Snackbar from "@mui/material/Snackbar";
import MuiAlert from "@mui/material/Alert";
import { Link, useNavigate } from "react-router-dom";
import { useAuthenticator } from "@aws-amplify/ui-react";

const Alert = React.forwardRef(function Alert(props, ref) {
  return <MuiAlert elevation={6} ref={ref} variant="filled" {...props} />;
});

const darkTheme = createTheme({
  palette: {
    mode: "dark",
    primary: {
      main: "#000000",
    },
  },
});

const ResponsiveAppBar = () => {
  let navigate = useNavigate();
  const { authStatus } = useAuthenticator((context) => [context.authStatus]);
  const { user, signOut } = useAuthenticator((context) => [context.user]);
  const [isNotification, setNotification] = useState("");

  useEffect(() => {
    setNotification(true);
    console.log("auth status is changed!");
  }, [authStatus]);

  const handleClose = (event, reason) => {
    setNotification(false);
  };

  const [anchorElNav, setAnchorElNav] = useState(null);
  const [anchorElUser, setAnchorElUser] = useState(null);

  const handleOpenNavMenu = (event) => {
    setAnchorElNav(event.currentTarget);
  };
  const handleOpenUserMenu = (event) => {
    setAnchorElUser(event.currentTarget);
  };

  const handleCloseNavMenu = () => {
    setAnchorElNav(null);
  };

  const handleCloseUserMenu = () => {
    setAnchorElUser(null);
  };

  const handleLogin = () => {
    navigate("/auth");
  };

  const handleLogout = () => {
    signOut();
  };

  const pages = [
    {
      text: "A",
      to: "/a",
    },
    {
      text: "B",
      to: "/b",
    },
  ];

  const authenticatedMenu = [
    {
      text:
        authStatus !== "authenticated"
          ? ""
          : "You are signed in as " + user.username,
      onClick: handleLogout,
    },
  ];

  const notAuthenticatedMenu = [
    {
      text: "ログイン",
      onClick: handleLogin,
    },
  ];

  return (
    <ThemeProvider theme={darkTheme}>
      <AppBar position="static" color="primary" enableColorOnDark>
        <Container maxWidth="xl">
          <Toolbar disableGutters>
            <Typography
              onClick={() => {
                navigate("/");
              }}
              variant="h6"
              noWrap
              component="div"
              sx={{ mr: 2, display: { xs: "none", md: "flex" } }}
            >
              BLIND AUCTION
            </Typography>

            <Box sx={{ flexGrow: 1, display: { xs: "flex", md: "none" } }}>
              <IconButton
                size="large"
                aria-label="account of current user"
                aria-controls="menu-appbar"
                aria-haspopup="true"
                onClick={handleOpenNavMenu}
                color="inherit"
              >
                <MenuIcon />
              </IconButton>
              <Menu
                id="menu-appbar"
                anchorEl={anchorElNav}
                anchorOrigin={{
                  vertical: "bottom",
                  horizontal: "left",
                }}
                keepMounted
                transformOrigin={{
                  vertical: "top",
                  horizontal: "left",
                }}
                open={Boolean(anchorElNav)}
                onClose={handleCloseNavMenu}
                sx={{
                  display: { xs: "block", md: "none" },
                }}
              >
                
              </Menu>
            </Box>
            <Typography
              onClick={() => {
                navigate("/");
              }}
              variant="h6"
              noWrap
              component="div"
              sx={{ flexGrow: 1, display: { xs: "flex", md: "none" } }}
            >
              BLIND AUCTION
            </Typography>
            <Box sx={{ flexGrow: 1, display: { xs: "none", md: "flex" } }}>
            </Box>

            <Box sx={{ 
              flexGrow: 0,
              alignItems: "end",  
              }}>
              <IconButton onClick={handleOpenUserMenu} sx={{ p: 0 }}>
                {authStatus !== "authenticated" ? (
                  <LoginIcon fontSize="large" />
                ) : (
                  <AccountCircleIcon fontSize="large" />
                )}
              </IconButton>
              <Menu
                sx={{ mt: "45px" }}
                id="menu-appbar"
                anchorEl={anchorElUser}
                anchorOrigin={{
                  vertical: "top",
                  horizontal: "right",
                }}
                keepMounted
                transformOrigin={{
                  vertical: "top",
                  horizontal: "right",
                }}
                open={Boolean(anchorElUser)}
                onClose={handleCloseUserMenu}
              >
                {(authStatus !== "authenticated"
                  ? notAuthenticatedMenu
                  : authenticatedMenu
                ).map((setting) => (
                  <MenuItem key={setting.text} onClick={handleCloseUserMenu}>
                    <Typography textAlign="center" onClick={setting.onClick}>
                      {setting.text}
                    </Typography>
                  </MenuItem>
                ))}
              </Menu>
            </Box>
          </Toolbar>
        </Container>
      </AppBar>
      <Snackbar
        open={isNotification && authStatus === "authenticated"}
        autoHideDuration={6000}
        onClose={handleClose}
        anchorOrigin={{ vertical: "top", horizontal: "right" }}
      >
        <Alert onClose={handleClose} severity="success" sx={{ width: "100%" }}>
          {authStatus !== "authenticated"
            ? ""
            : "You are signed in as " + user.username}
        </Alert>
      </Snackbar>
    </ThemeProvider>
  );
};
export default ResponsiveAppBar;
