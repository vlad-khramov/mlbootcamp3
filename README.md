# mlbootcamp3
Scripts for solving mlbootcamp#3 competitions (http://mlbootcamp.ru/)

18th place http://mlbootcamp.ru/users/10/

This repo contains snapshot of qml library. For more info see https://github.com/quantum13/qml


# Result model
45 - postprocessing model of 1001331 (see work.py)

example of models params:
* 1001331	QRankedAvg	{"models": [[1000445, -1], [1000473, -1], [1000711, -1], [1000735, -1], [1000772, -1], [1000800, -1], [1000808, -1], [1000975, -1]]}
* 1000445	QStackModel	{"models": [[1552, 4], [2005, 2], [2789, 2], [2853, 2], [3350, 3], [1000210, 11], [1000351, 10]], "second_layer_model": 2014}
* 2014	QXgb	    {"booster": "gbtree", "eta": 0.0022, "eval_metric": "logloss", "max_depth": 4, "num_boost_round": 3349, "objective": "binary:logistic", "subsample": 0.6}
* 1000473	QStackModel	{"models": [[2, 1], [1528, 2], [2025, 2], [2124, 5], [2155, 5], [3191, 2], [3261, 2], [3289, 2], [1000130, 12], [1000205, 13], [1000247, 9]], "second_layer_model": 2014}
* 1000711	QRankedAvg	{"models": [[2014, 9], [1000168, 8], [1000177, 13], [1000218, 10], [1000241, 8], [1000254, 9], [1000310, 7]]}

for more info see data.sql


Example of ensembles selection see in work_ensembling.ipynb
Example of models selection see in work_archive.py and work_hyperopt.py


# Data versions

*  1: origin
*  2: 1 +  *2
*  3: 1 +  *3
*  4: 1 +  normalize
*  5: 4 +  *2
*  6: 1 +  */+2
*  7: 1 +  */+-2
*  8: 7 +  claster3
*  9: 7 +  claster5
* 10: 7 + impot
* 11: 9 + impot
* 12: 10 + clast3
* 13: 10 + clast4