from unittest.mock import Mock


def create_user(email, send_email, user_exists):
    if user_exists:
        return False

    print("User created")
    send_email(email, "Welcome to our application!")

    return True


def test_create_new_user():
    mock_email = Mock()

    result = create_user(
        "john@example.com",
        mock_email,
        user_exists=False
    )

    assert result is True

    mock_email.assert_called_once_with(
        "john@example.com",
        "Welcome to our application!"
    )

    def test_existing_user():
        mock_email = Mock()

        result = create_user(
            "john@example.com",
            mock_email,
            user_exists=True
        )

        assert result is False

        mock_email.assert_not_called()