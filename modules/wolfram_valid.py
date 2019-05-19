import wolframalpha as wf

client = wf.Client("JYETQ2-WP5J5GX3ER")  # app_ID is the app id


def valid(text):
    """
    If wolfram has not answer on request returns False
    :param text: string
    :return: bool
    """
    res = client.query(text)
    # Wolfram cannot resolve the question
    if res['@success'] == 'false':
        return False
    # Else returns True
    return True
