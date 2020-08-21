import pandas as pd
pd.set_option('display.max_colwidth', -1)


jeopardy_data = pd.read_csv("jeopardy.csv")
#print(jeopardy_data.columns)

# Renaming misformatted columns
jeopardy_data = jeopardy_data.rename(columns = {" Air Date": "Air Date", " Round" : "Round", " Category": "Category", " Value": "Value", " Question":"Question", " Answer": "Answer"})
print(jeopardy_data.columns)
#print(jeopardy_data["Question"])

def filter(words,data):
 filter = lambda x: all(word.lower() in 
 x.lower() for word in words)
 return jeopardy_data.Question.apply(filter)
filtered = filter(jeopardy_data,["king","england"])

filtered = filter(jeopardy_data, ["king", "england"])
#print(filtered)

Value_replaced = jeopardy_data.Value.replace('$', '')

jeopardy_data["Float Value"] = jeopardy_data["Value"].apply(lambda x: float(x[1:].replace(',','')) if x != "None" else 0)

filtered = filter(jeopardy_data, ["King"])
print(filtered["Float Value"].mean())

def get_answer_counts(data):
    return data["Answer"].value_counts()

print(get_answer_counts(filtered))




