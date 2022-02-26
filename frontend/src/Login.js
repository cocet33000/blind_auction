import { useCookies } from "react-cookie";
import { createContext, useState } from "react";
import App from "./App";
export const LoginContext = createContext();

function Login() {
  const [cookies] = useCookies(["isLogin"]);
  const [isLogin, setIsLogin] = useState(cookies.isLogin ? true : false);
  const loginState = {
    isLogin,
    setIsLogin,
  };

  return (
    <LoginContext.Provider value={loginState}>
      <App />
    </LoginContext.Provider>
  );
}

export default Login;
