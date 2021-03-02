class FeatureExtraction:
    """
    input: 1 đoạn văn
    output: mảng các features của từng câu
    """
    def __init__(self, raw_data):
        self.raw_data = raw_data
        self.features = [[] for i in range(len(raw_data))]

    def __repr__(self):
        return self.__class__

    def __str__(self):
        return self.__class__

    def __call__(self, *args, **kwargs):
        for idx in range(len(self.raw_data)):
            self.extract(idx)
        return self.features

    def extract(self, idx):
        self.__rule_1(idx)
        self.__rule_2(idx)
        self.__rule_3(idx)
        self.__rule_4(idx)
        self.__rule_5(idx)
        self.__rule_6(idx)
        self.__rule_7(idx)
        self.__rule_8(idx)

    @staticmethod
    def is_subject(word):
        return word['kind'] == 'sub' and (word['type'] == 'N' or word['type'] == 'P')

    @staticmethod
    def is_adj_has_sentiment(word):
        return word['type'] == 'A' and word['sentiment'] != 'none'

    @staticmethod
    def is_verb_has_sentiment(word):
        return word['type'] == 'V' and word['sentiment'] != 'none'

    """
        Nếu có ngữ danh từ là chủ ngữ (subject)
        liên quan trực tiếp đến tính từ mang cảm xúc
        => rút trích cặp từ này.
    """
    def __rule_1(self, idx):
        for wid, word in enumerate(self.raw_data[idx]):
            if self.is_subject(word):
                if word['depend_on'] is not None:
                    dword = self.raw_data[idx][word['depend_on']]
                    if dword['type'] == 'A' and dword['sentiment'] != 'none':
                        f = {
                            'obj_1_idx': wid,
                            'obj_2_idx': word['depend_on'],
                            'rule': 1
                        }
                        self.features[idx].append(f)

                        if len(dword['conj']) > 0:
                            for other_w in dword['conj']:
                                f = {
                                    'obj_1_idx': wid,
                                    'obj_2_idx': other_w,
                                    'rule': 1
                                }
                                self.features[idx].append(f)


    """
        Nếu có ngữ danh từ là chủ ngữ (subject)
        là chủ thể trực tiếp của động từ mang cảm xúc
        thì rút trích cặp từ này.
    """
    def __rule_2(self, idx):
        for wid, word in enumerate(self.raw_data[idx]):
            if self.is_subject(word):
                if word['depend_on'] is not None:
                    dword = self.raw_data[idx][word['depend_on']]
                    if dword['type'] == 'V' and dword['sentiment'] != 'none':
                        f = {
                            'obj_1_idx': wid,
                            'obj_2_idx': word['depend_on'],
                            'rule': 2
                        }
                        self.features[idx].append(f)

                        if len(dword['conj']) > 0:
                            for other_w in dword['conj']:
                                f = {
                                    'obj_1_idx': wid,
                                    'obj_2_idx': other_w,
                                    'rule': 2
                                }
                                self.features[idx].append(f)

    """
        Nếu 1 ngữ danh từ T là subject của 1 từ H
        và H có mối quan hệ verb modifier(vmod) với từ mang cảm xúc S
        thi rút trích cặp từ S-T
    """
    def __rule_3(self, idx):
        for wid, word in enumerate(self.raw_data[idx]):
            if self.is_subject(word):
                if word['depend_on'] is not None:
                    dword = self.raw_data[idx][word['depend_on']]
                    if dword['type'] == 'V':
                        for dependency in dword['dependencies']:
                            dependency_word = self.raw_data[idx][dependency]
                            if dependency_word['kind'] == 'vmod' and dependency_word['sentiment'] != 'none':
                                f = {
                                    'obj_1_idx': wid,
                                    'obj_2_idx': dependency,
                                    'rule': 3
                                }
                                self.features[idx].append(f)

                                if len(dependency_word['conj']) > 0:
                                    for other_w in dependency_word['conj']:
                                        f = {
                                            'obj_1_idx': wid,
                                            'obj_2_idx': other_w,
                                            'rule': 3
                                        }
                                        self.features[idx].append(f)

    def __rule_4(self, idx):
        for wid, word in enumerate(self.raw_data[idx]):
            if self.is_subject(word):
                if word['depend_on'] is not None:
                    dword = self.raw_data[idx][word['depend_on']]
                    if dword['type'] == 'V':
                        for dependency in dword['dependencies']:
                            dependency_word = self.raw_data[idx][dependency]
                            if dependency_word['kind'] == 'dob' and dependency_word['sentiment'] != 'none':
                                f = {
                                    'obj_1_idx': wid,
                                    'obj_2_idx': dependency,
                                    'rule': 4
                                }
                                self.features[idx].append(f)

                                if len(dependency_word['conj']) > 0:
                                    for other_w in dependency_word['conj']:
                                        f = {
                                            'obj_1_idx': wid,
                                            'obj_2_idx': other_w,
                                            'rule': 4
                                        }
                                        self.features[idx].append(f)

    def __rule_5(self, idx):
        for wid, word in enumerate(self.raw_data[idx]):
            if self.is_adj_has_sentiment(word) and word['kind'] == 'nmod' and word['depend_on'] is not None:
                dword = self.raw_data[idx][word['depend_on']]
                if dword['type'] == 'N':
                    f = {
                        'obj_1_idx': wid,
                        'obj_2_idx': word['depend_on'],
                        'rule': 5
                    }
                    self.features[idx].append(f)

                    if len(dword['conj']) > 0:
                        for other_w in dword['conj']:
                            f = {
                                'obj_1_idx': wid,
                                'obj_2_idx': other_w,
                                'rule': 5
                            }
                            self.features[idx].append(f)

    def __rule_6(self, idx):
        for wid, word in enumerate(self.raw_data[idx]):
            if self.is_verb_has_sentiment(word):
                for dependency in word['dependencies']:
                    dependency_word = self.raw_data[idx][dependency]
                    if dependency_word['type'] == 'N' and dependency_word['kind'] == 'dob':
                        f = {
                            'obj_1_idx': wid,
                            'obj_2_idx': dependency,
                            'rule': 6
                        }
                        self.features[idx].append(f)

                        if len(dependency_word['conj']) > 0:
                            for other_w in dependency_word['conj']:
                                f = {
                                    'obj_1_idx': wid,
                                    'obj_2_idx': other_w,
                                    'rule': 6
                                }
                                self.features[idx].append(f)

    def __rule_7(self, idx):
        for wid, word in enumerate(self.raw_data[idx]):
            if self.is_verb_has_sentiment(word):
                for dependency in word['dependencies']:
                    dependency_word = self.raw_data[idx][dependency]
                    for dep_2_idx in dependency_word['dependencies']:
                        dep_2_word = self.raw_data[idx][dep_2_idx]
                        if dep_2_word['type'] == 'N' and dep_2_word['kind'] == 'dob':
                            f = {
                                'obj_1_idx': wid,
                                'obj_2_idx': dep_2_idx,
                                'rule': 7
                            }
                            self.features[idx].append(f)

                            if len(dep_2_word['conj']) > 0:
                                for other_w in dep_2_word['conj']:
                                    f = {
                                        'obj_1_idx': wid,
                                        'obj_2_idx': other_w,
                                        'rule': 7
                                    }
                                    self.features[idx].append(f)

    def __rule_8(self, idx):
        for wid, word in enumerate(self.raw_data[idx]):
            if word['type'] == 'N' and wid >= 1:
                if self.raw_data[idx][wid - 1]['txt'] == 'không':
                    f = {
                        'obj_1_idx': wid - 1,
                        'obj_2_idx': wid,
                        'rule': 8
                    }
                    self.features[idx].append(f)

