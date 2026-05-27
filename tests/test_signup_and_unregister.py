def test_signup_for_activity_succeeds(client):
    # Arrange
    activity_name = "Chess%20Club"
    email = "newstudent@mergington.edu"

    # Act
    response = client.post(f"/activities/{activity_name}/signup", params={"email": email})
    activities_response = client.get("/activities")
    participants = activities_response.json()["Chess Club"]["participants"]

    # Assert
    assert response.status_code == 200
    assert response.json() == {"message": f"Signed up {email} for Chess Club"}
    assert email in participants


def test_signup_for_unknown_activity_returns_not_found(client):
    # Arrange
    activity_name = "Unknown%20Club"
    email = "newstudent@mergington.edu"

    # Act
    response = client.post(f"/activities/{activity_name}/signup", params={"email": email})

    # Assert
    assert response.status_code == 404
    assert response.json() == {"detail": "Activity not found"}


def test_signup_duplicate_student_returns_bad_request(client):
    # Arrange
    activity_name = "Chess%20Club"
    email = "michael@mergington.edu"

    # Act
    response = client.post(f"/activities/{activity_name}/signup", params={"email": email})

    # Assert
    assert response.status_code == 400
    assert response.json() == {"detail": "Student already signed up"}


def test_unregister_from_activity_succeeds(client):
    # Arrange
    activity_name = "Chess%20Club"
    email = "daniel@mergington.edu"

    # Act
    response = client.delete(f"/activities/{activity_name}/unregister", params={"email": email})
    activities_response = client.get("/activities")
    participants = activities_response.json()["Chess Club"]["participants"]

    # Assert
    assert response.status_code == 200
    assert response.json() == {"message": f"Unregistered {email} from Chess Club"}
    assert email not in participants


def test_unregister_unknown_activity_returns_not_found(client):
    # Arrange
    activity_name = "Unknown%20Club"
    email = "newstudent@mergington.edu"

    # Act
    response = client.delete(f"/activities/{activity_name}/unregister", params={"email": email})

    # Assert
    assert response.status_code == 404
    assert response.json() == {"detail": "Activity not found"}


def test_unregister_student_not_signed_up_returns_not_found(client):
    # Arrange
    activity_name = "Chess%20Club"
    email = "notregistered@mergington.edu"

    # Act
    response = client.delete(f"/activities/{activity_name}/unregister", params={"email": email})

    # Assert
    assert response.status_code == 404
    assert response.json() == {"detail": "Student not signed up for this activity"}
