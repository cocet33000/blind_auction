import { Amplify } from 'aws-amplify';
import { Authenticator } from '@aws-amplify/ui-react';
import { Navigate } from "react-router-dom";
import '@aws-amplify/ui-react/styles.css';


Amplify.configure({
    aws_project_region: "ap-northeast-1",
    aws_cognito_region: "ap-northeast-1",
    aws_user_pools_id: "ap-northeast-1_GDOgCTVlJ",
    aws_user_pools_web_client_id: "4ot1mjr2mj65h59kv3f09cvpcd",
});

export default function CognitoAuthenticator() {

    return (
        <Authenticator signUpAttributes={['email']}>
            {({ signOut, user }) => (
                <Navigate to="/" />
            )}
        </Authenticator>
    );
}