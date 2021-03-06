card = json.loads(
    storage['card_create_dispute']['response']
)

card_debits_href = card['links']['cards.debits'].replace('{cards.id}', card['cards'][0]['id'])

request = {
    'uri': card_debits_href,
    'payload': {
        'amount': 5000,
        'appears_on_statement_as': 'Statement text',
        'description': 'Some descriptive text for the debit in the dashboard',
    },
    'card_href': card['cards'][0]['href']
}