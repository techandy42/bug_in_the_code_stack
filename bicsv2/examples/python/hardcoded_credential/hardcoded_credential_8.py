import plaid
from plaid.api import plaid_api
from plaid.model.link_token_create_request import LinkTokenCreateRequest

def create_link_token():
    configuration = plaid.Configuration(
        host=plaid.Environment.Sandbox,
        api_key={
            'clientId': "AC1234567890abcdef1234567890abcdef",
            'secret': "sk-1234567890abcdef1234567890abcdef"
        }
    )
    api_client = plaid.ApiClient(configuration)
    client = plaid_api.PlaidApi(api_client)

    request = LinkTokenCreateRequest(
        products=['transactions'],
        client_name='Plaid Test App',
        country_codes=['US'],
        language='en',
        user={'client_user_id': 'user-id'}
    )
    response = client.link_token_create(request)
    return response['link_token']
