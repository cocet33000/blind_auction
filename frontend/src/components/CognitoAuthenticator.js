import { Navigate } from 'react-router-dom';
import Box from '@mui/material/Box';
import { Amplify } from 'aws-amplify';
import { Authenticator } from '@aws-amplify/ui-react';
import {
	Image,
	View,
	useTheme,
	Text,
	translations
} from '@aws-amplify/ui-react';
import '@aws-amplify/ui-react/styles.css';
import { I18n } from 'aws-amplify';
// I18n.putVocabularies(vocabularies);
I18n.putVocabularies(translations);
I18n.setLanguage('ja');

Amplify.configure({
	aws_project_region: 'ap-northeast-1',
	aws_cognito_region: 'ap-northeast-1',
	aws_user_pools_id: 'ap-northeast-1_GDOgCTVlJ',
	aws_user_pools_web_client_id: '4ot1mjr2mj65h59kv3f09cvpcd'
});

export default function CognitoAuthenticator() {
	const formFields = {
		signIn: {
			username: {
				placeholder: 'ユーザ名 もしくは Eメール',
				isRequired: true
			}
		},
		signUp: {
			username: {
				order: 1
			},
			email: {
				order: 2
			},
			password: {
				order: 5
			},
			confirm_password: {
				order: 6
			}
		}
	};

	const components = {
		Header() {
			const { tokens } = useTheme();

			return (
				<View textAlign="center" padding={tokens.space.large}>
					<Image alt="BLIND AUCTION LOGO" src="/android-chrome-192x192.png" />
				</View>
			);
		},
		Footer() {
			const { tokens } = useTheme();

			return (
				<View textAlign="center" padding={tokens.space.large}>
					<Text color={`${tokens.colors.neutral['80']}`}>
						&copy;BLIND-AUCTION All Rights Reserved
					</Text>
				</View>
			);
		}
	};
	return (
		<main>
			<Box
				sx={{
					flexGrow: 1,
					marginTop: 8,
					display: 'flex',
					flexDirection: 'column',
					alignItems: 'center'
				}}
			>
				<Authenticator
					signUpAttributes={['email']}
					components={components}
					formFields={formFields}
				>
					{() => <Navigate to="/" />}
				</Authenticator>
			</Box>
		</main>
	);
}
