
import { createContext, useState } from "react";
import App from "./App";
import { Authenticator } from '@aws-amplify/ui-react';


function Login() {

  return (
    <Authenticator.Provider>
      <App />
    </Authenticator.Provider>
  );
}

export default Login;
