import { Amplify } from 'aws-amplify';
import { Authenticator } from '@aws-amplify/ui-react';
import { Navigate } from "react-router-dom";
import Box from "@mui/material/Box";
import Container from '@mui/material/Container';
import Grid from '@mui/material/Grid';
import '@aws-amplify/ui-react/styles.css';


Amplify.configure({
    aws_project_region: "ap-northeast-1",
    aws_cognito_region: "ap-northeast-1",
    aws_user_pools_id: "ap-northeast-1_GDOgCTVlJ",
    aws_user_pools_web_client_id: "4ot1mjr2mj65h59kv3f09cvpcd",
});

export default function CognitoAuthenticator() {

    return (
        <main>
            <Box sx={{
                flexGrow: 1,
                marginTop: 8,
                display: 'flex',
                flexDirection: 'column',
                alignItems: 'center',
            }}>

                <Authenticator signUpAttributes={['email']}>
                    {({ signOut, user }) => (
                        <Navigate to="/" />
                    )}
                </Authenticator>

            </Box>
        </main>
    );
}