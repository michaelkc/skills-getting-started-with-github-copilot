def test_get_activities_returns_all_activities(client):
    # Arrange
    endpoint = "/activities"

    # Act
    response = client.get(endpoint)
    payload = response.json()

    # Assert
    assert response.status_code == 200
    assert isinstance(payload, dict)
    assert "Chess Club" in payload


def test_get_activities_has_expected_activity_structure(client):
    # Arrange
    endpoint = "/activities"

    # Act
    response = client.get(endpoint)
    payload = response.json()
    activity = payload["Chess Club"]

    # Assert
    assert response.status_code == 200
    assert "description" in activity
    assert "schedule" in activity
    assert "max_participants" in activity
    assert "participants" in activity
