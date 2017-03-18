import datetime

from hyperopt import hp, fmin, tpe
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier

import workdir.classes.config
from qml.cv import QCV
from qml.models import QXgb, QStackModel, QAvg, QRankedAvg, QRankedByLineAvg
from workdir.classes.models import qm
import numpy as np

cv = QCV(qm)
print(datetime.datetime.now())
# for i in range(1, 14):
#     print(i, datetime.datetime.now(), cv.cross_val(1, i, force=False))



model_id = qm.add_by_params(
    QStackModel(
        [
            [1,7],
            [1,8],
            [1,9],
            [1,10],
            [1,11],
            [1,12],
            [1,13],
        ]
        , 2014
    ),
    '1'
)

print(model_id, cv.cross_val(model_id, -1, force=False))


# qm.qpredict(7750, 1)
#
# for mid in (2,6,7,8,9,10,11,12,13):
#     res = np.array([])
#     print(mid, datetime.datetime.now())
#     res = np.append(res, float(cv.cross_val(2014, mid, force=False)))
#     print(mid, datetime.datetime.now())
#     res = np.append(res, float(cv.cross_val(2014, mid, force=True)))
#     print(mid, datetime.datetime.now())
#     res = np.append(res, float(cv.cross_val(2014, mid, force=True)))
#
#     print('=====', mid, res.mean(), res.max()-res.min(), res.std(), res.tolist())



# if __name__ == '__main__':
#     cv = QCV(qm)
#
#
#     def fn(params):
#         model_id = qm.add_by_params(
#             RandomForestClassifier(
#                 max_depth=int(params['max_depth']),
#                 n_estimators=int(params['n_estimators']),
#                 max_features=float(params['max_features']),
#                 n_jobs=2
#             ),
#             'hyperopt rand_forest',
#             predict_fn='predict_proba'
#         )
#         res = cv.cross_val(model_id, 3  )
#         print(datetime.datetime.now(), res, model_id, params)
#         return res
#
#
#     space = {
#         'max_depth': hp.quniform('max_depth', 1, 10, 1),
#         'n_estimators': hp.quniform('n_estimators', 10, 1000, 1),
#         'max_features': hp.uniform('max_features', 0.2, 1)
#     }
#     best = fmin(fn, space, algo=tpe.suggest, max_evals=5000)
#     print(best)