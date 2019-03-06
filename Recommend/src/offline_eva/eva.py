import pandas as pd
from sklearn.metrics import roc_auc_score, precision_score, recall_score
from collections import defaultdict
# user_pro:用户ID 购买概率
# user_buy:用户ID 是否购买
# user_active:用户ID 是否活跃
# 全部用户的AUC


def all_user_auc(user_pro, user_buy):
    user_buy_pro = pd.merge(user_buy, user_pro, how='inner', on='user_id')
    buy_bool = user_buy_pro['buyed'].values
    buy_pro = user_buy_pro['buy_pro'].values
    return roc_auc_score(buy_bool, buy_pro)

# 活跃用户的AUC


def active_user_auc(user_pro, user_buy, user_active):
    active_user_set = user_active[user_active['active'] == '1'] # 取出活跃用户
    user_active_buy = pd.merge(active_user_set, user_buy, how='inner', on='user_id')
    user_active_buy_pro = pd.merge(user_active_buy, user_pro, how='inner', on='user_id')
    buy_bool = user_active_buy_pro['buyed'].values
    buy_pro = user_active_buy_pro['buy_pro'].values
    return roc_auc_score(buy_bool, buy_pro)

# 给定top n万全部用户或top 1万活跃用户，的准确率和召回率


def topn_all_eva(user_pro, user_buy):
    user_buy_pro = pd.merge(user_buy, user_pro, how='inner', on='user_id')
    buy_bool = user_buy_pro['buyed'].values
    buy_pro = user_buy_pro['buy_pro'].values
    y_pre_5 = (buy_pro > 0.5)
    return [precision_score(buy_bool, y_pre_5), recall_score(buy_bool, y_pre_5)]

# map3


def map_at_k(user_id, true, predict, k):
    u_label_score = defaultdict(list)
    for (uid, label, score) in zip(user_id, true, predict):
        u_label_score[uid].append((label, score))
    map_k = dict()
    for uid, user_ratings in u_label_score.items()[:k]:
        user_ratings.sort(key=lambda x: x[1], reverse=True)
        pos_num_k = sum(true for (true, _) in user_ratings[:k])
        if pos_num_k == 0.0:
            ap_k = 0.0
        else:
            ap_k = sum(true / (i + 1) for (i, (true, _)) in enumerate(user_ratings[:k])) / pos_num_k
        map_k[uid] = ap_k
    return sum(map_k.values()) / len(map_k)


def map3_all_eva(user_pro, user_buy):
    user_buy_pro = pd.merge(user_buy, user_pro, how='inner', on='user_id')
    buy_bool = user_buy_pro['buyed'].values
    buy_pro = user_buy_pro['buy_pro'].values
    user_id = user_buy_pro['user_id'].values
    return map_at_k(user_id, buy_bool, buy_pro)
