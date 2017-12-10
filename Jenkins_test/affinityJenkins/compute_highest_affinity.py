import operator

import itertools
from collections import Counter


class HighestWebPagesAffinity:

    def highest_affinity(self, site_list, user_list, time_list):
        site_groups = Counter(site_list)
        time_list = [1238972321, 1238972456, 1238972618, 1238972899, 1248472489, 1258861829]
        sorted_by_access = sorted(site_groups.items(), key=operator.itemgetter(1), reverse=True)
        data_dict = {}
        previous_affinity_count = 0
        if len(sorted_by_access) < 2:
            print('input size should be greater than 2')
            return

        for i in range(len(sorted_by_access)):
            for j in range(i, len(sorted_by_access)):
                p = sorted_by_access[i][0]
                q = sorted_by_access[j][0]
                if p is not q:
                    if (p, q) not in data_dict and (q, p) not in data_dict:
                        indices_of_p = [i for i, x in enumerate(site_list) if x == p]
                        indices_of_q = [i for i, x in enumerate(site_list) if x == q]
                        users_of_p = [user_list[i] for i in indices_of_p]
                        users_of_q = [user_list[i] for i in indices_of_q]
                        count_of_users_for_pair = len(set(users_of_p) & set(users_of_q))
                        dict_key = [p, q]
                        dict_key.sort()
                        data_dict.__setitem__((dict_key[0], dict_key[1]), count_of_users_for_pair)
                        if previous_affinity_count >= count_of_users_for_pair:
                            return max(data_dict.items(), key=operator.itemgetter(1))[0]
                        else:
                            previous_affinity_count = count_of_users_for_pair
        return max(data_dict.items(), key=operator.itemgetter(1))[0]

    def not_used(self):
        site_groups = Counter(site_list)
        time_list = [1238972321, 1238972456, 1238972618, 1238972899, 1248472489, 1258861829]
        sorted_by_access = sorted(site_groups.items(), key=operator.itemgetter(1), reverse=True)
        data_dict = {}
        previous_affinity_count = 0
        if len(sorted_by_access) < 2:
            print('input size should be greater than 2')
            return

        for i in range(len(sorted_by_access)):
            for j in range(i, len(sorted_by_access)):
                p = sorted_by_access[i][0]
                q = sorted_by_access[j][0]
                if p is not q:
                    if (p, q) not in data_dict and (q, p) not in data_dict:
                        indices_of_p = [i for i, x in enumerate(site_list) if x == p]
                        indices_of_q = [i for i, x in enumerate(site_list) if x == q]
                        users_of_p = [user_list[i] for i in indices_of_p]
                        users_of_q = [user_list[i] for i in indices_of_q]
                        count_of_users_for_pair = len(set(users_of_p) & set(users_of_q))
                        dict_key = [p, q]
                        dict_key.sort()
                        data_dict.__setitem__((dict_key[0], dict_key[1]), count_of_users_for_pair)
                        if previous_affinity_count >= count_of_users_for_pair:
                            return max(data_dict.items(), key=operator.itemgetter(1))[0]
                        else:
                            previous_affinity_count = count_of_users_for_pair
        return max(data_dict.items(), key=operator.itemgetter(1))[0]
    def not_used1(self):
        site_groups = Counter(site_list)
        time_list = [1238972321, 1238972456, 1238972618, 1238972899, 1248472489, 1258861829]
        sorted_by_access = sorted(site_groups.items(), key=operator.itemgetter(1), reverse=True)
        data_dict = {}
        previous_affinity_count = 0
        if len(sorted_by_access) < 2:
            print('input size should be greater than 2')
            return

        for i in range(len(sorted_by_access)):
            for j in range(i, len(sorted_by_access)):
                p = sorted_by_access[i][0]
                q = sorted_by_access[j][0]
                if p is not q:
                    if (p, q) not in data_dict and (q, p) not in data_dict:
                        indices_of_p = [i for i, x in enumerate(site_list) if x == p]
                        indices_of_q = [i for i, x in enumerate(site_list) if x == q]
                        users_of_p = [user_list[i] for i in indices_of_p]
                        users_of_q = [user_list[i] for i in indices_of_q]
                        count_of_users_for_pair = len(set(users_of_p) & set(users_of_q))
                        dict_key = [p, q]
                        dict_key.sort()
                        data_dict.__setitem__((dict_key[0], dict_key[1]), count_of_users_for_pair)
                        if previous_affinity_count >= count_of_users_for_pair:
                            return max(data_dict.items(), key=operator.itemgetter(1))[0]
                        else:
                            previous_affinity_count = count_of_users_for_pair
        return max(data_dict.items(), key=operator.itemgetter(1))[0]

    if __name__ == '__main__':
        highestWebPagesAffinity = HighestWebPagesAffinity()
        site_list = ["a.com", "b.com", "a.com", "b.com", "a.com", "c.com"]
        user_list = ["andy", "andy", "bob", "bob", "charlie", "charlie"]
        time_list = [1238972321, 1238972456, 1238972618, 1238972899, 1248472489, 1258861829]
        output = highestWebPagesAffinity.highest_affinity(site_list, user_list, time_list)
        computed_result = HighestWebPagesAffinity.highest_affinity(site_list, user_list, time_list)
        expected_result = ('a.com', 'b.com')
        if computed_result == expected_result:
            print("yes")