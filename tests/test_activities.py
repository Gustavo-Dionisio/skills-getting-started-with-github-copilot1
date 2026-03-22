import pytest


class TestGetActivities:
    """Test cases for GET /activities endpoint"""

    def test_get_activities_success(self, client):
        """Test successful retrieval of all activities"""
        # Arrange - no special setup needed as activities are predefined

        # Act
        response = client.get("/activities")

        # Assert
        assert response.status_code == 200
        data = response.json()
        assert isinstance(data, dict)
        assert len(data) == 9  # Based on the predefined activities

        # Check structure of first activity
        chess_club = data["Chess Club"]
        assert "description" in chess_club
        assert "schedule" in chess_club
        assert "max_participants" in chess_club
        assert "participants" in chess_club
        assert isinstance(chess_club["participants"], list)

    def test_get_activities_contains_expected_activities(self, client):
        """Test that response contains all expected activity names"""
        # Arrange
        expected_activities = [
            "Chess Club", "Programming Class", "Gym Class", "Basketball Team",
            "Tennis Club", "Drama Club", "Art Studio", "Debate Team", "Science Club"
        ]

        # Act
        response = client.get("/activities")

        # Assert
        assert response.status_code == 200
        data = response.json()
        assert set(data.keys()) == set(expected_activities)