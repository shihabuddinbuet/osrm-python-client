

def route(client, points, alternative=None, steps=None,
          annotations=None, geometries=None,overview=None,
          continue_straight=None, waypoints=None):
    url = f"{client.base_url}route/{client.api_version}/{client.profile}/{points}"
    params = {
        "alternatives": alternative,
        "steps": steps,
        "geometries": geometries,
        "overview": overview,
        "annotations": annotations,
        "continue_straight": continue_straight,
        "waypoints": waypoints
    }

    return client._request(url, params)



