from tcr_interactions.tcr_auth import tcrAuth

tcr = tcrAuth()
tcr.login()
headers = tcr.headers
