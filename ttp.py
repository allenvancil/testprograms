data = [
    {'url': 'http://speedtest.gohilight.com:8080/speedtest/upload.php', 'lat': '45.5229', 'lon': '-122.9898', 'name': 'Hillsboro, OR', 'country': 'United States', 'cc': 'US', 'sponsor': 'City of Hillsboro', 'id': '37289', 'host': 'speedtest.gohilight.com:8080', 'd': 236.5900693679649, 'latency': 68.485}
    
]

k = data[0].keys()

v = data[0].values()


print(list(v)[7])
print(list(v)[6])

# {'url': 'http://74.85.229.3:8080/speedtest/upload.php', 'lat': '45.5236', 'lon': '-122.6750', 'name': 'Portland, OR', 'country': 'United States', 'cc': 'US', 'sponsor': 'SilverStarTelecom', 'id': '6531', 'host': '74.85.229.3:8080', 'd': 232.6646418842887, 'latency': 77.296},
#     {'url': 'http://speedtest.gohilight.com:8080/speedtest/upload.php', 'lat': '45.5229', 'lon': '-122.9898', 'name': 'Hillsboro, OR', 'country': 'United States', 'cc': 'US', 'sponsor': 'City of Hillsboro', 'id': '37289', 'host': 'speedtest.gohilight.com:8080', 'd': 236.5900693679649, 'latency': 78.988},
#     {'url': 'http://speedtest.wwest.net:8080/speedtest/upload.php', 'lat': '46.3309', 'lon': '-123.6385', 'name': 'Rosburg, WA', 'country': 'United States', 'cc': 'US', 'sponsor': 'Wahkiakum West Communications', 'id': '35198', 'host': 'speedtest.wwest.net:8080', 'd': 172.35609252076966, 'latency': 81.541}