import {
	Authenticator,
	ThemeProvider as TP,
	useTheme
} from '@aws-amplify/ui-react';

import { useTheme as muiUseTheme } from '@mui/material/styles';

import { Navigate } from 'react-router-dom';
import Box from '@mui/material/Box';
import { Amplify } from 'aws-amplify';
import { Image, View, Text, translations } from '@aws-amplify/ui-react';
import '@aws-amplify/ui-react/styles.css';
import { I18n } from 'aws-amplify';
// I18n.putVocabularies(vocabularies);
I18n.putVocabularies(translations);
I18n.setLanguage('ja');
import awsExports from '../aws-exports';

const isLocalhost = !!(window.location.hostname === 'localhost');
const [localRedirectSignIn, productionRedirectSignIn] =
	awsExports.oauth.redirectSignIn.split(',');
const [localRedirectSignOut, productionRedirectSignOut] =
	awsExports.oauth.redirectSignOut.split(',');
const updatedAwsConfig = {
	...awsExports,
	oauth: {
		...awsExports.oauth,
		redirectSignIn: isLocalhost
			? localRedirectSignIn
			: productionRedirectSignIn,
		redirectSignOut: isLocalhost
			? localRedirectSignOut
			: productionRedirectSignOut
	}
};
Amplify.configure(updatedAwsConfig);

export default function CognitoAuthenticator() {
	const muiTheme = muiUseTheme();
	const theme = {
		name: 'Auth Example Theme',
		tokens: {
			colors: {
				background: {
					primary: {
						value: muiTheme.palette.authenticator.background.primary
					},
					secondary: {
						value: muiTheme.palette.authenticator.background.secondary
					}
				},
				font: {
					interactive: {
						value: muiTheme.palette.authenticator.font.interactive
					}
				}
			},
			components: {
				tabs: {
					item: {
						_focus: {
							color: {
								value: muiTheme.palette.authenticator.font.focus
							}
						},
						_hover: {
							color: {
								value: muiTheme.palette.authenticator.font.hover
							}
						},
						_active: {
							color: {
								value: muiTheme.palette.authenticator.font.active
							}
						}
					}
				},
				button: {
					fontWeight: { value: '{fontWeights.extrabold}' },
					primary: {
						backgroundColor: {
							value: muiTheme.palette.authenticator.components.button.background
						},
						_hover: {
							backgroundColor: {
								value: muiTheme.palette.authenticator.components.button.hover
							}
						},
						_focus: {
							backgroundColor: {
								value: muiTheme.palette.authenticator.components.button.focus
							}
						},
						_active: {
							backgroundColor: {
								value: muiTheme.palette.authenticator.components.button.active
							}
						}
					}
				}
			}
		}
	};
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
				<TP theme={theme}>
					<Authenticator
						signUpAttributes={['email']}
						components={components}
						formFields={formFields}
						socialProviders={['google']}
					>
						{() => <Navigate to="/" />}
					</Authenticator>
				</TP>
			</Box>
		</main>
	);
}
