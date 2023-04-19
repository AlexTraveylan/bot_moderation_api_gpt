from src.app.core.format_response import formatResponse


def test_reformatStr():
    message_to_given = 'msldkfmzs { rep:"True", motif: "coucou" } dsfdsdfsdfsdf}'

    message_to_have = '{ rep:"True", motif: "coucou" }'

    formatResponse(message_to_given)

    assert formatResponse(message_to_given) == message_to_have
