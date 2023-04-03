import pandas as pd

from src.data_classes.conversational_turn import ConversationalTurn, Document
from src.mi_systems.retriever import SparseRetriever
from IPython import embed
from bs4 import BeautifulSoup as bs

retriever = SparseRetriever(
        collection="/scratch/sekulic/trecweb_index/",
        collection_type="trecweb")

ret = []
df = pd.read_csv("qid_query.csv")
for i, row in df.iterrows():
    turn = ConversationalTurn(
            turn_id=row["qid"], information_need=row["query"],
            user_utterance=row["query"],
            conversation_history=[],
            user_utterance_type="question",
            relevance_judgements=[]
        )
    docs = retriever.retrieve(turn)
    
    for i in range(len(docs)):
        ret.append({'qid': row['qid'],
                   'docid': docs[i].docid,
                   'score': docs[i].score,})

retdf = pd.DataFrame(ret)
retdf.to_csv("BM25_Ale.run")

