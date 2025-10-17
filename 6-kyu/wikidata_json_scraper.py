import requests
import json

def wikidata_scraper(url):
	headers = {
		"Accept-Encoding": "gzip,deflate",
		"User-Agent": "Mozilla/5.0 (compatible; WikidataScraper/1.0)"
	}

	response = requests.get(url, headers=headers)
	data = response.json()
	entity_id = list(data['entities'].keys())[0]
	labels = data['entities'][entity_id].get('labels', {})
	label = labels.get('en', {}).get('value', 'No Label')
	descriptions = data['entities'][entity_id].get('descriptions', {})
	description = descriptions.get('en', {}).get('value', 'No Description')
	return {'ID': entity_id, 'LABEL': label, 'DESCRIPTION': description}
