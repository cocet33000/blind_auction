import { useCookies } from "react-cookie";
import { createContext, useState } from "react";
import App from "./App";
import { Authenticator } from '@aws-amplify/ui-react';

export const LoginContext = createContext();

function Login() {
  const [cookies] = useCookies(["isLogin"]);
  const [isLogin, setIsLogin] = useState(cookies.isLogin ? true : false);
  const loginState = {
    isLogin,
    setIsLogin,
  };

  return (
    <Authenticator.Provider>
      <LoginContext.Provider value={loginState}>
        <App />
      </LoginContext.Provider>
    </Authenticator.Provider>
  );
}

export default Login;
