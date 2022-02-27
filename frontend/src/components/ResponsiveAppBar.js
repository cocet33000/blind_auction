import { useState, useContext } from "react";
import AppBar from "@mui/material/AppBar";
import Box from "@mui/material/Box";
import Toolbar from "@mui/material/Toolbar";
import IconButton from "@mui/material/IconButton";
import Typography from "@mui/material/Typography";
import Menu from "@mui/material/Menu";
import MenuIcon from "@mui/icons-material/Menu";
import Container from "@mui/material/Container";
import Button from "@mui/material/Button";
import Tooltip from "@mui/material/Tooltip";
import MenuItem from "@mui/material/MenuItem";
import AccountCircleIcon from "@mui/icons-material/AccountCircle";
import LoginIcon from "@mui/icons-material/Login";
import { useCookies } from "react-cookie";
import { Link } from "react-router-dom";

import { LoginContext } from "../Login";

const ResponsiveAppBar = () => {
  const { isLogin, setIsLogin } = useContext(LoginContext);
  const [, setCookie, removeCookie] = useCookies(["isLogin"]);

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
    setIsLogin(true);
    setCookie("isLogin", true);
  };

  const handleLogout = () => {
    setIsLogin(false);
    removeCookie("isLogin");
  };

  const pages = [
    {
      "text": "A",
      "to": "/a"
    },
    {
      "text": "B",
      "to": "/b"
    }
  ];

  const isLoginMenus = [
    {
      text: "ログアウト",
      onClick: handleLogout,
    },
  ];

  const isNotLoginMenus = [
    {
      text: "ログイン",
      onClick: handleLogin,
    },
  ];

  return (
      <AppBar position="static" color="primary">
        <Container maxWidth="xl">
          <Toolbar disableGutters>
            <Button
              color="secondary"
              noWrap
              component="div"
              sx={{ mr: 2, display: { xs: "none", md: "flex" } }}
              component={Link}
              to={'/'}
            >
              LOGO
            </Button>

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
                {pages.map((page) => (
                  <MenuItem key={page.text} onClick={handleCloseNavMenu}>
                    <Button
                      color="secondary"
                      key={page.text}
                      sx={{ my: 1, display: "block" }}
                      component={Link}
                      to={page.to}
                    >
                      {page.text}
                    </Button>
                  </MenuItem>
                ))}
              </Menu>
            </Box>
            <Box sx={{ flexGrow: 1, display: { xs: "flex", md: "none" } }}>
            <Button
              color="secondary"
              component="div"
              sx={{ flexGrow: 0, display: { xs: "flex", md: "none" } }}
              component={Link}
              to={"/"}
            >
              LOGO
            </Button>
            </Box>
            <Box sx={{ flexGrow: 1, display: { xs: "none", md: "flex" } }}>
              {pages.map((page) => (
                <Button
                  key={page.text}
                  onClick={handleCloseNavMenu}
                  sx={{ my: 2, color: "secondary.main", display: "block" }}
                  component={Link}
                  to={page.to}
                >
                  {page.text}
                </Button>
              ))}
            </Box>

            <Box sx={{ flexGrow: 0 }}>
              <IconButton onClick={handleOpenUserMenu} sx={{ p: 0 }}>
                {isLogin ? (
                  <AccountCircleIcon fontSize="large" />
                ) : (
                  <LoginIcon fontSize="large" />
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
                {(isLogin ? isLoginMenus : isNotLoginMenus).map((setting) => (
                  <MenuItem gdcolor="secondary" key={setting.text} onClick={handleCloseUserMenu}>
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
  );
};
export default ResponsiveAppBar;
