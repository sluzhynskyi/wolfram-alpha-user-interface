import wolframalpha  as wf

client = wf.Client("JYETQ2-WP5J5GX3ER")  # app_ID is the app id

q = "Solve limit (3*x^2 + 78)/(x^2 -15x) as x to inf"
res = client.query(q)
answer = next(res.results).text
print(answer)
