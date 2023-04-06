import pandas as pd 

df = pd.read_csv("data/dataframeNew.csv")

ret = []
for i, row in df.iterrows():
    uid = row["UserID"]
    topic = row[f"TopicID"]
    for i in range(1, 12):
        query = row[f"Query{i}"]
        if not query or type(query) == float:
            break
        qid = uid + '-' + topic + '-' + str(i)
        ret.append({"qid": qid,
                    "query": query.rstrip()})

clean_df = pd.DataFrame(ret)
clean_df.to_csv("data/qid_query.csv", index=False)

