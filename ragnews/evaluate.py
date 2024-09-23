'''
This file is for evaluating our RAG system
using the Hairy Trumpet tool/dataset
'''
import ragnews
import json

class RAGEvaluator:
    def predict(self, masked_text):
        '''
        >>> model = RAGEvaluator()
        >>> model.predict('[MASK0] is the democratic nominee')
        ['Harris']
        >>> model.predict('[MASK0] i the democratic nominee and [MASK1] is the republican nominee')
        ['Harris', 'Trump']
        >>> model.predict('There is no mask token here')
        []
        '''
        valid_labels = ['Harris', 'Trump', 'Biden']
        # you might think about:
        # calling the ragnews.run_llm function directly;
        # so we will call the ragnews.rag function
        db = ragnews.ArticleDB('ragnews.db')
        textprompt = '''

        I will give you a sentence with masked tokens, such as [MASK0], [MASK1], etc. Your job is to predict the value of each masked token.
        - Valid values include: {valid_labels}.
        - You should output each predicted value as a single word, separated by a space if there are multiple masks.
        - Do not provide any explanation or extra words in your response.
        INPUT: [MASK0] is the democratic nominee
        OUTPUT: Harris

        INPUT: [MASK0] is the democratic nominee and [MASK1] is the republican nominee
        OUTPUT: Harris Trump


        INPUT: Democrats outperformed [MASK0]'s results in the 2020 U.S. presidential election in several 2022 House special elections, with abortion cited as a major contributor to their victories. Then during the 2023 elections, both Democratic and Republican operatives attributed the Democrats' overperformance streak to the growing bipartisan support of broad abortion rights in the wake of Dobbs decision. Thus, many conservative political analysts and commentators called a continued Republican alliance with the anti-abortion movement \"untenable\" and an \"electoral disaster\", and urged the party to favor abortion rights. Some issue polling has shown Trump, the 2024 Presidential Republican nominee, outrunning his party and closing the gap with Democrats on the issue of abortion, but no election data with Trump directly on the ballot has happened to verify these results
        OUTPUT: Biden

        '''
        output = ragnews.rag(textprompt, db, keywords_text=masked_text)

        return output

def load_data(filepath):
    '''
    Load the data from the provided file
    '''
    with open(filepath, 'r') as file:
        data = [json.loads(line) for line in file]
    return data

def evaluate_predictions(data):
    '''
    Evaluate the accuracy of predictions against the expected masks
    '''
    evaluator = RAGEvaluator()
    total = len(data)
    correct = 0

    for entry in data:
        masked_text = entry['masked_text']
        expected_masks = entry['masks']
        
        # Get the prediction
        prediction = evaluator.predict(masked_text).split()  # Split in case of multiple masks

        # Compare predictions with expected masks
        if prediction == expected_masks:
            correct += 1
        else:
            print(f"Mismatch!\nMasked text: {masked_text}\nExpected: {expected_masks}\nPredicted: {prediction}\n")

    # Calculate accuracy
    accuracy = correct / total if total > 0 else 0
    print(f"Accuracy: {accuracy * 100:.2f}%")

if __name__ == "__main__":
    # Load the data from the file
    filepath = 'hairy-trumpet/data/wiki__page=2024_United_States_elections,recursive_depth=0__dpsize=paragraph,transformations=[canonicalize, group, rmtitles, split]'
    data = load_data(filepath)

    # Evaluate the predictions
    evaluate_predictions(data)

import logging
logging.basicConfig(
format='%(asctime)s %(levelname)-8s %(message)s',
datefmt='%Y-%m-%d %H:%M:%S',
level=logging.INFO,
)
