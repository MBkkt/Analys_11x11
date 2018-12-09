import pickle
import numpy
import catboost


def fun(x):
    with open('dicts/formation', mode='rb') as f:
        formation = pickle.load(f)
    with open('dicts/strategy', mode='rb') as f:
        strategy = pickle.load(f)
    with open('dicts/pass', mode='rb') as f:
        pas = pickle.load(f)

    x[0] = float(x[0])
    x[1] = int(x[1])
    x[2] = formation[x[2]]
    x[3] = strategy[x[3]]
    x[4] = pas[x[4]]
    return x


if __name__ == '__main__':

    a = input().split()
    b = input().split()
    model = catboost.CatBoostClassifier().load_model('model/CatboostCls', format='catboost')
    a = fun(a)
    b = fun(b)
    c = a + b
    c = [c]
    y = model.predict_proba(c)[:, 1]
    if y > 0.7:
        print('Second player win')
    elif y < 0.3:
        print('First player win')
    else:
        print('Draw')
