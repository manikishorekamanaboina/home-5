import pytest
from all_questions import *
import pickle



#-----------------------------------------------------------
def question1():
    answers = {}

    # type: float
    # Calculate the probability.
    answers['(a)'] = 0.0288

    # type: float
    # Calculate the probability.
    answers['(b)'] = 0.002

    # type: float
    # Calculate the probability.
    answers['(c)'] = 0.0080
    return answers


#-----------------------------------------------------------
def question2():
    answers = {}

    # type: bool
    answers['(a) A'] = True

    # type: bool
    answers['(a) B'] = False

    # type: bool
    answers['(a) C'] = False

    # type: bool
    answers['(a) D'] = True

    # type: bool
    answers['(b) A'] = True

    # type: bool
    answers['(b) B'] = False

    # type: bool
    answers['(b) C'] = True

    # type: bool
    answers['(b) D'] = False

    # type: eval_float
    # The formulas should only use the variable 'p'. The formulas should be
    # a valid Python expression. Use the functions in the math module as
    # required.
    answers['(c) Weight update'] = '0.5 * math.log((1 - p) / p)'

    # type: float
    # the answer should be correct to 3 significant digits
    answers['(d) Weight influence'] = 1.528
    return answers


#-----------------------------------------------------------
def question3():
    answers = {}

    # type: string
    answers['Agree?'] = 'no'

    # type: explain_string
    answers['Explain'] = "Alans approach to prediction of stock market movements using a fair coin and taking the majority as result is by no means perfect ensemble methods application. Ensemble techniques incorporate predictions from multiple classifiers which work separately on training data without training and learning. Therefore, Alan`s approach is essentially fails and will not provide any valuable forecast for the stock market."
    return answers


#-----------------------------------------------------------
def question4():
    answers = {}

    # type: bool
    answers['(a) e=0.5, independent'] = False

    # type: bool
    answers['(b), independent'] = True

    # type: bool
    answers['(c) identical'] = False
    return answers


#-----------------------------------------------------------
def question5():
    answers = {}

    # type: string
    # choices: ['i', 'ii', 'iii', 'iv']
    answers['(a)'] = 'iii'

    # type: string
    # choices: ['i', 'ii', 'iii', 'iv']
    answers['(b)'] = 'i'

    # type: string
    # choices: ['i', 'ii', 'iii', 'iv']
    answers['(c)'] = 'ii'

    # type: string
    # choices: ['i', 'ii', 'iii', 'iv']
    answers['(d)'] = 'iv'
    return answers


#-----------------------------------------------------------
def question6():
    answers = {}

    # type: eval_float
    answers['(a) C1-TPR'] = "p"

    # type: eval_float
    answers['(a) C2-TPR'] = "2*p"

    # type: eval_float
    answers['(a) C1-FPR'] = "p"

    # type: eval_float
    answers['(a) C2-FPR'] = "2*p"

    # type: string
    # Hint: The random guess line in an ROC curve corresponds to TPR=FPR.
    # choices: ['yes', 'no']
    answers['(b) C2 better classifier than C1?'] = "no"

    # type: explain_string
    answers['(b) C2 better classifier than C1? Explain'] = "Both algorithms tend to achieve the same results as random guessing whenever true positive rate (TPR) equals false positive rate (FPR). Enhancing the probability of the positive class prediction will not improve the efficiency of C2, because it increases both TPR and FPR by the same number, making performance similar to random choice."
    # type: string
    # choices: ['TPR/FPR', 'precision/recall']
    answers['(c) Which metric?'] = "TPR/FPR"

    # type: explain_string
    answers['(c) explain'] = "TPR-FPR identify the positive predictions and their impact on performance when they are both positive and negative. As C1 and C2 both have the same TPR and FPR numbers, they can be seen to have the same level of performance on the ROC curve compares to that of the baseline random guess. True negatives neglecting precision and recall, which don't give any meaningful insights concerning classifiers that randomly predict as imbalanced classes."
    return answers

#-----------------------------------------------------------
def question7():
    answers = {}

    # type: string
    # choices: ['C1', 'C2', 'None']
    answers['(i) Best classifier?'] = "C2"

    # type: explain_string
    answers['(i) Best classifier, explain'] = "Here C2 beats C1 as it demonstrates the best recall/TPR and F1-measure. This shows that C2 perfectly identifies more positive cases and does it in a way that is better than C1."

    # type: string
    # choices: ['TPR-FPR', 'precision-recall-F1-Measure']
    answers['(ii) appropriate metric pair'] = "precision-recall-F1-Measure"

    # type: explain_string
    answers['(ii) appropriate metric pair, explain'] = "Precision, recall, and F1-measure serve as suitable metrics as they offer a comprehensive assessment of a classifier's performance, particularly crucial in scenarios with imbalanced datasets where positive instances are significantly less common than negatives."

    # type: string
    # choices: ['C1', 'C2', 'C3']
    answers['(iii) preferred classifier?'] = "C3"

    # type: explain_string
    answers['(iii) best classifier, explain'] = "C2 is favored due to its ability to strike a balance between precision and recall, evident from its highest F1-measure among the classifiers. Although C3 exhibits the highest precision, it does so at the cost of recall, rendering it less preferable for situations where capturing all positive instances is crucial."
    return answers


#-----------------------------------------------------------
def question8():
    answers = {}

    # type: eval_float
    answers['(a) precision for C0'] = '(p*100)/(p*1000)'

    # type: eval_float
    answers['(a) recall for C0'] = 'P'#0.5

    # type: eval_float
    answers['(b) F-measure of C0'] =  '(0.2 * P) / (0.1 + P)'#0.16666

    # type: string
    # choices: ['yes', 'no', 'unknown']
    answers['C1 better than random?'] = 'no'

    # type: float
    # What is the range of p for which C1 is better than random?  What is
    # "?" in the expression "p > ?"

    answers['p-range'] = 0.3#0.3
    return answers


#-----------------------------------------------------------
def question9():
    answers = {}

    # type: dict[string,float]
    # keys: ['recall', 'precision', 'F-measure', 'accuracy']
    answers['(i) metrics'] =  {
        'recall': 0.533,
        'precision': 0.6154,
        'F-measure': 0.5689,
        'accuracy': 0.8800
    }

    # type: string
    # choices: ['recall', 'precision', 'F-measure', 'accuracy']
    answers['(i) best metric?'] = 'F-measure'

    # type: string
    # choices: ['recall', 'precision', 'F-measure', 'accuracy']
    answers['(i) worst metric?'] = 'Accuracy'

    # type: explain_string
    answers['(ii) Explain your choices of best and worst metrics'] ="With the F-measure being the best suited metric due to its consideration of both precision and recall, providing the necessary balance as is the case in weather prediction where one outcome dominates. Accuracy, on the other hand, is not the most suitable metric due to it being that it can be skewed positively by a large number of true negatives, which isnt  always reflective of good predictive capabilities for the minority class"
    return answers


#-----------------------------------------------------------
def question10():
    answers = {}

    # type: string
    # choices: ['T1', 'T2']
    answers['(a) better test based on F-measure?'] = "T1"

    # type: string
    # choices: ['T1', 'T2']
    answers['(b) better test based on TPR/FPR?'] = "T2"

    # type: string
    # choices: ['F1', 'TPR/FPR']
    answers['(c) Which evaluation measure to use between the two tests?'] = "F1"

    # type: explain_string
    answers['(c) Which evaluation measure? Explain'] = "The F1-Score is chosen because of its merit of providing a more accurate and fair evaluation of a test by balancing both precision and recall. Therefore, this type of score is very apt for the assessment of clinical tests, where the cost or effects of false positives and false negatives are significant."
    # type: explain_string
    answers['(d) Example scenario where you would reverse choise in (c)'] = "In cases where identification of real cases at first place is the most critical, such as early screening of highly dangerous disease, TPR (True Positive Rate) and FPR (False Positive Rate) could be preferred because of their authentication of the ratio of the real cases and that of being wrong. This preference is due to their special focus on sensitivity rather than precision."


    return answers
#-----------------------------------------------------------
if __name__ == '__main__':
    answers_dict = {}
    answers_dict['question1'] = question1()
    answers_dict['question2'] = question2()
    answers_dict['question3'] = question3()
    answers_dict['question4'] = question4()
    answers_dict['question5'] = question5()
    answers_dict['question6'] = question6()
    answers_dict['question7'] = question7()
    answers_dict['question8'] = question8()
    answers_dict['question9'] = question9()
    answers_dict['question10'] = question10()

    with open('answers.pkl', 'wb') as f:
        pickle.dump(answers_dict, f)
