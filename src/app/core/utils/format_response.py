def formatResponse(response: str):
    begin = response.index("{")
    end = response.index("}") + 1

    return response.replace("'", '"')[begin:end]
